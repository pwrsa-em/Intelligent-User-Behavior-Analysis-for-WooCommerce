import joblib
import os
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from config.settings import MODEL_PATH
from services.data_preprocessing import DataPreprocessor
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MLModelAdvanced:
    def __init__(self, model_path=MODEL_PATH):
        self.model_path = model_path
        self.data_preprocessor = DataPreprocessor()
        self.model = None

    def load_and_prepare_data(self, target_column='purchase_count'):
        processed_data = self.data_preprocessor.preprocess_all()
        features_df = processed_data['features']

        X = features_df.drop(columns=['product_id'])
        y = features_df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        return X_train, X_test, y_train, y_test

    def train_models(self, X_train, y_train):
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
        lr = LogisticRegression(max_iter=500)

        # Voting ensemble
        ensemble = VotingClassifier(estimators=[
            ('rf', rf), ('gb', gb), ('lr', lr)
        ], voting='soft')

        self.model = ensemble
        self.model.fit(X_train, y_train)
        logging.info("Training completed")

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        y_proba = self.model.predict_proba(X_test)[:,1] if hasattr(self.model, 'predict_proba') else None

        acc = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_proba) if y_proba is not None else None

        logging.info(f"Accuracy: {acc:.4f}")
        if roc_auc: logging.info(f"ROC-AUC: {roc_auc:.4f}")
        logging.info("Confusion Matrix:\n" + str(confusion_matrix(y_test, y_pred)))
        logging.info("Classification Report:\n" + classification_report(y_test, y_pred))
        return acc, roc_auc

    def cross_validate(self, X, y, cv=5):
        scores = cross_val_score(self.model, X, y, cv=cv)
        logging.info(f"Cross-validation scores: {scores}")
        logging.info(f"Mean CV score: {scores.mean():.4f}")
        return scores

    def save_model(self, versioned=True):
        path = self.model_path
        if versioned:
            base, ext = os.path.splitext(self.model_path)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            path = f"{base}_{timestamp}{ext}"
        joblib.dump(self.model, path)
        logging.info(f"Model saved to {path}")

    def load_model(self, path=None):
        path = path or self.model_path
        self.model = joblib.load(path)
        logging.info(f"Model loaded from {path}")

    def predict(self, features_df):
        X = features_df.drop(columns=['product_id'])
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)[:,1] if hasattr(self.model, 'predict_proba') else None
        return predictions, probabilities

    def recommend_discounts(self, features_df, threshold=0.5, max_discount=20):
        predictions, probabilities = self.predict(features_df)
        recommendations = []
        for idx, pred in enumerate(predictions):
            prob = probabilities[idx] if probabilities is not None else pred
            if prob >= threshold:
                discount = max_discount * (1 - prob)  # dynamic discount
                recommendations.append({
                    'product_id': features_df.iloc[idx]['product_id'],
                    'recommended_discount': round(discount, 2)
                })
        return recommendations