# Standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# We do this to ignore several specific warnings
import warnings
warnings.filterwarnings("ignore")

sns.set()

# Load the Iris Data
iris = pd.read_csv("Iris.csv")
iris.info()

# Examine several random rows
iris.sample(5)

# # Examine grouped data
iris.groupby('Species').count()

# Get descriptive statistics
iris.describe()