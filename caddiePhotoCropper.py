import os, sys
from PIL import Image
import face_recognition

directory = './photos'
directoryOutput = './results'
imageSize = 146,146

# Create output folder
if not os.path.exists(directoryOutput):
    os.makedirs(directoryOutput)

# Reading photo in photos folder
for readFileName in os.listdir(directory) :
    if not readFileName.endswith('.jpg'): continue
    fullname = os.path.join(directory, readFileName)
    writeFilePath = os.path.join(directoryOutput, readFileName)

    image = face_recognition.load_image_file(fullname)
    face_locations = face_recognition.face_locations(image)

    face_location = face_locations[0]
    top, right, bottom, left = face_location

    # Vertical
    ratio = int((bottom - top)/2)
    top_k = max(0, top - ratio*2)
    bottom_k = bottom + int(ratio*1.5)

    # Horizontal
    center = left + int((right - left)/2)
    radius = int((bottom_k - top_k)/2)
    left_k = max(0, center - radius)
    right_k = center + radius
    face_image = image[top_k:bottom_k, left_k:right_k]
    pil_image = Image.fromarray(face_image)
    pil_image.thumbnail(imageSize)
    pil_image.save(writeFilePath)
    message = 'imageName: ' + readFileName + ' crop successfully'
    print(message)

