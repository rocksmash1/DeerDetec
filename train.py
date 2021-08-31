from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="deer")
# train_from_pretrained_model="pretrained-yolov3.h5"
trainer.setTrainConfig(object_names_array=["deer"], batch_size=2, num_experiments=200)
trainer.trainModel()