import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

class SepsisRiskModel:
    """
    Wraps the Machine Learning logic for Sepsis prediction.
    Focuses on explainability for clinical validation.
    """

    def __init__(self):
        # Using RandomForest for its interpretability (feature importance)
        self.model = RandomForestClassifier(
            n_estimators=100, 
            max_depth=10, 
            random_state=42, 
            class_weight='balanced'
        )
        self.features = []

    def train(self, df: pd.DataFrame, target_col: str):
        """
        Trains the predictive model.
        """
        print(f"[Model] Training Sepsis Risk Model on {len(df)} records...")
        
        # Drop ID and Target for X
        X = df.drop(columns=['anon_id', target_col])
        y = df[target_col]
        
        # Store feature names for later interpretation
        self.features = X.columns.tolist()
        
        # Split data (80% Train, 20% Test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        
        # Evaluate immediately
        self._evaluate(X_test, y_test)

    def _evaluate(self, X_test, y_test):
        """
        Internal method to print clinical validation metrics.
        """
        y_pred = self.model.predict(X_test)
        y_prob = self.model.predict_proba(X_test)[:, 1]
        
        print("\n" + "="*40)
        print("CLINICAL VALIDATION REPORT")
        print("="*40)
        print(classification_report(y_test, y_pred))
        print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
        print("-" * 40)
        
        self._explain_model()

    def _explain_model(self):
        """
        Prints feature importance to support clinical interpretability.
        Crucial for doctors to trust the 'Digital Patient' model.
        """
        print("\n[Explainability] Key Drivers of Risk:")
        importances = self.model.feature_importances_
        indices = importances.argsort()[::-1]

        for i in range(min(5, len(self.features))):
            print(f"{i+1}. {self.features[indices[i]]:<20} (Imp: {importances[indices[i]]:.4f})")