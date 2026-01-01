import pandas as pd

class BiomedicalFeatureEngineer:
    """
    Transforms raw sensor data into clinically relevant features.
    This demonstrates domain knowledge integration.
    """

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies feature engineering logic.
        
        Args:
            df (pd.DataFrame): Anonymized dataframe.
            
        Returns:
            pd.DataFrame: Dataframe with added clinical features.
        """
        print("[FeatureEngineer] Generating clinical biomarkers...")
        df_eng = df.copy()
        

        # 1. ML models don't read text. We need to convert Gender M/F to 0/1.
        if 'gender' in df_eng.columns:
            df_eng['gender'] = df_eng['gender'].map({'M': 0, 'F': 1})

        # 2. Shock Index (SI)
        # Formula: Heart Rate / Systolic BP. 
        # Clinical Context: SI > 0.9 suggests hemodynamic instability.
        df_eng['shock_index'] = df_eng['heart_rate'] / df_eng['systolic_bp']
        
        # 3. Pulse Pressure
        # Formula: Systolic - Diastolic.
        # Clinical Context: Low pulse pressure can indicate heart failure.
        df_eng['pulse_pressure'] = df_eng['systolic_bp'] - df_eng['diastolic_bp']
        
        # 4. Hypoxia Flag (Sensor Alert)
        df_eng['alert_hypoxia'] = (df_eng['oxygen_sat'] < 92).astype(int)
        
        # 5. Fever Flag
        df_eng['alert_fever'] = (df_eng['temperature'] > 38.0).astype(int)
        

        cols_to_drop = ['admission_date']
        for col in cols_to_drop:
            if col in df_eng.columns:
                df_eng = df_eng.drop(columns=[col])
            
        return df_eng