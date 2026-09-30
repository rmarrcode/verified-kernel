"""
PyTorch training-loop drills: fill in the gaps.

Five functions below have their bodies replaced with `raise NotImplementedError`.
Implement them one at a time, then run the self-checks:

    python exercises/pytorch_training_gaps.py            # run every check
    python exercises/pytorch_training_gaps.py --only 1   # just exercise 1
    python exercises/pytorch_training_gaps.py --list     # names only

Everything is synthetic and CPU-only, so there is nothing to download and each
check finishes in seconds. Only edit the bodies marked `YOUR CODE HERE`; the
checks assume the documented signatures and return values.

Requires: torch (>= 2.0 recommended).
"""

from __future__ import annotations

import argparse
import copy
import math
from dataclasses import dataclass, field

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


# ---------------------------------------------------------------------------
# Fixtures: tiny synthetic data + models. Nothing to fill in here.
# ---------------------------------------------------------------------------


def make_blobs(n_per_class: int = 150, n_classes: int = 4, seed: int = 0):
    """Gaussian blobs in 2-D, one per class. Returns (X, y)."""
    g = torch.Generator().manual_seed(seed)
    centers = torch.tensor([[2.0, 2.0], [-2.0, 2.0], [-2.0, -2.0], [2.0, -2.0]])
    centers = centers[:n_classes]
    xs, ys = [], []
    for c in range(n_classes):
        xs.append(torch.randn(n_per_class, 2, generator=g) * 0.6 + centers[c])
        ys.append(torch.full((n_per_class,), c, dtype=torch.long))
    X, y = torch.cat(xs), torch.cat(ys)
    perm = torch.randperm(X.shape[0], generator=g)
    return X[perm], y[perm]


class MLP(nn.Module):
    def __init__(self, in_dim: int = 2, hidden: int = 64, n_classes: int = 4, p_drop: float = 0.0):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),
            nn.Dropout(p_drop),
            nn.Linear(hidden, n_classes),
        )

    def forward(self, x):
        return self.net(x)


@dataclass
class FitResult:
    """Return type for `fit` (exercise 5)."""

    train_losses: list[float] = field(default_factory=list)
    val_losses: list[float] = field(default_factory=list)
    best_val_loss: float = math.inf
    best_epoch: int = 0  # 1-indexed; 0 means "never improved"
    epochs_run: int = 0


# ===========================================================================
# EXERCISE 1 — the basic training epoch
# ===========================================================================


def train_one_epoch(model, loader, loss_fn, optimizer, device, max_grad_norm=None):
    """Run exactly one pass over `loader` in training mode.

    For every (inputs, targets) batch:
      1. put the model in training mode (once, before the loop)
      2. move the batch to `device`
      3. clear stale gradients
      4. forward pass -> logits
      5. loss = loss_fn(logits, targets)   (assume reduction='mean')
      6. backward pass
      7. if `max_grad_norm` is not None, clip gradients to that global norm
         with torch.nn.utils.clip_grad_norm_
      8. optimizer step

    Returns:
        (avg_loss, accuracy) as plain Python floats, both averaged over
        *samples*, not over batches. The last batch may be smaller than the
        rest, so weight each batch's mean loss by its sample count.

    Do not let autograd graphs leak into your running totals: accumulate with
    `loss.item()` (or `.detach()`), never the loss tensor itself.
    """
    # ------------------------- YOUR CODE HERE -------------------------
    raise NotImplementedError("exercise 1: train_one_epoch")
    # ------------------------------------------------------------------


# ===========================================================================
# EXERCISE 2 — the evaluation loop
# ===========================================================================


def evaluate(model, loader, loss_fn, device):
    """Run one pass over `loader` without training.

    Same per-sample averaging rule as exercise 1, but:
      - the model must be in eval mode (the check uses a model with heavy
        dropout, so train-mode numbers will not match)
      - no gradients may be built or stored (the check asserts every
        `param.grad` is still None afterwards)

    Returns:
        (avg_loss, accuracy) as plain Python floats.
    """
    # ------------------------- YOUR CODE HERE -------------------------
    raise NotImplementedError("exercise 2: evaluate")
    # ------------------------------------------------------------------


# ===========================================================================
# EXERCISE 3 — gradient accumulation
# ===========================================================================


def accumulate_and_step(model, loss_fn, optimizer, micro_batches, device):
    """Simulate one large batch using several small ones, then take ONE step.

    `micro_batches` is a list of (inputs, targets) tuples. After this call the
    gradients must equal the gradients you would have gotten from a single
    forward/backward over `torch.cat(all inputs)` — i.e. scale each micro-batch
    loss so the sum telescopes into the full-batch mean. Assume all micro-batches
    have the same number of samples.

    Order matters: clear gradients once at the start, backward once per
    micro-batch, and call `optimizer.step()` once at the end.

    Returns:
        The accumulated full-batch loss as a float.
    """
    # ------------------------- YOUR CODE HERE -------------------------
    raise NotImplementedError("exercise 3: accumulate_and_step")
    # ------------------------------------------------------------------


# ===========================================================================
# EXERCISE 4 — learning-rate schedule (warmup + cosine decay)
# ===========================================================================


def lr_lambda(step: int, warmup_steps: int, total_steps: int) -> float:
    """LR multiplier for `torch.optim.lr_scheduler.LambdaLR`, called per step.

    Exact schedule the check expects:
      - step < warmup_steps:  linear warmup, step / max(1, warmup_steps)
                              (so step 0 -> 0.0 and step == warmup_steps -> 1.0)
      - otherwise:            cosine decay, 0.5 * (1 + cos(pi * progress)) with
                              progress = (step - warmup_steps) / max(1, total_steps - warmup_steps),
                              clamped into [0, 1] so steps past `total_steps`
                              stay at 0.0 instead of rising again.

    Returns:
        A float multiplier in [0, 1].
    """
    # ------------------------- YOUR CODE HERE -------------------------
    raise NotImplementedError("exercise 4: lr_lambda")
    # ------------------------------------------------------------------


# ===========================================================================
# EXERCISE 5 — the outer fit loop, with early stopping
# ===========================================================================


def fit(model, train_epoch_fn, eval_fn, max_epochs: int, patience: int) -> FitResult:
    """Drive up to `max_epochs` epochs and keep the best model by val loss.

    `train_epoch_fn()` and `eval_fn()` take no arguments and each return
    (loss, accuracy) — they stand in for exercises 1 and 2 so this loop can be
    tested on its own. Per epoch: train, then evaluate, then append both losses
    to the FitResult history.

    Early stopping / checkpointing rules:
      - an epoch improves only if its val loss is STRICTLY lower than the best
        seen so far
      - on improvement: record best_val_loss, set best_epoch (1-indexed), and
        snapshot the weights with copy.deepcopy(model.state_dict())
      - otherwise increment a patience counter; once it reaches `patience`,
        stop after that epoch
      - before returning, load the best snapshot back into `model` (if any
        epoch improved)

    Returns:
        A FitResult with both loss histories, best_val_loss, best_epoch, and
        epochs_run (how many epochs actually ran).
    """
    # ------------------------- YOUR CODE HERE -------------------------
    raise NotImplementedError("exercise 5: fit")
    # ------------------------------------------------------------------


# ===========================================================================
# Self-checks. Read them if you get stuck — they spell out the contracts.
# ===========================================================================


def check_1() -> None:
    torch.manual_seed(0)
    device = torch.device("cpu")
    X, y = make_blobs()
    loader = DataLoader(TensorDataset(X, y), batch_size=64, shuffle=True)
    model = MLP().to(device)
    loss_fn = nn.CrossEntropyLoss()
    opt = torch.optim.SGD(model.parameters(), lr=0.1)

    losses, accs = [], []
    for _ in range(12):
        loss, acc = train_one_epoch(model, loader, loss_fn, opt, device)
        assert isinstance(loss, float) and isinstance(acc, float), "return plain floats"
        assert 0.0 <= acc <= 1.0, f"accuracy out of range: {acc}"
        losses.append(loss)
        accs.append(acc)

    assert losses[-1] < losses[0] * 0.6, f"loss barely moved: {losses[0]:.3f} -> {losses[-1]:.3f}"
    assert accs[-1] > 0.85, f"final train accuracy too low: {accs[-1]:.3f}"

    # With a microscopic clip norm the gradients are scaled to ~0, so plain SGD
    # should leave the weights essentially untouched.
    before = [p.detach().clone() for p in model.parameters()]
    train_one_epoch(model, loader, loss_fn, opt, device, max_grad_norm=1e-12)
    delta = max((p.detach() - b).abs().max().item() for p, b in zip(model.parameters(), before))
    assert delta < 1e-8, f"max_grad_norm was ignored (weights moved by {delta:.2e})"


def check_2() -> None:
    torch.manual_seed(0)
    device = torch.device("cpu")
    X, y = make_blobs(n_per_class=125)  # 500 samples, batch 128 -> ragged last batch
    loader = DataLoader(TensorDataset(X, y), batch_size=128, shuffle=False)
    model = MLP(p_drop=0.9).to(device)
    loss_fn = nn.CrossEntropyLoss()

    # Reference: eval mode, whole dataset at once.
    model.eval()
    with torch.no_grad():
        logits = model(X.to(device))
        want_loss = loss_fn(logits, y.to(device)).item()
        want_acc = (logits.argmax(1) == y.to(device)).float().mean().item()

    model.train()  # your evaluate() is responsible for switching modes
    for p in model.parameters():
        p.grad = None

    loss, acc = evaluate(model, loader, loss_fn, device)
    assert abs(loss - want_loss) < 1e-5, (
        f"loss {loss:.6f} != {want_loss:.6f} — eval mode missing, or you averaged "
        "batch means instead of per-sample means"
    )
    assert abs(acc - want_acc) < 1e-6, f"accuracy {acc:.6f} != {want_acc:.6f}"
    assert all(p.grad is None for p in model.parameters()), "gradients were built during eval"


def check_3() -> None:
    torch.manual_seed(0)
    device = torch.device("cpu")
    X, y = make_blobs(n_per_class=32)
    model = MLP().to(device)
    loss_fn = nn.CrossEntropyLoss()
    init_state = copy.deepcopy(model.state_dict())

    # Reference: one forward/backward over the full batch.
    model.zero_grad(set_to_none=True)
    full_loss = loss_fn(model(X), y)
    full_loss.backward()
    want_grads = [p.grad.detach().clone() for p in model.parameters()]

    # Now the accumulated version, from identical starting weights.
    model.load_state_dict(init_state)
    for p in model.parameters():
        p.grad = torch.randn_like(p)  # stale grads that must be cleared
    opt = torch.optim.SGD(model.parameters(), lr=0.05)
    micro = [(X[i : i + 32], y[i : i + 32]) for i in range(0, X.shape[0], 32)]
    assert len(micro) == 4

    got_loss = accumulate_and_step(model, loss_fn, opt, micro, device)
    assert isinstance(got_loss, float), "return a plain float"
    assert abs(got_loss - full_loss.item()) < 1e-5, (
        f"loss {got_loss:.6f} != full-batch {full_loss.item():.6f} — check your scaling"
    )
    for i, (p, want) in enumerate(zip(model.parameters(), want_grads)):
        diff = (p.grad - want).abs().max().item()
        assert diff < 1e-5, f"param {i}: accumulated grad differs from full-batch grad by {diff:.2e}"

    moved = max((p.detach() - init_state[k]).abs().max().item()
                for k, p in zip(init_state, model.parameters()))
    assert moved > 0, "optimizer.step() was never called"


def check_4() -> None:
    warmup, total = 10, 100

    def want(step: int) -> float:
        if step < warmup:
            return step / max(1, warmup)
        progress = (step - warmup) / max(1, total - warmup)
        progress = min(max(progress, 0.0), 1.0)
        return 0.5 * (1.0 + math.cos(math.pi * progress))

    for step in range(0, total + 20):
        got = lr_lambda(step, warmup, total)
        assert abs(got - want(step)) < 1e-9, f"step {step}: got {got:.6f}, want {want(step):.6f}"

    assert lr_lambda(0, warmup, total) == 0.0
    assert abs(lr_lambda(warmup, warmup, total) - 1.0) < 1e-9
    assert abs(lr_lambda(total, warmup, total)) < 1e-9
    assert lr_lambda(total + 50, warmup, total) < 1e-9, "schedule must not climb back up"

    # It should also drop straight into LambdaLR without modification.
    model = MLP()
    opt = torch.optim.SGD(model.parameters(), lr=1.0)
    sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: lr_lambda(s, warmup, total))
    seen = []
    for _ in range(total):
        opt.step()
        sched.step()
        seen.append(opt.param_groups[0]["lr"])
    assert max(seen) > 0.99, "warmup never reached the base LR"
    assert seen[-1] < 0.01, "cosine tail never decayed"


def check_5() -> None:
    torch.manual_seed(0)
    model = MLP()
    first = next(model.parameters())

    val_schedule = [1.0, 0.8, 0.9, 0.85, 0.5, 0.4]  # best at epoch 2, then 2 bad epochs
    state = {"epoch": 0}

    def train_epoch_fn():
        state["epoch"] += 1
        with torch.no_grad():
            first.fill_(float(state["epoch"]))  # marker so we can spot the restore
        return (2.0 / state["epoch"], 0.5)

    def eval_fn():
        return (val_schedule[state["epoch"] - 1], 0.5)

    res = fit(model, train_epoch_fn, eval_fn, max_epochs=6, patience=2)

    assert res.epochs_run == 4, f"expected early stop after epoch 4, ran {res.epochs_run}"
    assert len(res.val_losses) == 4 and len(res.train_losses) == 4, "history length must match epochs_run"
    assert res.val_losses == val_schedule[:4], f"val history wrong: {res.val_losses}"
    assert abs(res.best_val_loss - 0.8) < 1e-9, f"best_val_loss wrong: {res.best_val_loss}"
    assert res.best_epoch == 2, f"best_epoch should be 1-indexed 2, got {res.best_epoch}"
    restored = first.detach().flatten()[0].item()
    assert abs(restored - 2.0) < 1e-9, f"best weights not restored (param = {restored}, expected 2.0)"

    # A run that keeps improving must use every epoch and never early-stop.
    state["epoch"] = 0
    val_schedule[:] = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
    res2 = fit(MLP(), train_epoch_fn, eval_fn, max_epochs=6, patience=2)
    assert res2.epochs_run == 6 and res2.best_epoch == 6, (
        f"monotonic run stopped early: epochs_run={res2.epochs_run}, best_epoch={res2.best_epoch}"
    )


CHECKS = [
    ("train_one_epoch", check_1),
    ("evaluate", check_2),
    ("accumulate_and_step", check_3),
    ("lr_lambda", check_4),
    ("fit", check_5),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", type=int, metavar="N", help="run just exercise N (1-5)")
    parser.add_argument("--list", action="store_true", help="list the exercises and exit")
    args = parser.parse_args()

    if args.list:
        for i, (name, _) in enumerate(CHECKS, 1):
            print(f"{i}. {name}")
        return 0

    selected = CHECKS if args.only is None else [CHECKS[args.only - 1]]
    failures = 0
    for i, (name, check) in enumerate(selected, 1 if args.only is None else args.only):
        try:
            check()
        except NotImplementedError as e:
            print(f"[ TODO ] {i}. {name}: {e}")
            failures += 1
        except AssertionError as e:
            print(f"[ FAIL ] {i}. {name}: {e}")
            failures += 1
        except Exception as e:  # noqa: BLE001 - surface the error, keep going
            print(f"[ERROR ] {i}. {name}: {type(e).__name__}: {e}")
            failures += 1
        else:
            print(f"[ PASS ] {i}. {name}")

    print(f"\n{len(selected) - failures}/{len(selected)} passing")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

