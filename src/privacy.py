import pandas as pd
import hashlib

class PrivacyHandler:
    """
    Responsible for GDPR compliance: Pseudo-anonymization and data minimization.
    """

    @staticmethod
    def anonymize_ids(df: pd.DataFrame, id_col: str) -> pd.DataFrame:
        """
        Replaces raw Patient IDs with a SHA-256 hash.
        
        Args:
            df (pd.DataFrame): The raw dataframe.
            id_col (str): The name of the column containing real IDs.

        Returns:
            pd.DataFrame: Dataframe with anonymized IDs.
        """
        print(f"[PrivacyHandler] Anonymizing column: {id_col}...")
        
        df_clean = df.copy()
        
        # Apply SHA-256 hashing
        df_clean['anon_id'] = df_clean[id_col].apply(
            lambda x: hashlib.sha256(str(x).encode()).hexdigest()[:12]
        )
        
        # Drop the original PII column
        df_clean = df_clean.drop(columns=[id_col])
        
        # Move anon_id to first column for readability
        cols = ['anon_id'] + [c for c in df_clean.columns if c != 'anon_id']
        return df_clean[cols]

    @staticmethod
    def suppress_dates(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
        """
        Generalizes specific dates to Year-Month to prevent re-identification.
        """
        # Ensure it's datetime format before converting
        df[date_col] = pd.to_datetime(df[date_col]).dt.to_period('M')
        return df