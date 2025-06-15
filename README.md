🚫 Stop The Scam: Fraudulent Job Listing Classifier


A complete end-to-end machine learning pipeline to detect fraudulent job postings.

Built using XGBoost, TF-IDF NLP, SHAP Explainability, and Email Alerting.



📦 Features




Text preprocessing and feature engineering (TF-IDF + categorical encoding)




XGBoost classifier with class imbalance handling




SMOTE oversampling for better fraud detection




SHAP interpretability for model explainability




Email alerts for high-risk job listings




Modular code structure for training, prediction, and deployment




Easily deployable via Render, Hugging Face, or any cloud platform





🗂️ Project Structure





fraudulent_job_classifier/

│

├── data/                # Raw & cleaned datasets

├── models/              # Saved models (XGBoost, vectorizers, encoders)

├── src/                 # Source code

│   ├── config.py        # Configurations

│   ├── data_preprocessing.py

│   ├── feature_engineering.py

│   ├── model_training.py

│   ├── prediction_pipeline.py

│   └── utils/

│       ├── shap_explainer.py

│       └── alerting.py

│

├── train.py             # One-time training script

├── predict.py           # Prediction & inference pipeline

├── requirements.txt

└── README.md




⚙️ Setup Instructions


1️⃣ Clone Repository





git clone https://github.com/EasyDeduce/stop-the-scam.git
cd stop-the-scam



2️⃣ Create Virtual Environment





python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows



3️⃣ Install Dependencies





pip install -r requirements.txt




📊 Model Training


Only required for initial model building or retraining.





python train.py





Model artifacts (XGBoost model, vectorizer, encoder) will be saved to models/.





🔎 Model Prediction


Perform prediction and trigger alerts on new data:





python predict.py





Make sure predict.py points to your new dataset path.




SHAP plots and email alerts will trigger automatically.





📧 Email Alert Configuration




Update your credentials in src/utils/alerting.py:







sender = 'youremail@gmail.com'
password = 'your_app_password'
receiver = 'destination_email@gmail.com'





For Gmail:

Enable App Passwords under Google Account > Security.





🌐 Deployment Options


PlatformSMTP SupportNotesRender✅Recommended for full functionalityHugging Face Spaces❌SMTP blockedLocal✅Fully supported


🔥 Tech Stack




Python 3.11




scikit-learn




XGBoost




imbalanced-learn




SHAP




Gradio (for web UI)




smtplib (for email)





🏷️ To Do (Optional Future Improvements)




✅ SHAP Explainability




✅ Real-time Email Alerts




✅ API Endpoint Deployment (Gradio/Flask)




✅ Retraining Automation




⬜ Dockerize for portable deployment




⬜ CI/CD pipeline for automatic updates





🙏 Acknowledgments




Dataset: Kaggle Job Fraud Dataset




Developed by: YourNameHere

