from src import DataLoader, PrivacyHandler, BiomedicalFeatureEngineer, SepsisRiskModel

def run_pipeline():
    """
    Orchestrates the Digital Patient Pipeline:
    Ingestion -> Privacy (GDPR) -> Features -> Modeling -> Validation
    """
    print("--- STARTING DIGITAL PATIENT PIPELINE ---\n")

    # 1. Data Ingestion
    loader = DataLoader(num_samples=2000)
    raw_data = loader.load_dummy_data()

    # 2. Privacy & Compliance (GDPR)
    # Removing PII (Patient_ID) and generalizing dates
    privacy = PrivacyHandler()
    anonymized_data = privacy.anonymize_ids(raw_data, id_col='patient_real_id')
    anonymized_data = privacy.suppress_dates(anonymized_data, date_col='admission_date')

    # 3. Biomedical Feature Engineering
    # Adding clinical context (Shock Index, etc.)
    engineer = BiomedicalFeatureEngineer()
    final_dataset = engineer.process(anonymized_data)
    
    # Preview data for debugging
    print(f"\n[Pipeline] Processed Data Preview:\n{final_dataset.head(3)}\n")

    # 4. Simulation & Validation
    # Training the Digital Patient Model
    model = SepsisRiskModel()
    model.train(final_dataset, target_col='target_sepsis')

    print("\n--- PIPELINE COMPLETED SUCCESSFULLY ---")

if __name__ == "__main__":
    run_pipeline()