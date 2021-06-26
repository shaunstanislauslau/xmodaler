import torch
from torch import nn

from xmodaler.config import configurable
from xmodaler.config import kfg
from .build import PREDICTOR_REGISTRY

__all__ = ["BasicPredictor"]

@PREDICTOR_REGISTRY.register()
class BasicPredictor(nn.Module):
    @configurable
    def __init__(
        self,
        *,
        hidden_size: int,
        vocab_size: int   # include <BOS>/<EOS>
    ):
        super(BasicPredictor, self).__init__()
        self.logits = nn.Linear(hidden_size, vocab_size)
        self.vocab_size = vocab_size
        
    @classmethod
    def from_config(cls, cfg):
        return {
            "hidden_size": cfg.MODEL.DECODER_DIM,
            "vocab_size": cfg.MODEL.VOCAB_SIZE
        }

    @classmethod
    def add_config(cls, cfg):
        pass

    def forward(self, batched_inputs):
        hidden_states = batched_inputs[kfg.HIDDEN_STATES][-1]
        logits = self.logits(hidden_states)
        return logits