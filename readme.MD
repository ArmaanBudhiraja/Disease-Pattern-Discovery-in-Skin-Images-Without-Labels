# Disease Pattern Discovery in Skin Images Without Labels

A machine learning and computer vision system for discovering dermatological disease patterns in skin images **without relying on annotated datasets or deep learning models**.

This project uses **classical image processing techniques, feature extraction, and machine learning** to analyze skin lesions, identify patterns, and retrieve visually similar cases from a dataset.

---

# Overview

Skin disease detection often requires **large labeled datasets and deep neural networks**, which are expensive and time-consuming to create.

This project explores an **alternative approach** by using:

- Color analysis
- Texture analysis
- Structural pattern extraction

to detect and classify dermatological patterns **without needing labeled training data for segmentation or deep learning models**.

The system also provides **visual explainability and case-based retrieval** to help understand predictions.

---

# Key Features

- Image preprocessing and enhancement  
- Lesion segmentation using color space analysis  
- Feature extraction using:

  - Color Histogram  
  - GLCM Texture Features  
  - Local Binary Patterns (LBP)

- Machine learning classification using **Support Vector Machine (SVM)**
- Explainability using **heatmap visualization**
- Case-based retrieval of similar images from the dataset
- Interactive **web interface for uploading and analyzing images**

---

# System Architecture

``` bash

User Upload Image
↓
Image Preprocessing
↓
Lesion Segmentation
↓
Feature Extraction
(Color + Texture + Structure)
↓
Feature Scaling
↓
SVM Classification
↓
Explainability Heatmap
↓
Similar Image Retrieval
↓
Results Displayed in Web Interface
```

---

# Tech Stack

### Frontend
- React
- Vite
- TailwindCSS
- ShadCN UI

### Backend
- FastAPI

### Machine Learning / Image Processing
- OpenCV
- NumPy
- Scikit-Learn
- Scikit-Image

### Deployment
- Vercel (Frontend)
- Render (Backend)

---

# Project Structure

``` bash
Disease-Pattern-Discovery-in-Skin-Images-Without-Labels

backend
│
├── main.py
├── predict.py
├── preprocessing.py
├── segmentation.py
├── feature_extraction.py
├── explainability.py
├── retrieval.py
├── train_model.py
├── visualization.py
│
├── model.pkl
├── scaler.pkl
├── feature_database.pkl
└── image_paths.pkl


frontend
│
├── index.html
├── package.json
├── vite.config.ts
│
└── src
    ├── pages
    │   └── Index.tsx
    ├── components
    ├── hooks
    └── lib
    └── main.tsx
    └── App.tsx
    └── index.css

dataset
│
├──train
    └── Actinic keratosis
    └── Atopic Dermatitis 
    └── Benign keratosis 
    └── Dermatofibroma 
    └── Melanocytic nevus 
    └── Melanoma 
    └── Squamous cell carcinoma 
    └── Tinea Ringworm Candidiasis 
    └── Vascular lesion
└──val
    └── Actinic keratosis
    └── Atopic Dermatitis 
    └── Benign keratosis 
    └── Dermatofibroma 
    └── Melanocytic nevus 
    └── Melanoma 
    └── Squamous cell carcinoma 
    └── Tinea Ringworm Candidiasis 
    └── Vascular lesion
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/ArmaanBudhiraja/Disease-Pattern-Discovery-in-Skin-Images-Without-Labels.git
cd disease-pattern-discovery
```

---

## Backend Setup

Navigate to backend folder:
``` bash
cd backend
```
Install dependencies:
``` bash
pip install -r requirements.txt
```
Run the backend server:
``` bash
uvicorn backend.main:app --reload
```
Backend will run at:
``` bash
http://127.0.0.1:8000
```
API documentation:
``` bash
http://127.0.0.1:8000/docs
```