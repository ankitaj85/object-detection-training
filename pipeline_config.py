# Configure pipeline.config

import yaml

with open("config.yaml",'r') as infile:
    config = yaml.load(infile.read(), Loader=yaml.SafeLoader)

FINE_TUNE_CHECKPOINT_TYPE = config["FINE_TUNE_CHECKPOINT_TYPE"]
FINE_TUNE_CHECKPOINT      = config["FINE_TUNE_CHECKPOINT"]
TRAIN_TFRECORD            = [config["TRAIN_TFRECORD"]]
TEST_TFRECORD             = [config["TEST_TFRECORD"]]
CONFIG_PATH               = config["CONFIG_PATH"]
NUM_CLASSES               = config["NUM_CLASSES"]
BATCH_SIZE                = config["BATCH_SIZE"]
LABEL_MAP                 = config["LABEL_MAP"]
NUM_STEPS                 = config["NUM_STEPS"]
LR_TOTAL_STEPS            = config["LR_TOTAL_STEPS"] 
LR_WARMUP_STEPS           = config["LR_WARMUP_STEPS"] 

import tensorflow as tf
from google.protobuf import text_format
import object_detection
from object_detection.protos import pipeline_pb2
pipeline = pipeline_pb2.TrainEvalPipelineConfig()                                                                                                                                                                                                          
with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:                                                                                                                                                                                                                     
    proto_str = f.read()                                                                                                                                                                                                                                          
    text_format.Merge(proto_str, pipeline)     

pipeline.train_config.optimizer.momentum_optimizer.learning_rate.cosine_decay_learning_rate.total_steps=LR_TOTAL_STEPS 
pipeline.train_config.optimizer.momentum_optimizer.learning_rate.cosine_decay_learning_rate.warmup_steps=LR_WARMUP_STEPS
pipeline.train_config.fine_tune_checkpoint = FINE_TUNE_CHECKPOINT
pipeline.train_config.fine_tune_checkpoint_type = FINE_TUNE_CHECKPOINT_TYPE
pipeline.train_config.batch_size=BATCH_SIZE 
pipeline.train_config.num_steps=NUM_STEPS               
pipeline.model.ssd.num_classes = NUM_CLASSES

# TRAIN INPUT PATH CONFIGURATION
pipeline.train_input_reader.tf_record_input_reader.input_path[:] = TRAIN_TFRECORD # it's a repeated field 
pipeline.train_input_reader.label_map_path = LABEL_MAP

# TEST INPUT PATH CONFIGURATION
pipeline.eval_input_reader[0].tf_record_input_reader.input_path[:] = TEST_TFRECORD # it's a repeated field 
pipeline.eval_input_reader[0].label_map_path = LABEL_MAP

config_text = text_format.MessageToString(pipeline)                                                                                                                                                                                                        
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:                                                                                                                                                                                                                       
    f.write(config_text)
