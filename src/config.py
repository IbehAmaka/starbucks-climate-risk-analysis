# src/config.py

from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS = PROJECT_ROOT / "outputs"

# Analysis parameters
CONFIG = {
    'scenarios': ['ssp126', 'ssp245', 'ssp585'],
    'scenario_names': {
        'ssp126': 'Net Zero 2050',
        'ssp245': 'Delayed Transition',
        'ssp585': 'Current Policies'
    },
    'variables': ['tas', 'tasmax', 'tasmin', 'pr', 'hurs'],
    'time_periods': {
        'baseline': (1985, 2014),
        'near_term': (2021, 2040),
        'mid_term': (2041, 2060)
    },
    'coffee_optimal': {
        'temp_min': 15,
        'temp_max': 24,
        'temp_optimal': 19.5,
        'precip_min': 1200,
        'precip_max': 2000,
        'precip_optimal': 1600
    },
    'financial_params': {
        'discount_rate': 0.08,
        'starbucks_annual_coffee_mt': 172000,
        'total_assets': 35e9,
        'total_revenue': 36.2e9,
        'price_elasticity': -0.8
    }
}