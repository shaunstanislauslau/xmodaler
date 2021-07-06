####################################### DATASETS #######################################
DATASETS:
  TRAIN: 'MSCoCoDataset'
  VAL: 'MSCoCoDataset'
  TEST: 'MSCoCoDataset'

###################################### DATALOADER ######################################
DATALOADER:
  TRAIN_BATCH_SIZE: 8
  TEST_BATCH_SIZE: 32
  NUM_WORKERS: 0
  FEATS_FOLDER: '/export1/dataset/mscoco_torch/feature/up_down_100'
  ANNO_FOLDER:  '/export1/dataset/open_source/mscoco'
  #FEATS_FOLDER: 'D:/export/dataset/mscoco_open_source/features/up_down_100'
  #ANNO_FOLDER:  'D:/export/dataset/mscoco_open_source'
  SEQ_PER_SAMPLE:  5
  MAX_FEAT_NUM: 50

######################################### Engine #########################################
ENGINE:
  NAME: 'DefaultTrainer'

######################################### Scheduled sampling #########################################
SCHEDULED_SAMPLING:
  START_EPOCH: 0
  INC_EVERY_EPOCH: 5
  INC_PROB: 0.05
  MAX_PROB: 0.25

######################################### MODEL #########################################
MODEL:
  VOCAB_SIZE: 10200 # include <BOS>/<EOS>
  META_ARCHITECTURE: 'TransformerEncoderDecoder'
  ENCODER: 'UpDownEncoder'
  ENCODER_DIM: 1000
  DECODER: 'UpDownDecoder'
  DECODER_DIM: 1000
  PREDICTOR: 'BasePredictor'
  PRED_DROPOUT: 0.5
  MAX_SEQ_LEN: 20

#################################### Token embedding ####################################
  TOKEN_EMBED:
    NAME: 'TokenBaseEmbedding'
    DIM: 1000
    ACTIVATION: 'relu'
    USE_NORM: False
    DROPOUT: 0.5

#################################### Visual embedding ####################################
  VISUAL_EMBED:
    NAME: 'VisualBaseEmbedding'
    IN_DIM: 2048
    OUT_DIM: 1000
    ACTIVATION: 'relu'
    USE_NORM: False
    DROPOUT: 0.5
  
####################################### Optimizer #######################################
SOLVER:
  NAME: 'Adam'
  EPOCH: 10
  CHECKPOINT_PERIOD: 1
  EVAL_PERIOD: 1
  BASE_LR: 0.0005
  BIAS_LR_FACTOR: 1.0
  WEIGHT_DECAY: 0.0
  WEIGHT_DECAY_NORM: 0.0
  WEIGHT_DECAY_BIAS: 0.0
  MOMENTUM: 0.0
  DAMPENING: 0.0
  NESTEROV: 0.0
  BETAS: [0.9, 0.999]
  EPS: 1e-8
  GRAD_CLIP: 0.1
  GRAD_CLIP_TYPE: 'value'
  NORM_TYPE: 2.0
  
####################################### lr scheduler ####################################### 
LR_SCHEDULER:
  NAME: 'StepLR'
  STEP_SIZE: 3
  GAMMA: 0.1

####################################### losses ####################################### 
LOSSES:
  NAMES: ['LabelSmoothing']
  LABELSMOOTHING: 0.1

####################################### scorer ####################################### 
SCORER:
  NAME: 'BaseScorer'
  TYPES: ['Cider']
  WEIGHTS: [1.0]
  GT_PATH: '/export1/dataset/mscoco_open_source/mscoco_train_gts.pkl'
  CIDER_CACHED: '/export1/dataset/mscoco_open_source/mscoco_train_cider.pkl'
  EOS_ID: 0

####################################### decode strategy ####################################### 
DECODE_STRATEGY:
  NAME: 'BeamSearcher'
  BEAM_SIZE: 3

####################################### evaluation ####################################### 
INFERENCE:
  NAME: 'COCOEvaler'
  VOCAB: '/export1/dataset/open_source/mscoco/coco_vocabulary.txt'
  #VOCAB: 'D:/export/dataset/mscoco_open_source/coco_vocabulary.txt'
  ID_KEY: 'image_id'
  CAP_KEY: 'caption'
  VAL_ANNFILE: '/export1/dataset/open_source/mscoco/captions_val5k.json'
  TEST_ANNFILE: '/export1/dataset/open_source/mscoco/captions_test5k.json'
  #VAL_ANNFILE: 'D:/export/dataset/mscoco_open_source/captions_val5k.json'
  #TEST_ANNFILE: 'D:/export/dataset/mscoco_open_source/captions_test5k.json'

