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
item_sales_data = pd.read_csv("Item_wise_sales_history.csv")


# Examine several random rows
g = sns.pairplot(item_sales_data, hue="Customer")
