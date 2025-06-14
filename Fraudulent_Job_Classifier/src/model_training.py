from xgboost import XGBClassifier
from sklearn.metrics import f1_score

def train_xgb(X_train, y_train):
    model = XGBClassifier(
        scale_pos_weight=(len(y_train)-sum(y_train)) / sum(y_train),  # handle imbalance
        n_estimators=500,
        learning_rate=0.05,
        max_depth=6,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    return model

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    print(f"F1 Score: {f1:.4f}")
    return f1
