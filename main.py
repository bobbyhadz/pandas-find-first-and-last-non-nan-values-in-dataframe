# Pandas: Find first and last non-NaN values in a DataFrame

import pandas as pd
import numpy as np


df = pd.DataFrame({
    'A': [np.nan, 'Bobby', 'Carl', np.nan],
    'B': [np.nan, 20, np.nan, 50],
    'C': [np.nan, np.nan, 30, np.nan],
})

print(df)

print('-' * 50)

first_non_nan = df.apply(pd.Series.first_valid_index)
print(first_non_nan)

print('-' * 50)

last_non_nan = df.apply(pd.Series.last_valid_index)
print(last_non_nan)