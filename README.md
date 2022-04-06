<h1 align="center"><strong>Any Face Clustering</strong></h1>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Jupyter](https://img.shields.io/badge/jupyter-v5.3+-orange.svg)
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/souvikmajumder26/Any-Face-Clustering.svg)](https://github.com/souvikmajumder26/Any-Face_Clustering/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

----

## Basic Overview[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#basic-overview)
A Face Clustering Engine has been developed utilizing <a href="https://opencv.org/" target="_blank">OpenCV</a>, <a href="https://pypi.org/project/face-recognition/" target="_blank">Face Recognition</a> & <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html" target="_blank">DBSCAN (scikit-learn)</a> python libraries.
The project has been deployed as a <a href="https://streamlit.io/" target="_blank">Streamlit</a> Web App which provides users the facility to upload their own images (or images they want to test with) and be delivered with the images grouped according to the individual unique faces contained in them.

A Face Clustering Engine in essence performs grouping of user-provided images according to the unique faces contained in them. Unsupervised Learning being at the core of this Face Clustering Engine enables it to cluster/group images by faces which it hasn't even seen (trained on) yet. And thus it is applicable to **Any Face**.

----

## Table of contents[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#table-of-contents)
1. [How to interact with the Project as a User](#how-to-interact-with-the-project-as-a-user)
   - [Opening the Project in Google Colab Notebook](#a-follow-these-steps-to-open-the-project-in-google-colab-notebook)
   - [Demo video of the Streamlit Web App](#b-demo-follow-this-video-on-how-to-interact-with-the-streamlit-web-app-after-launching-it-from-google-colab-notebook)
3. [Motivation and Applications](#motivation-and-applications)
4. [Dependencies](#dependencies)
5. [Acknowledgement](#acknowledgement)

----

## How to interact with the Project as a User[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#how-to-interact-with-the-project-as-a-user)

### A. Follow these steps to open the Project in Google Colab Notebook:
- *Open the file **"Any_Face_Clustering_Streamlit_app.ipnyb"** and click **"Open in Colab"*** OR *just click <a href="https://colab.research.google.com/github/souvikmajumder26/Any-Face-Clustering/blob/main/Any_Face_Clustering_Streamlit_app.ipynb">**here**</a>* :D

- > A notebook will open in Google Colab.

- *Follow the **next steps mentioned in the notebook** to launch the **Streamlit Web App**.*


### B. Demo: Follow this video on how to interact with the Streamlit Web App after launching it from Google Colab Notebook:

*Feel free to interact with the Streamlit Web App...*
> ***Upload images of several faces (make sure to upload atleast 3 images containing the same face)... or you can choose to use the <a href="https://drive.google.com/drive/folders/1JXYCf4Qk4fuTfTDoduGU7vgmXNyXSMUe?usp=sharing">Unlabelled_test_images</a> by downloading the folder and then uploading the images to the Web App to experience how the project works.***

https://user-images.githubusercontent.com/86871718/161094650-5aecaa71-a6de-4ae6-85ff-07c0a7d0345b.mp4

----

## Motivation and Applications[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#motivation-and-applications)

Long before I knew anything about Artificial Intelligence, I discovered a feature in my mobile phone which grouped all images according to the faces contained in them. I was always intruiged by this feature and wondered how this had been achieved. After a few years, fortunately I was exposed to the field of Data Science and Artificial Intelligence, and now I have been able to fulfill my old curiosity by building the same feature in the form of a Web App prototype to be used by anyone.

Other than **Web & Mobile application integrations** of this project making lives easier by enabling people to search photos by a particular face, another crucial application area of this project can be **Law Enforcement**. In case of a crime scene, suppose there are active security cameras in the neighbourhood that recorded the people present at the crime scene and in the nearby areas. So, even if the law enforcement/police officers arrive after the criminal(s) has/have fled, this project can help the law enforcement in tracking the routes and activities of the people present there and in the neighbourhood areas by comparing unique faces/identities from several video feeds to check for suspicious activities which will further aid in the investigation.

----

## Dependencies[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#dependencies)

- OpenCV (cv2)
- Face_Recognition

----

## Acknowledgement[![](https://github.com/souvikmajumder26/Any-Face-Clustering/blob/main/docs/img/pushpin.svg)](#motivation-and-applications)
- https://pyimagesearch.com/2018/07/09/face-clustering-with-python/
