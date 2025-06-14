# main.py

import sys
sys.path.append('./src')

from config import *
from data_preprocessing import load_and_clean_data
from feature_engineering import FeatureBuilder

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

# Load data
df = load_and_clean_data(DATA_PATH)

# Target and Features
y = df['fraudulent']

# Train-test split
train_df, test_df, y_train, y_test = train_test_split(df, y, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_SEED)

# Build features
builder = FeatureBuilder(TFIDF_MAX_FEATURES, TFIDF_NGRAM_RANGE)
X_train = builder.fit_transform(train_df)
X_test = builder.transform(test_df)

# Apply SMOTE (oversampling only on train data)
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# Train XGBoost
model = XGBClassifier(
    scale_pos_weight=(len(y_train_balanced) - sum(y_train_balanced)) / sum(y_train_balanced),
    n_estimators=600,
    learning_rate=0.07,
    max_depth=6,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_balanced, y_train_balanced)

# Evaluate
y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.4f}")
