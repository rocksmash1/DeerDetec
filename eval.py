from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="deer")
metrics = trainer.evaluateModel(model_path="deer\\models", json_path="deer\\json\\detection_config.json")
print(metrics)