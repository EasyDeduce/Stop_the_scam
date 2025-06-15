🚀 Stop The Scam — Fraudulent Job Listing Classifier


An end-to-end machine learning pipeline to detect fraudulent job postings.



📂 Project Structure





Stop_The_Scam/
│
├── data/
│   ├── job_data.csv          # Original dataset
│   └── custom_jobs.csv       # New jobs to predict
│
├── models/
│   ├── final_model.pkl       # Trained XGBoost model
│   ├── vectorizer.pkl        # Saved TFIDF vectorizer
│   └── ohe.pkl               # Saved OneHotEncoder
│
├── src/
│   ├── config.py             # Configurations & hyperparameters
│   ├── data_preprocessing.py # Cleaning raw data
│   ├── feature_engineering.py# Feature extraction pipeline
│   └── model_training.py     # Model training & evaluation functions
│
├── utils/
│   ├── alerting.py           # Email alerts for high-risk jobs
│   └── explainability.py     # SHAP-based explainability
│
├── train_model.py            # Full training pipeline
├── predict_and_alert.py      # Full prediction + explainability + alert pipeline
└── README.md




💡 Features




✅ Full data cleaning & feature engineering




✅ TFIDF + OneHotEncoder based feature extraction




✅ SMOTE oversampling for class imbalance




✅ Trained XGBoost model (90%+ F1-score)




✅ SHAP explainability (where possible)




✅ Email alerts for high-risk jobs (probability > 90%)




✅ Modular code with full separation of training vs inference




✅ Fully scalable & production-ready structure





🔧 Setup Instructions


1️⃣ Clone repository





git clone https://github.com/EasyDeduce/Stop_The_Scam.git
cd Stop_The_Scam



2️⃣ Create virtual environment





python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows



3️⃣ Install dependencies





pip install -r requirements.txt



4️⃣ Add your data




Place your training data inside data/job_data.csv




Place any custom data you want to predict on in data/custom_jobs.csv





🚀 Usage


🔬 Train model (only required once or when retraining):





python train_model.py





This will train the model and save it inside models/




🔮 Predict on new data (and trigger alerts):





python predict_and_alert.py




📧 Email Alert Setup


1️⃣ Enable "App Passwords" for your Gmail account

2️⃣ Replace your credentials inside utils/alerting.py:





sender = 'your_email@gmail.com'
password = 'your_app_password'
receiver = 'receiver_email@gmail.com'




📊 Explainability (SHAP)




SHAP plots will be generated during prediction.




If feature count is too high, plots may be skipped automatically.





🔄 Retraining


Simply run python train_model.py anytime you add new labeled data.



🚧 To Do (Future)




✅ Flask API endpoint for real-time predictions




✅ Automate retraining with cron job




✅ Deployment-ready Docker setup




✅ GitHub Actions CI/CD





🙏 Acknowledgements




Dataset: Kaggle — Fake Job Postings Dataset




Libraries: scikit-learn, xgboost, imbalanced-learn, shap, nltk





🧑‍💻 Author


Saksham Rao
