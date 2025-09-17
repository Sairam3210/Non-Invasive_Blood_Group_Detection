
## Non-Invasive_Blood_Group_Detection

This research represents a major advancement in integrating biometric data with healthcare technologies, paving the way for future innovations in the field by using Deep Learning Model.

## Table of Contents

- [Introduction](#introduction)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Working Principle](#working-principle)
- [Modules](#modules)
- [Trained Results](#trained-results)
- [Outputs](#outputs)
- [Testing Results](#testing-results)
- [Contributing](#contributing)


## Introduction

# Fingerprint-Based Blood Group Detection

This project aims to detect blood groups (A, B, AB, O) using a non-invasive approach by analyzing fingerprints. The system is designed to provide a quick and simple way to determine blood type without the need for a traditional blood test.

#### Project Architecture
<img width="644" height="299" alt="image" src="https://github.com/user-attachments/assets/bbd34fde-73b7-4a99-a54b-dcb387492421" />

## Folder Structure

<img width="383" height="623" alt="image" src="https://github.com/user-attachments/assets/992e2cb2-dac2-497c-bd4d-99504ee20732" />


## Prerequisites

#### Python 3.x ( Python Flask )

### The following Python libraries:

#### tensorflow
 
 #### keras
	
 #### scikit-learn
  
 #### numpy
	
 #### pandas

 #### opencv-python

#### pillow

#### testing Tool - Post man API

## Getting Started


```bash
# Clone the repository

git clone [https://github.com/Your_Username/Non-Invasive_Blood_Group_Detectio.git]

# Navigate to the project directory

cd Non-Invasive_Blood_Group_Detection

# Install the required dependencies

pip install -r requirements.txt  

```

## Dataset

The model was trained on a comprehensive dataset of fingerprint images, carefully organized by blood group type. The folder structure within Dataset_blood_group/ demonstrates how the data is categorized for training the deep learning model.

#### Dataset Classification

The bar graph titled "Dataset Class Distribution" illustrates the number of samples belonging to each blood group in the dataset used for training and evaluation.

![classdistribution](https://github.com/user-attachments/assets/5f33e7b9-c515-4e14-b2ca-5bbba356d202)


#### Download the dataset:

The dataset is included in the repository due to size constraints.

## Working Principle

-Image Acquisition: A high-resolution image of the user's fingerprint is captured.

-Image Pre-processing: The captured image is pre-processed to enhance the ridges and valleys and remove noise.

-Feature Extraction: Key features such as ridge endings, bifurcations, and minutiae points are extracted.

-Pattern Recognition: A Convolutional Neural Network (CNN) model analyzes the extracted features to identify patterns.

-Classification: The CNN model classifies the pattern into one of the four blood groups (A, B, AB, O).

-Prediction: The system provides a final prediction of the user's blood group.

## Frontend & User Interface
The web-based user interface allows users to upload a fingerprint image and receive an instant prediction of their blood group. The frontend is built with standard web technologies (HTML, CSS, JavaScript) and is powered by the backend application.

#### Home page
<img width="602" height="468" alt="image" src="https://github.com/user-attachments/assets/f4b24ad2-54d8-4420-a613-1b056bd532a7" />

#### signup page
<img width="655" height="408" alt="image" src="https://github.com/user-attachments/assets/e610940b-2a8e-4c45-9455-212aba0009bf" />

#### Login page
<img width="602" height="353" alt="image" src="https://github.com/user-attachments/assets/b0c10b5e-813b-4c8b-9f96-02b05fbe9625" />

#### predict page
<img width="666" height="366" alt="image" src="https://github.com/user-attachments/assets/40a9ca49-86c1-4e6b-a0d3-1c3a0d1a1924" />

 ## Modules

A Jupyter Notebook ```bash( .ipynb ) ``` that contains code for Training and Testing.
 
The main modules in this CNN architecture are the Input Layer, Convolutional Layers, Max-Pooling Layers, Hidden (Fully Connected) Layers, and the Output Layer. Each module performs a specific function to process the input image and produce a final prediction.

1. Input Layer
This is the starting point of the network. It receives the raw data, which in this case is an image. The dimensions shown, 125x125x3, represent the width, height, and color channels (Red, Green, Blue) of the input image, respectively.

2. Convolutional Layers
These layers are the core of the CNN. They use small filters (or kernels) to scan the input image and detect specific features like edges, textures, or shapes. Each convolutional layer in your diagram creates a series of feature maps (e.g., 32, 64, 64, 16) that highlight the presence of these features.

3. Max-Pooling Layers
These layers work in tandem with the convolutional layers. They perform a down-sampling operation by taking the maximum value from a small region of the feature maps. This reduces the spatial dimensions of the data (e.g., from 62x62 to 31x31), which helps to: Reduce the computational complexity and Make the model more robust to minor shifts and distortions in the input image.

4. Fully Connected (Hidden) Layers
After the convolutional and max-pooling layers have extracted high-level features, the data is flattened into a single, long vector. This vector is then fed into these layers. The fully connected layers act as a traditional neural network, using the features to learn complex relationships and prepare for final classification.

## Trained Results


#### Classification Report
This report provides a detailed breakdown of key performance metrics like precision, recall, and f1-score for each blood group.

<img width="625" height="388" alt="image" src="https://github.com/user-attachments/assets/5c91c13f-091e-4b45-9564-5d65697beed7" />

 #### Model Accuracy Graph
This graph shows the model's accuracy increasing with each training epoch, demonstrating that it is effectively learning from the data without significant overfitting.

<img width="630" height="418" alt="image" src="https://github.com/user-attachments/assets/58f3ef1f-a1a4-49bc-b982-f8432f78e4db" />

#### Confusion Matrix
The confusion matrix visually represents the model's performance on each blood group, showing how many predictions were correct versus incorrect.

<img width="602" height="509" alt="image" src="https://github.com/user-attachments/assets/abf7499a-4716-4526-9bba-dd81d3cae707" />


## Outputs

A live demonstration of the system's functionality is available in the images.

<img width="620" height="327" alt="image" src="https://github.com/user-attachments/assets/5c6fcd9d-2da8-4705-ac62-a66249552f2f" />

<img width="629" height="314" alt="image" src="https://github.com/user-attachments/assets/e6ab48e8-ae25-4c44-aa87-c3c8b5377d1e" />

## Testing Results

#### API Endpoint Testing
The Postman API was used to test the http://127.0.0.1:5000/predict endpoint. We sent a POST request with a fingerprint image, and the API successfully responded with the predicted blood group and a confidence score. This demonstrates that our API can correctly process image data and return a prediction.

<img width="1131" height="614" alt="image" src="https://github.com/user-attachments/assets/2620e0d7-e533-4914-bd89-7d9e62c423bb" />




## Contributing

We welcome contributions from the community. If you would like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature (git checkout -b feature/your-feature-name).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Create a pull request.

