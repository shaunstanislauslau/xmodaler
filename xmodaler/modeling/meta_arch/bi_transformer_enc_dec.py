import torch
from torch import nn
from torch.autograd import Variable
import torch.nn.functional as F

from xmodaler.config import configurable
from xmodaler.config import kfg
from xmodaler.functional import pad_tensor, dict_to_cuda
from ..predictor import build_v_predictor
from .transformer_enc_dec import TransformerEncoderDecoder
from .build import META_ARCH_REGISTRY

__all__ = ["BiTransformerEncoderDecoder"]

@META_ARCH_REGISTRY.register()
class BiTransformerEncoderDecoder(TransformerEncoderDecoder):
    @configurable
    def __init__(
        self,
        *,
        vocab_size,
        max_seq_len,
        token_embed,
        visual_embed,
        encoder,
        decoder,
        predictor,
        greedy_decoder,
        beam_searcher,
        v_predictor,
    ):
        super().__init__(
            vocab_size=vocab_size,
            max_seq_len=max_seq_len,
            token_embed=token_embed,
            visual_embed=visual_embed,
            encoder=encoder,
            decoder=decoder,
            predictor=predictor,
            greedy_decoder=greedy_decoder,
            beam_searcher=beam_searcher,
            v_predictor=v_predictor
        )

    @classmethod
    def from_config(cls, cfg):
        ret = super().from_config(cfg)
        ret.update({ "v_predictor": None })
        return ret

    def get_extended_attention_mask(self, batched_inputs):
        if kfg.TOKENS_MASKS not in batched_inputs:
            batched_inputs[kfg.TOKENS_MASKS] = torch.ones((batched_inputs[kfg.ATT_MASKS].size(0), self.max_seq_len)).cuda()

        tmasks = batched_inputs[kfg.TOKENS_MASKS]
        tmasks = tmasks.to(dtype=next(self.parameters()).dtype)
        ext_u_tmasks = tmasks.unsqueeze(1).unsqueeze(2)
        ext_u_tmasks = (1.0 - ext_u_tmasks) * -10000.0
        ext_g_tmasks = ext_u_tmasks

        vmasks = batched_inputs[kfg.ATT_MASKS]
        vmasks = vmasks.to(dtype=next(self.parameters()).dtype)
        vmasks = vmasks.unsqueeze(1).unsqueeze(2)
        ext_vmasks = (1.0 - vmasks) * -10000.0

        return {
            kfg.TOKENS_MASKS: tmasks,
            kfg.EXT_U_TOKENS_MASKS: ext_u_tmasks,
            kfg.EXT_G_TOKENS_MASKS: ext_g_tmasks,
            kfg.ATT_MASKS: vmasks,
            kfg.EXT_ATT_MASKS: ext_vmasks
        }

    