// Validation and Python binding for the tiled matmul kernel.
//
// All argument checking lives here rather than being split with the Python
// wrapper, so there is exactly one place that decides what the kernel accepts.

#include <torch/extension.h>

namespace verified_kernel {

at::Tensor matmul_cuda(const at::Tensor& A, const at::Tensor& B);

at::Tensor matmul(const at::Tensor& A, const at::Tensor& B) {
  TORCH_CHECK(A.is_cuda(), "matmul: A must be a CUDA tensor, got ", A.device());
  TORCH_CHECK(B.is_cuda(), "matmul: B must be a CUDA tensor, got ", B.device());
  TORCH_CHECK(
      A.device() == B.device(),
      "matmul: A and B must be on the same device, got ",
      A.device(),
      " and ",
      B.device());

  TORCH_CHECK(
      A.scalar_type() == at::kFloat,
      "matmul: A must be float32, got ",
      A.scalar_type());
  TORCH_CHECK(
      B.scalar_type() == at::kFloat,
      "matmul: B must be float32, got ",
      B.scalar_type());

  TORCH_CHECK(A.dim() == 2, "matmul: A must be 2-D, got ", A.dim(), "-D");
  TORCH_CHECK(B.dim() == 2, "matmul: B must be 2-D, got ", B.dim(), "-D");
  TORCH_CHECK(
      A.size(1) == B.size(0),
      "matmul: shape mismatch, A is ",
      A.sizes(),
      " and B is ",
      B.sizes());

  // The kernel indexes with row-major strides directly.
  TORCH_CHECK(A.is_contiguous(), "matmul: A must be contiguous");
  TORCH_CHECK(B.is_contiguous(), "matmul: B must be contiguous");

  return matmul_cuda(A, B);
}

} // namespace verified_kernel

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def(
      "matmul",
      &verified_kernel::matmul,
      "Tiled fp32 matmul (CUDA)",
      pybind11::arg("A"),
      pybind11::arg("B"));
}

