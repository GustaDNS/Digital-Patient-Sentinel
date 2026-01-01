import pandas as pd
import numpy as np

class DataLoader:
    """
    Handles the ingestion and simulation of raw clinical data.
    In a real scenario, this would connect to an SQL database or FHIR API.
    """

    def __init__(self, num_samples: int = 1000):
        """
        Args:
            num_samples (int): Number of synthetic patients to generate.
        """
        self.num_samples = num_samples
        self.random_state = 42

    def load_dummy_data(self) -> pd.DataFrame:
        """
        Generates synthetic Intensive Care Unit (ICU) data.
        
        Returns:
            pd.DataFrame: Raw dataframe containing PII and sensor data.
        """
        np.random.seed(self.random_state)
        
        # Simulating PII (Personally Identifiable Information)
        data = {
            'patient_real_id': [f"PT_{i:05d}" for i in range(self.num_samples)],
            # CORREÇÃO DO AVISO: Mudei 'H' para 'h' (horas)
            'admission_date': pd.date_range(start='2023-01-01', periods=self.num_samples, freq='h'),
            
            # Static Clinical Data
            'age': np.random.randint(18, 95, self.num_samples),
            'gender': np.random.choice(['M', 'F'], self.num_samples),
            
            # Dynamic Sensor Data (Vitals)
            'heart_rate': np.random.normal(85, 15, self.num_samples),  # bpm
            'systolic_bp': np.random.normal(120, 25, self.num_samples), # mmHg
            'diastolic_bp': np.random.normal(80, 15, self.num_samples), # mmHg
            'temperature': np.random.normal(37.0, 0.8, self.num_samples), # Celsius
            'oxygen_sat': np.random.normal(96, 3, self.num_samples),    # %
            'lactate': np.random.exponential(1.5, self.num_samples)     # mmol/L
        }
        
        df = pd.DataFrame(data)
        
        # Generate a synthetic target variable (Sepsis: 0 or 1)
        risk_score = (
            (df['heart_rate'] > 100).astype(int) + 
            (df['systolic_bp'] < 90).astype(int) + 
            (df['lactate'] > 2.0).astype(int)
        )
        df['target_sepsis'] = (risk_score >= 2).astype(int)
        
        print(f"[DataLoader] Loaded {len(df)} raw patient records.")
        
        return df