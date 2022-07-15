<h1 align="center"><strong>Any Face Clustering:<br>Automatically Group your Images by Faces with<br>an end-to-end Artificial Intelligence App</strong></h1>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Jupyter](https://img.shields.io/badge/jupyter-v5.3+-orange.svg)
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/souvikmajumder26/Any-Face-Clustering.svg)](https://github.com/souvikmajumder26/Any-Face_Clustering/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

----

## Overview[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#basic-overview)
A Face Clustering Engine has been developed utilizing <a href="https://opencv.org/" target="_blank">OpenCV</a>, <a href="https://pypi.org/project/face-recognition/" target="_blank">Face Recognition</a> & <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html" target="_blank">DBSCAN (scikit-learn)</a> python libraries.
The project has been deployed as a <a href="https://streamlit.io/" target="_blank">Streamlit</a> Web App which provides users the facility to upload their own images (or images they want to test with) and be delivered with the images grouped according to the individual unique faces contained in them.

A Face Clustering Engine in essence performs grouping of user-provided images according to the unique faces contained in them. Unsupervised Learning being at the core of this Face Clustering Engine enables it to cluster/group images by faces which it hasn't even seen (trained on) yet. Thus it is applicable to **Any Face**.

----

## Table of Contents[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#table-of-contents)
1. [Usage / User Interaction with the Project (follow any one)](#1-usage--user-interaction-with-the-project-follow-any-one)
   - [Opening the Project in Google Colab Notebook](#a-follow-these-steps-to-open-the-project-in-google-colab-notebook)
   - [Opening the Project Locally](#b-follow-these-steps-to-open-the-project-locally)
2. [Demo video of the Streamlit Web App](#2-demo-follow-this-video-on-how-to-interact-with-the-streamlit-app-after-launching-it)
3. [Motivation and Use Cases](#3-motivation-and-use-cases)
4. [Detailed Project Code with Explanation](#4-detailed-project-code-with-explanation)
5. [Dependencies](#5-dependencies)
6. [Acknowledgement](#6-acknowledgement)

----

## 1. Usage / User Interaction with the Project (follow any one)[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#1-usage--user-interaction-with-the-project-follow-any-one)

>💡 To launch the "Any Face Clustering" Streamlit Web App...

### a) Follow these steps to open the Project in Google Colab Notebook:
- *Open the file **"Any_Face_Clustering_Streamlit_app.ipnyb"** and click **"Open in Colab"*** OR *just click <a href="https://colab.research.google.com/github/souvikmajumder26/Any-Face-Clustering/blob/main/Any_Face_Clustering_Streamlit_app.ipynb">**here**</a>* :D

  >💡 A notebook will open in Google Colab.
  >
  >💡 This app can be deployed directly on cloud for end-users, but as it requires a lot of memory (RAM) for its computation, it could not be deployed successfully to a *free-tier cloud service* (eg: Streamlit Share Cloud, Heroku, AWS, Azure, GCP etc.), thus Google Colab was chosen to work as the free server for this project prototype.

- *Follow the **next steps mentioned inside the notebook** to launch the **Streamlit Web App**.*

### b) Follow these steps to open the Project Locally:
- *Download/clone the repository onto desktop*
- *setup.cfg, setup.py run **python setup.py***
- *Launch the Streamlit Web App by opening the file **"app.py" - streamlit run myfile.py***

----

## 2. [Demo] Follow this video on how to interact with the Streamlit App after launching it:[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#2-Demo-Follow-this-video-on-how-to-interact-with-the-Streamlit-App-after-launching-it)

*Feel free to interact with the Streamlit Web App...*
>💡 ***Upload images of several faces (make sure to upload atleast 3 images containing the same face)... or you can choose to use the <a href="https://drive.google.com/drive/folders/1JXYCf4Qk4fuTfTDoduGU7vgmXNyXSMUe?usp=sharing">Unlabelled_test_images</a> by downloading the folder and then uploading the images to the Web App to experience how the project works.***

https://user-images.githubusercontent.com/86871718/171251974-bd3312c7-b407-4ca6-b4ee-8f59b4b742e4.mp4

----

## 3. Motivation and Use Cases[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#3-motivation-and-use-cases)

- Long before I knew anything about Artificial Intelligence, I discovered a feature in my mobile phone which grouped all images according to the faces contained in them. I was always intruiged by this feature and wondered how this had been achieved. After a few years, fortunately I was exposed to the field of Data Science and Artificial Intelligence, and now I have been able to fulfill my old curiosity by building the same feature in the form of a Web App prototype to be used by anyone.

- Other than **Web & Mobile application integrations** of this project making lives easier by enabling people to search photos by a particular face, another crucial use case of this project can be **Law Enforcement**. In case of a crime scene, suppose there are active security cameras in the neighbourhood that recorded the people present at the crime scene and in the nearby areas. So, even if the law enforcement/police officers arrive after the criminal(s) has/have fled, this can help the law enforcement in tracking the routes and activities of the people present there and in the neighbourhood areas by comparing unique faces/identities from several video feeds to check for suspicious activities which will further aid in the investigation.

----

## 4. Detailed Project Code with Explanation[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#4-detailed-project-code-with-explanation)

- *Open the file **"Detailed_Project_Explanation.ipnyb"** and click **"Open in Colab"*** OR *just click <a href="https://colab.research.google.com/github/souvikmajumder26/Any-Face-Clustering/blob/main/Detailed_Project_Explanation.ipynb">**here**</a>* to open the notebook with detailed and explained project code.

----

## 5. Dependencies[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#5-dependencies)

- OpenCV (cv2)
- Face-Recognition
- scikit-learn
- Numpy
- Streamlit
- imutils
- os
- time
- shutil
- tempfile

----

## 6. Acknowledgement[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#6-acknowledgement)
- https://opencv.org/
- https://face-recognition.readthedocs.io/en/latest/index.html
- https://scikit-learn.org/stable/
- https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
- https://numpy.org/
- https://streamlit.io/
- https://pypi.org/project/imutils/
- https://docs.python.org/3/library/os.html
- https://docs.python.org/3/library/time.html
- https://docs.python.org/3/library/shutil.html
- https://docs.python.org/3/library/tempfile.html
- https://pyimagesearch.com/2018/07/09/face-clustering-with-python/
