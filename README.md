# 🛡️ Network Security Threat Detection using Machine Learning

A robust and production-ready machine learning pipeline designed to detect **phishing threats in network environments**. This project leverages a modular architecture with comprehensive logging, experiment tracking using MLflow, and collaboration/version control via DagsHub. It covers the full ML lifecycle including data ingestion, validation, transformation, model training, and evaluation.

---

## 🚀 Project Highlights

- ✅ **Automated ML Pipeline**: Ingestion → Validation → Transformation → Training
- 📦 **End-to-End Logging**: Captures every stage of pipeline execution
- 📈 **High Performance**:  
  - **Train F1 Score**: `0.9909`  
  - **Test F1 Score**: `0.9747`
- 📊 **MLflow + DagsHub**: Integrated experiment tracking & collaboration
- 🧪 **Reproducible Artifacts**: All inputs/outputs are tracked and versioned
- 🐳 **Containerized**: Dockerized for reproducibility and deployment

---

## 📂 Project Structure

```plaintext
├── .github/workflows/main.yaml         # CI/CD GitHub Actions Workflow
├── Artifacts/                          # Generated pipeline artifacts
├── data_schema/schema.yaml             # Data schema for validation
├── final_model/                        # Trained model outputs
├── Logs/                               # Runtime logs
├── mlruns/                             # MLflow experiment tracking data
├── Network_Data/phisingData.csv        # Raw dataset
├── Networksecurity/                    # Core pipeline package
│   ├── cloud/s3_syncer.py              # AWS S3 sync script
│   ├── components/                     # Ingestion, validation, transformation, training
│   ├── constants/                      # Static pipeline configurations
│   ├── entity/                         # Data & artifact entities
│   ├── exception/                      # Custom exception handling
│   ├── logging/                        # Logging configurations
│   ├── pipeline/                       # Batch prediction & training scripts
│   └── utils/                          # Utility functions (general + ML-specific)
├── Templates/table.html                # UI template
├── valid_data/test.csv                 # Cleaned test data
├── .env                                # Environment variables
├── .gitignore
├── app.py                              # App script (API / Streamlit)
├── Dockerfile                          # Docker container definition
├── Main.py                             # Entry point for training
├── push_data.py                        # Data push script
├── README.md
├── requirements.txt                    # Python dependencies
└── setup.py                            # Installation script
```

---

### ✅ Model Performance Summary

Metric	          Training Set	        Test Set
F1 Score	        0.9909	             0.9747
Precision	        0.9896	             0.9728
Recall	            0.9922	             0.9767

> 🔍 Model shows excellent generalization and robustness with very minor performance drop between train and test datasets.

---

### ⚙️ Key Technologies Used

Category	                Tools & Technologies

Programming Language	        Python 3.10
ML Libraries	                scikit-learn, pandas, NumPy
Imputation Technique	        KNNImputer (n_neighbors=3)
Model Tracking	                MLflow (integrated with DagsHub)
Cloud Storage	                AWS S3 (via s3_syncer.py)
Logging	                        Python logging module with centralized custom logs
Containerization	            Docker
CI/CD	                        GitHub Actions (.github/workflows/main.yaml)
Web API / UI	                FastAPI or Streamlit (app.py)
Project Structure	            Modular Python package with reusable components

---

### 🔁 Training & Evaluation Pipeline

Pipeline Stage	                Description

1. Data Ingestion	            Loads raw dataset, splits into train/test, and saves to artifact directory.

2. Validation	                Validates schema and column consistency (handles mismatches gracefully).

3. Transformation	            Applies KNNImputer, feature engineering, and serializes transformers.

4. Model Training	            Trains classification model using scikit-learn.

5. Evaluation	                Calculates metrics (F1, precision, recall) on both train and test datasets.

6. Artifact                     Logging	Stores model, transformer, and metric artifacts with time-stamped paths.

7. Experiment Tracking	        Logs everything to MLflow and DagsHub for versioning and comparison.

---

### 🧪 How to Reproduce

1. Install Dependencies
    ```pip install -r requirements.txt```

2. Run Training Pipeline
    ```python Main.py```

3. Launch API / Web App
    ```python app.py```
