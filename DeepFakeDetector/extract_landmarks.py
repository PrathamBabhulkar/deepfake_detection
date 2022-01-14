import argparse
import os
import numpy as np
import cv2
from DeepFakeDetector.landmark_utils import LandmarkUtils
l = LandmarkUtils()

#CALIB = ['Y', 'N']
#VIS = ['Y', 'N']

class ExtractLandmarks():
    def __init__(self):

        input_path = './DeepFakeDetector/input'
        visualize = "N"

        """
        Prepare the environment
        """
        assert os.path.exists(input_path), "Input path does not exist."
        output_path = "./DeepFakeDetector/landmarks/"
        if not os.path.exists(output_path):
            os.makedirs("./DeepFakeDetector/landmarks/")

        if visualize == 'Y':
            print("Settings: Visualize the extraction results.")
            use_visualization = True
        else:
            print("Settings: NOT visualize the extraction results.")
            use_visualization = False

        # use_visualization:
        visualize_path = "./visualize/"
        if use_visualization:
            if not os.path.exists(visualize_path):
                os.makedirs("./visualize/")



        videos = os.listdir(input_path)
        for video in videos:
            if video.startswith('.'):
                continue

            print("Extract landmarks from {}.".format(video))
            raw_data = self.detect_track(input_path, video, use_visualization, visualize_path)

            if len(raw_data) == 0:
                print("No face detected", video)
            else:
                np.savetxt(output_path + video + ".txt", raw_data, fmt='%1.5f')
            print("Landmarks data saved!")

    def detect_track(self, input_path, video, use_visualization, visualize_path):
        vidcap = cv2.VideoCapture(os.path.join(input_path, video))
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        frames = []
        while True:
            success, image = vidcap.read()
            if success:
                frames.append(image)
            else:
                break
        raw_data = l.detect_frames_track(frames, fps, use_visualization, visualize_path, video)

        vidcap.release()
        return np.array(raw_data)





# e = ExtractLandmarks()
    




