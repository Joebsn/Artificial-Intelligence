# Splitting Data for Machine Learning Models

Splitting data, an important step in the machine learning workflow, involves dividing a dataset into separate subsets for training, validation and testing so that a model can be trained, tuned and evaluated on appropriate data.

A model should not be evaluated on the same data used for training, as it may perform well simply because it has already seen those examples. Therefore, the data is divided into different subsets:

- Training Set: Used to train the model and learn its parameters.
- Validation (Dev) Set: Used during model development to compare models and tune hyperparameters.
- Test Set: Used only for the final evaluation of the selected model.

## Common Methods

### Train-Test Split

- The dataset is divided into two subsets: a training set for training the model and a test set for evaluating it on unseen data.
- A common split is 70–80% for training and 20–30% for testing, though the ratio depends on the dataset.
- It is useful when a separate validation set is not needed or cross-validation is used for model selection.

### Train-Validation-Test Split

- When hyperparameter tuning or model comparison is required, divide the data into three subsets: training for training, validation for tuning and comparison and test for final evaluation.
- A common split is 80% training, 10% validation and 10% testing, but the proportions can vary. For large datasets, smaller percentages may still provide enough samples.
- For example, a dataset with millions of records may use 98% training, 1% validation and 1% testing. The appropriate split depends on the dataset size and evaluation needs.

### K-fold Cross Validation

- For small datasets, setting aside a validation set can reduce the data available for training. K-fold cross-validation can be used instead.
- The training data is divided into K folds. The model is trained on K−1 folds and validated on the remaining fold, repeating the process K times.
- The validation scores are combined, commonly by taking their average, to estimate model performance.
- A separate test set should still be kept aside for final evaluation.

### Stratified Sampling

- In classification, a random split may produce different class proportions across subsets.
- Stratified splitting preserves approximately the same class proportions in each subset.
- It is especially useful for imbalanced datasets or rare classes.

### Time-based Split

- Random splitting is unsuitable when data order matters, such as in time-series data.
- Using future data for training can lead to unrealistic performance estimates.
- Use chronological or time-aware splitting instead.

### Group-Based Split

- Related observations, such as records from the same patient or customer, should generally stay in the same subset.
- Group-aware splitting prevents related samples from appearing in both training and test sets.
- It provides a more realistic evaluation when the model will encounter new groups.
