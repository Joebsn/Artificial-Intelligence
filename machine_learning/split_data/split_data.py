# %% Imports
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

X, y = load_iris(return_X_y=True)

# %% Train Test Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, # Split data into training and test sets
    test_size=0.2, # reserves 20% of the data for testing
    random_state=42, # makes the random split reproducible.
    stratify=y # preserves the class distribution between the training and test sets
)

print("Training samples:", len(X_train))
print("Test samples:", len(X_test))
print("Training distribution:", np.bincount(y_train))
print("Testing distribution:", np.bincount(y_test))

# %% Training, Validation & Test Sets
# First split: 80% training, 20% temporary data
X_train, X_temp, y_train, y_temp = train_test_split(X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Second split: divide the remaining 20% equally
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp,
    test_size=0.5,
    random_state=42,
    stratify=y_temp
)

print("Training:", len(X_train))
print("Validation:", len(X_val))
print("Testing:", len(X_test))

# %%
