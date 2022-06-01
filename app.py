import os
import time
import shutil
import tempfile
import numpy as np
import streamlit as st

import cv2
import face_recognition
from sklearn.cluster import DBSCAN
from imutils import build_montages

flag1 = 0

st.set_page_config(layout = 'wide')

#st.title("Any Face Clustering")
st.markdown("<h1 style='text-align: center; color: grey;'>Any Face Clustering</h1>", unsafe_allow_html=True)

st.text(" ")
st.text("Upload Images of Multiple Faces (with AT LEAST 3 images of a particular face).")
st.text("Please wait a while after uploading the images until you see a dialog box stating that the images were uploaded successfully.")
st.text("Sometimes Streamlit takes unusually more time to upload the images... if failed, try compressing the images before uploading.")

uploaded_files = st.file_uploader("", type = ["png","jpg","jpeg"], accept_multiple_files = True)

no_of_files = len(uploaded_files)

if no_of_files > 0:
  placeholder = st.empty()
  placeholder.success("{} Images uploaded successfully!".format(no_of_files))
  time.sleep(3)
  placeholder.empty()
  data = []
  
  for f in uploaded_files:
    tfile = tempfile.NamedTemporaryFile(delete = False)
    tfile.write(f.read())
    image = cv2.imread(tfile.name)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model = "cnn")
    encodings = face_recognition.face_encodings(rgb, boxes)
    d = [{"imagePath": tfile.name, "loc": box, "encoding": enc} for (box, enc) in zip(boxes, encodings)]
    data.extend(d)
  
  # converting the data into a numpy array
  data_arr = np.array(data)
  # extracting the 128-d facial encodings and placing them in a list
  encodings_arr = [item["encoding"] for item in data_arr]

  # initializing and fitting the clustering model on the encoded data
  cluster = DBSCAN(min_samples = 3)
  cluster.fit(encodings_arr)
  st.balloons()
  
  labelIDs = np.unique(cluster.labels_)
  numUniqueFaces = len(np.where(labelIDs > -1)[0])
  
  st.subheader("Number of unique faces identified (excluding the unknown faces) is: " + str(numUniqueFaces))

  if flag1 == 0:
    cols1 = st.columns(numUniqueFaces + 1)
    flag1 = 1

  # loop over the unique face integers
  for labelID in labelIDs:
    idxs = np.where(cluster.labels_ == labelID)[0]
    idxs = np.random.choice(idxs, size = min(15, len(idxs)), replace = False)
    # initializing the list of faces to include in the montage
    faces = []
    # initializing the list of whole_images to include in the zip files of each faces, to be downloaded by the user
    whole_images = []
    
    if labelID != -1:
      dir_name = 'face#{}'.format(labelID + 1)
      os.mkdir(dir_name)

    for i in idxs:
      current_image = cv2.imread(data_arr[i]["imagePath"])
      rgb_current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
      (top, right, bottom, left) = data_arr[i]["loc"]
      current_face = rgb_current_image[top:bottom, left:right]
      current_face = cv2.resize(current_face, (96, 96))
      whole_images.append(rgb_current_image)
      faces.append(current_face)

      if labelID != -1:
        face_image_name = 'image{}.jpg'.format(i)
        cv2.imwrite(os.path.join(dir_name, face_image_name), current_image)
    
    if labelID != -1:
      shutil.make_archive('zip_face#{}'.format(labelID + 1), 'zip', dir_name)
      # deleting the directory and image files contained in it as we need only the zip file which has been created already
      shutil.rmtree('face#{}'.format(labelID + 1))
      
    montage = build_montages(faces, (96, 96), (2, 2))[0]

    current_title = "Face #{}:".format(labelID + 1)
    expander_caption = "Images with Face #{}:".format(labelID + 1)
    current_title = "Unknown:" if labelID == -1 else current_title

    with cols1[labelID + 1]:
      st.write(current_title)
      st.image(montage)
    if labelID != -1:
      with st.expander(expander_caption):
        # displaying the images of the current face
        cols2 = st.columns(3)
        for j in range(len(whole_images)):
          with cols2[j%3]:
            st.image(whole_images[j], use_column_width = 'always')
        # providing an option for the user to download folders with images of particular faces after clustering as zip files
        with open("zip_face#{}.zip".format(labelID + 1), "rb") as fp:
          btn = st.download_button(
              label="Download ZIP of Clustered Images with Face #{}".format(labelID + 1),
              data=fp,
              file_name="clustered_faces#{}.zip".format(labelID + 1),
              mime="application/zip"
          )
        fp.close()
