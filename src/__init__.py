"""
Digital Patient Sentinel Package
--------------------------------
This package contains the modules for data ingestion, privacy protection,
feature engineering, and model training.
"""

# Exposing the main classes to be easily imported from the 'src' package
from .data_loader import DataLoader
from .privacy import PrivacyHandler
from .features import BiomedicalFeatureEngineer
from .model import SepsisRiskModel

# Optional: Define what is exported when someone uses 'from src import *'
__all__ = [
    'DataLoader',
    'PrivacyHandler',
    'BiomedicalFeatureEngineer',
    'SepsisRiskModel'
]