# dataset/generate_dataset.py
import pandas as pd
import numpy as np

# Define material properties
data = {
    "material_id": range(1, 101),
    "material_name": [f"Material_{i}" for i in range(1, 101)],
    "strength": np.random.randint(100, 1000, 100),
    "durability": np.random.uniform(1, 10, 100),
    "toughness": np.random.uniform(1, 10, 100),
    "hardness": np.random.randint(1, 10, 100),
    "elasticity": np.random.uniform(0.1, 1.0, 100),
    "plasticity": np.random.uniform(0.1, 1.0, 100),
    "density": np.random.randint(500, 5000, 100),
    "thermal_conductivity": np.random.uniform(0.1, 5.0, 100),
    "porosity": np.random.uniform(0, 50, 100),
    "permeability": np.random.uniform(0.1, 5.0, 100),
    "fire_resistance": np.random.randint(1, 10, 100),
    "weather_resistance": np.random.randint(1, 10, 100),
    "corrosion_resistance": np.random.uniform(0.1, 1.0, 100),
    "chemical_stability": np.random.uniform(0.1, 1.0, 100),
    "reactivity": np.random.uniform(0.1, 1.0, 100),
    "cost": np.random.randint(100, 10000, 100),
    "availability": np.random.randint(1, 10, 100),
    "maintenance": np.random.randint(1, 10, 100),
    "lifecycle_cost": np.random.randint(1000, 50000, 100),
    "recyclability": np.random.uniform(0, 1, 100),
    "energy_efficiency": np.random.uniform(0, 1, 100),
    "carbon_footprint": np.random.uniform(0, 100, 100),
    "ease_of_handling": np.random.randint(1, 10, 100),
    "compatibility": np.random.randint(1, 10, 100),
    "curing_time": np.random.randint(1, 30, 100),
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("../dataset/materials.csv", index=False)
print("Dataset generated and saved as materials.csv")
