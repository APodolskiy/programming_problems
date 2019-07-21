from typing import Callable

import math
import torch
from torch.optim.optimizer import Optimizer


class AdamOptimizer(Optimizer):
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.99), weight_decay=0, eps=1e-8):
        if not lr >= 0.0:
            raise ValueError(f"Bad learning rate: {lr}")
        if not 0.0 <= betas[0] < 1.0:
            raise ValueError(f"Bad beta_1: {betas[0]}")
        if not 0.0 <= betas[1] < 1.0:
            raise ValueError(f"Bad beta_2: {betas[1]}")
        if not weight_decay >= 0:
            raise ValueError(f"Bad weight decay: {weight_decay}")
        if not eps >= 0.0:
            raise ValueError(f"Bad eps parameter: {eps}")
        defaults = dict(lr=lr, betas=betas, weight_decay=weight_decay, eps=eps)
        super(AdamOptimizer, self).__init__(params=params, defaults=defaults)

    def step(self, closure: Callable = None):
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data
                if grad.is_sparse:
                    raise RuntimeError("Adam doesn't support sparse gradients!")

                state = self.state[p]
                if len(state) == 0:
                    state['step'] = 0
                    state['exp_avg_grad'] = torch.zeros_like(p.data)
                    state['exp_avg_grad_sq'] = torch.zeros_like(p.data)
                # Acquire optimizer parameters
                exp_avg_grad = state['exp_avg_grad']
                exp_avg_grad_sq = state['exp_avg_grad_sq']
                beta1, beta2 = group['betas']
                eps = group['eps']
                weight_decay = group['weight_decay']
                lr = group['lr']
                state['step'] += 1
                # Update model parameters
                if weight_decay > 0:
                    self.p.add_(-weight_decay*lr, self.p)

                exp_avg_grad = exp_avg_grad.mul_(beta1).add_(1 - beta1, grad)
                exp_avg_grad_sq = exp_avg_grad_sq.mul_(beta2).addcmul_(1 - beta2, grad, grad)
                denom = exp_avg_grad_sq.sqrt_().add_(eps)

                bias_corr1 = 1. - beta1 ** state['step']
                bias_corr2 = 1. - beta2 ** state['step']

                step_size = lr * math.sqrt(bias_corr2) / bias_corr1

                self.p.addcdiv_(-step_size, exp_avg_grad, denom)

        return loss
