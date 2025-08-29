# 1st Question: Write code to read a json file, and count numbre of chicken in the given image.
import json
json_file_path = 'D:\\496.json'
def count_chickens_in_json(file_path):
    with open(file_path, 'r') as file:
            data = json.load(file)
    return sum(1 for shape in data.get('shapes', []) if shape.get('label') == 'chicken')
print(f"The Number of 'chicken'is: {count_chickens_in_json(json_file_path)}")


#-----------------------------------------------------------------------------------------------


# Question2: Use the MediaPipe library to extract joint keypoints from humans.
import cv2
import mediapipe as mp
import json
import glob
import os
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)
image_folder = 'D:\\image Folder'  
output_folder = 'output_keypoints'
os.makedirs(output_folder, exist_ok=True)
for img_path in glob.glob(f"{image_folder}/*.jpg"):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)
    keypoints = []
    if results.pose_landmarks:
        for lm in results.pose_landmarks.landmark:
            keypoints.append({
                'x': lm.x,
                'y': lm.y,
                'z': lm.z,
                'visibility': lm.visibility
            })
    out_path = os.path.join(output_folder, os.path.splitext(os.path.basename(img_path))[0] + '.json')
    with open(out_path, 'w') as f:
        json.dump(keypoints, f, indent=2)
pose.close()
