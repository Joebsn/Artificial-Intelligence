# %% Import Required Libraries
import math
from sklearn.metrics import mean_squared_error
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def plot_predictions(real_prices, predicted_prices):
    plt.figure(figsize=(16, 6))
    plt.plot(real_prices, color='green', label='Actual Company Stock Price')
    plt.plot(predicted_prices, color='orange',
             label='Predicted Company Stock Price')
    plt.title('Company Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()


def calculate_rmse(real_prices, predicted_prices):
    rmse = math.sqrt(mean_squared_error(real_prices, predicted_prices))
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# %% Load and Visualize Company Stock Dataset
dataset = pd.read_csv("dataset.csv", index_col='Date', parse_dates=['Date'])

training_set = dataset.loc[:'2016', 'High'].values.reshape(-1, 1)
test_set = dataset.loc['2017':, 'High'].values.reshape(-1, 1)

plt.figure(figsize=(16, 4))
plt.plot(dataset.loc[:'2016', 'High'], label='Training Set (Before 2017)')
plt.plot(dataset.loc['2017':, 'High'], label='Test Set (2017 and beyond)')
plt.title('Company Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# %% Apply Feature Scaling
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_training = scaler.fit_transform(training_set)

# %% Prepare Training Sequences
X_train = []
y_train = []

for i in range(60, len(scaled_training)):
    # if i = 80, then X_train will contain scaled_training[20:80] where 80 is excluded
    # and y_train will contain scaled_training[70], meaning that we predict day 80 from days 20:79
    X_train.append(scaled_training[i - 60:i, 0])
    y_train.append(scaled_training[i, 0])

X_train = np.array(X_train)
y_train = np.array(y_train)

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

# %% Build the LSTM Model
lstm_model = Sequential()

lstm_model.add(LSTM(units=50, return_sequences=True,
               input_shape=(X_train.shape[1], 1)))
lstm_model.add(Dropout(0.2))

lstm_model.add(LSTM(units=50, return_sequences=True))
lstm_model.add(Dropout(0.2))

lstm_model.add(LSTM(units=50, return_sequences=True))
lstm_model.add(Dropout(0.2))

lstm_model.add(LSTM(units=50))
lstm_model.add(Dropout(0.2))

lstm_model.add(Dense(units=1))

lstm_model.compile(optimizer='rmsprop', loss='mean_squared_error')

# %% Train the Model
lstm_model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

# %% Prepare Test Data for Prediction
dataset_total = pd.concat((dataset['High'][:'2016'], dataset['High']['2017':]), axis=0)
inputs = dataset_total[len(dataset_total) - len(test_set) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60, len(inputs)):
    X_test.append(inputs[i - 60:i, 0])

X_test = np.array(X_test)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# %% Predict Stock Prices
predicted_prices_scaled = lstm_model.predict(X_test)
predicted_prices = scaler.inverse_transform(predicted_prices_scaled)

# %% Plot Actual vs Predicted Prices
plot_predictions(test_set, predicted_prices)
