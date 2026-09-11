// Tiled single-precision matmul: C[M,N] = A[M,K] @ B[K,N], row-major, fp32.
//
// This is the hand-written baseline the verification work is eventually meant
// to generate. Nothing here is verified yet; correctness is currently argued by
// the tests in tests/test_matmul.py only.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAException.h>
#include <c10/cuda/CUDAGuard.h>
#include <torch/extension.h>

namespace verified_kernel {

// One thread computes one output element; one block computes a kTile x kTile
// output tile, staging the corresponding A and B tiles in shared memory so each
// loaded element is reused kTile times.
constexpr int kTile = 16;

__global__ void matmul_tiled_kernel(
    const float* __restrict__ A,
    const float* __restrict__ B,
    float* __restrict__ C,
    int M,
    int N,
    int K) {
  // As is read as As[ty][k]: every thread in a warp sharing ty hits the same
  // address, which broadcasts. Bs is read as Bs[k][tx]: consecutive tx hit
  // consecutive banks. Neither pattern conflicts, so no padding is needed.
  __shared__ float As[kTile][kTile];
  __shared__ float Bs[kTile][kTile];

  const int tx = threadIdx.x;
  const int ty = threadIdx.y;
  const int row = blockIdx.y * kTile + ty;
  const int col = blockIdx.x * kTile + tx;

  float acc = 0.0f;

  const int num_tiles = (K + kTile - 1) / kTile;
  for (int t = 0; t < num_tiles; ++t) {
    const int a_col = t * kTile + tx;
    const int b_row = t * kTile + ty;

    // Out-of-range lanes stage zeros so the inner loop needs no bounds check
    // and the whole block still reaches both barriers.
    As[ty][tx] = (row < M && a_col < K) ? A[row * K + a_col] : 0.0f;
    Bs[ty][tx] = (b_row < K && col < N) ? B[b_row * N + col] : 0.0f;
    __syncthreads();

#pragma unroll
    for (int k = 0; k < kTile; ++k) {
      acc += As[ty][k] * Bs[k][tx];
    }
    // Guard the next iteration's stores against threads still reading this tile.
    __syncthreads();
  }

  if (row < M && col < N) {
    C[row * N + col] = acc;
  }
}

at::Tensor matmul_cuda(const at::Tensor& A, const at::Tensor& B) {
  const int64_t M = A.size(0);
  const int64_t K = A.size(1);
  const int64_t N = B.size(1);

  const c10::cuda::CUDAGuard device_guard(A.device());
  at::Tensor C = at::empty({M, N}, A.options());

  if (M == 0 || N == 0) {
    return C;
  }
  if (K == 0) {
    // Empty contraction: every output is the empty sum. Skip the launch, since
    // the kernel's tile loop would not run and C would stay uninitialized.
    C.zero_();
    return C;
  }

  const dim3 block(kTile, kTile);
  const dim3 grid(
      static_cast<unsigned int>((N + kTile - 1) / kTile),
      static_cast<unsigned int>((M + kTile - 1) / kTile));

  matmul_tiled_kernel<<<grid, block, 0, at::cuda::getCurrentCUDAStream()>>>(
      A.data_ptr<float>(),
      B.data_ptr<float>(),
      C.data_ptr<float>(),
      static_cast<int>(M),
      static_cast<int>(N),
      static_cast<int>(K));
  C10_CUDA_KERNEL_LAUNCH_CHECK();

  return C;
}

} // namespace verified_kernel

