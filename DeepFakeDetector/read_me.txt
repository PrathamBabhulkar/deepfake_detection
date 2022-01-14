Video:

input --> contains input video 
model_weights --> has weights for LRNet
landmarks --> stores landmarks in files for each video
Visualize --> contains tracing of facial landmarks {Don't bother with this}
shape_predictor_68_face_landmarks.dat --> This is essential in detecting facial landmarks for DLib

Executing LRNet:
1) python extract_landmarks.py
This will extract landmarks from input video in input directory.
2) python classify.py
Prints out results of classification

/* Remember To clean Input, Landmarks and Visualize folders after every RUN*/
Don't clear weights, model automaticaly loads weights


