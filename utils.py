import pandas as pd
import numpy as np

def generate_sample_data():
    dates = pd.date_range(start='2025-01-01', periods=100, freq='D')
    n = len(dates)
    data = {
        'Date': dates,
        'Raw_Material_Input_kg': np.random.normal(10000, 500, n),
        'Batch_Weight_kg': np.random.normal(9500, 480, n),
        'Electricity_Consumed_kWh': np.random.normal(3000, 120, n),
        'Heat_Loss_kWh': np.random.normal(150, 20, n),
        'Resistance_Loss_kWh': np.random.normal(80, 10, n),
        'Furnace_Temperature_C': np.random.normal(1850, 30, n),
        'Furnace_Efficiency_%': np.random.normal(88, 2, n),
        'Electrode_Wear_mm': np.random.normal(5, 0.3, n),
        'Metal_Produced_kg': np.random.normal(9000, 450, n),
        'Slag_Produced_kg': np.random.normal(500, 30, n),
        'Conveyor_Energy_kWh': np.random.normal(50, 5, n),
        'Utility_Energy_kWh': np.random.normal(200, 10, n),
        'Batch_Mix_Ratio': np.random.normal(0.97, 0.01, n),
        'Yield_%': np.random.normal(92, 2, n),
        'GHG_Emissions_tCO2e': np.random.normal(110, 5, n),
        'Cost_USD': np.random.normal(20000, 1000, n),
        'Anomaly_Flag': np.random.choice([0, 1], n, p=[0.95, 0.05])
    }
    return pd.DataFrame(data)
