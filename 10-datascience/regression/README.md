# Regression

## Sklearn Regression Model

```py
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

regr = MLPRegressor(random_state=1, max_iter=10000, hidden_layer_sizes=(64,32, 16, 8),activation='relu',momentum=0.9).fit(X_train, y_train)

regr.score(X_test, y_test)

mean_squared_error(y_test, regr.predict(X_test), squared=False)

pd.DataFrame(regr.loss_curve_).plot()
```

## Keras Regression Model

```py
import tensorflow as tf
from tensorflow import keras
from keras import backend as K

import os
from keras.models import Sequential
from keras.layers import Dense

%reload_ext tensorboard

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

seed = 1
tf.keras.utils.set_random_seed(
    seed
)
```

```py
# def r_square(y_true, y_pred):
#     SS_res =  K.sum(K.square( y_true-y_pred )) 
#     SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) ) 
#     return ( 1 - SS_res/(SS_tot + K.epsilon()) )

model = Sequential()
model.add(Dense(64, input_dim=3, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(Dense(32, activation='relu'))
model.add(keras.layers.Dropout(0.4))
# model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
opt = tf.keras.optimizers.Adam(learning_rate=0.001)
es_callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, mode='min')
# model.compile(optimizer=opt, loss='mean_squared_error', metrics=['mae', r_square])
model.compile(optimizer=opt, loss='mean_squared_error', metrics=['mae'])

history = model.fit(X_train,
                    y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(X_test, y_test),
                    callbacks=[es_callback])
```

```py
# list all data in history
print(history.history.keys())

# summarize history for mae
plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.title('model Mean Absolute Error (MAE)')
plt.ylabel('MAE')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# # summarize history for R2
# plt.plot(history.history['r_square'])
# plt.plot(history.history['val_r_square'])
# plt.title('model Accuracy (R2)')
# plt.ylabel('R2')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, model.predict(X_test), squared=False)

from sklearn.metrics import r2_score
baseline_model_score = r2_score(y_test, model.predict(X_test))
baseline_model_score
```