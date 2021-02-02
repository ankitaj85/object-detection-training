cd ~/TensorFlow/models/research 
CONFIG_PATH=/root/TensorFlow/workspace/local/pre-trained-models/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8/pipeline.config
MODEL_DIR=/root/TensorFlow/workspace/local/model-checkpoints/2
EXPORT_MODEL=/root/TensorFlow/workspace/local/exported-models/2
python3 object_detection/exporter_main_v2.py \
    --input_type image_tensor \
    --pipeline_config_path $CONFIG_PATH \
    --trained_checkpoint_dir $MODEL_DIR \
    --output_directory $EXPORT_MODEL
    #--config_override " \
    #      model{ \
    #        faster_rcnn { \
    #         second_stage_post_processing { \
    #          batch_non_max_suppression { \
    #           score_threshold: 0.5 \
    #         } \
    #       } \
    #     } \
    #  }"

#If side inputs are desired, the following arguments could be appended
#(the example below is for Context R-CNN).
#   --use_side_inputs True \
#   --side_input_shapes 1,2000,2057/1 \
#   --side_input_names context_features,valid_context_size \
#   --side_input_types tf.float32,tf.int32
