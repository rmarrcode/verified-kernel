#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAException.h>
#include <c10/cuda/CUDAGuard.h>
#include <torch/extension.h>

namespace verified_kernel {

at::Tensor matmul_cuda(const at::Tensor& A, const at::Tensor& B) {
  const int64_t M = A.size(0);
  const int64_t K = A.size(1);
  const int64_t N = B.size(1);

  const c10::cuda::CUDAGuard device_guard(A.device());
  at::Tensor C = at::empty({M, N}, A.options());

}

} // namespace verified_kernel
