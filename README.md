# Parkinson-s-Disease-Classification-using-SVM
# Overview
This project implements a Support Vector Machine (SVM) model to classify individuals as Healthy or Parkinson’s patients based on biomedical voice measurements. The dataset is sourced from Kaggle and includes multiple acoustic features extracted from voice recordings.

# Dataset
* Source: Parkinson's Disease Dataset on Kaggle
* Filename: parkinsons.data
* Attributes:
  * name: Unique identifier for each patient
  * status: (Target Variable)
      * 1 → Parkinson’s Disease
      * 0 → Healthy
* Other Features: Various voice-based metrics such as jitter, shimmer, and fundamental frequency.

# Installation & Setup
# 1. Clone the Repository
```bash
   git clone https://github.com/your-username/parkinsons-svm-classifier.git
cd parkinsons-svm-classifier
```
# 2. Install Dependencies
```bash
  pip install numpy pandas scikit-learn matplotlib seaborn kaggle
```
# Evaluation Metrics
* Accuracy Score: Measures overall classification correctness.
* Confusion Matrix: Shows the number of correct and incorrect predictions.
* Classification Report: Provides precision, recall, and F1-score.

# ✅ Expected Model Performance:

* Accuracy: ~85-90%
* Precision & Recall: Depend on feature scaling and hyperparameter tuning.

# Results
* The SVM model effectively classifies Parkinson’s patients.
* Feature scaling improves performance.
* Adding non-linear kernels (RBF, polynomial) might further enhance accuracy.

