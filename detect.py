from imageai.Detection import VideoObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
import os
from cv2 import cv2

execution_path = os.getcwd()

camera = cv2.VideoCapture(0) 

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("detection_model-ex-026--loss-0015.929.h5")
video_detector.setJsonPath("detection_config.json")
video_detector.loadModel()

# video_detector.detectObjectsFromVideo(camera_input=camera,
#                                           output_file_path=os.path.join(execution_path, "sadsadasd"),
#                                           frames_per_second=20,
#                                           minimum_percentage_probability=15,
#                                           log_progress=True)

video_path = video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "deervid.mp4"),
                                output_file_path=os.path.join(execution_path, "traffic_detected")
                                , frames_per_second=20, log_progress=True, minimum_percentage_probability=15)

# detector = VideoObjectDetection()
# detector.setModelTypeAsYOLOv3()
# detector.setModelPath(os.path.join(execution_path , "yol1.h5"))
# detector.loadModel()

# video_path = detector.detectObjectsFromVideo(camera_input=camera,
#                                 output_file_path=os.path.join(execution_path, "camera_detected_1")
#                                 , frames_per_second=20, log_progress=True)
# print(video_path)