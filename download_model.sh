# Download the checkpoint and put it into models/research/object_detection/test_data/
model_display_name=ssd_mobilenet_v1_fpn_640x640_coco17_tpu_8
DOWNLOAD_PATH=~/TensorFlow/workspace/local/pre-trained-raw/
EXTRACT_PATH=~/TensorFlow/workspace/local/pre-trained-models
echo ${DOWNLOAD_PATH}
echo $EXTRACT_PATH
if [ $model_display_name==ssd_mobilenet_v1_fpn_640x640_coco17_tpu_8 ]
then 
  if [ -f "$DOWNLOAD_PATH/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz" ] 
  then
    echo File Exist - Below Find List of Models
    ls $DOWNLOAD_PATH
  else
    wget  -q http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz -P ${DOWNLOAD_PATH}
    tar -xf ${DOWNLOAD_PATH}/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz -C $EXTRACT_PATH
  fi  
else
   echo "a is not equal to b"
fi
# https://cloud.google.com/storage/docs/gsutil/commands/cp#:~:text=The%20gsutil%20cp%20command%20allows%20you%20to%20copy,can%20also%20download%20text%20files%20from%20a%20bucket:
gsutil -m cp -r  ~/Tensorflow/ gs://object-detection-pipeline-demo/
#!mv centernet_hg104_512x512_coco17_tpu-8/checkpoint models/research/object_detection/test_data/
