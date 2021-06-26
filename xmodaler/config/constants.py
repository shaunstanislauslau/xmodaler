from .config import CfgNode as CN

_K = CN()

kfg = _K

_K.IDS = 'IDS'

_K.TOKENS_IDS = 'TOKENS_IDS'

_K.TARGET_IDS = 'TARGET_IDS'

_K.TOKEN_EMBED = 'TOKEN_EMBED'

_K.ATT_FEATS = 'ATT_FEATS'

_K.ATT_MASKS = 'ATT_MASKS'

_K.EXT_ATT_MASKS = 'EXT_ATT_MASKS'

_K.P_ATT_FEATS = 'P_ATT_FEATS'

_K.HIDDEN_STATES = 'HIDDEN_STATES'

_K.CELL_STATES = 'CELL_STATES'

_K.GLOBAL_FEATS = 'GLOBAL_FEATS'

_K.LOGITS = 'LOGITS'

_K.COCO_PATH = '../coco_caption'

_K.TEMP_DIR = './data/temp'