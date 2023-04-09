# Model Optimization

## Keras Model Pruning

```py
!pip install -q tensorflow-model-optimization

import tempfile

_, keras_file = tempfile.mkstemp('.h5')
tf.keras.models.save_model(model, keras_file, include_optimizer=True)
print('Saved baseline model to:', keras_file)

# Compute end step to finish pruning after 2 epochs.
batch_size = 32
epochs = 100
validation_split = 0.

num_samples = X_train.shape[0] * (1 - validation_split)
end_step = np.ceil(num_samples / batch_size).astype(np.int32) * epochs
end_step

import tensorflow_model_optimization as tfmot

prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude

# Define model for pruning.
pruning_params = {
      'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.50,
                                                               final_sparsity=0.80,
                                                               begin_step=0,
                                                               end_step=end_step)
}

model_for_pruning = prune_low_magnitude(model, **pruning_params)

opt = tf.keras.optimizers.Adam(learning_rate=0.001)

# `prune_low_magnitude` requires a recompile.
model_for_pruning.compile(optimizer=opt, loss='mean_squared_error', metrics=['mae'])

model_for_pruning.summary()

logdir = tempfile.mkdtemp()

callbacks = [
  tfmot.sparsity.keras.UpdatePruningStep(),
  tfmot.sparsity.keras.PruningSummaries(log_dir=logdir),
  es_callback
]

history_prune = model_for_pruning.fit(X_train, y_train,
                                    batch_size=batch_size, epochs=epochs,
                                    callbacks=callbacks,
                                    validation_data=(X_test, y_test))

model_for_pruning_score = r2_score(y_test, model_for_pruning.predict(X_test))

print('Baseline test score:', baseline_model_score) 
print('Pruned test score:', model_for_pruning_score)

# summarize history for mae
plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.plot(history_prune.history['mae'])
plt.plot(history_prune.history['val_mae'])
plt.title('model Mean Absolute Error (MAE)')
plt.ylabel('MAE')
plt.xlabel('epoch')
plt.legend(['train', 'test', 'pruned train', 'pruned test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.plot(history_prune.history['loss'])
plt.plot(history_prune.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test', 'pruned train', 'pruned test'], loc='upper left')
plt.show()

model_for_export = tfmot.sparsity.keras.strip_pruning(model_for_pruning)

_, pruned_keras_file = tempfile.mkstemp('.h5')
tf.keras.models.save_model(model_for_export, pruned_keras_file, include_optimizer=False)
print('Saved pruned Keras model to:', pruned_keras_file)

converter = tf.lite.TFLiteConverter.from_keras_model(model_for_export)
pruned_tflite_model = converter.convert()

_, pruned_tflite_file = tempfile.mkstemp('.tflite')

with open(pruned_tflite_file, 'wb') as f:
  f.write(pruned_tflite_model)

print('Saved pruned TFLite model to:', pruned_tflite_file)

def get_gzipped_model_size(file):
  # Returns size of gzipped model, in bytes.
  import os
  import zipfile

  _, zipped_file = tempfile.mkstemp('.zip')
  with zipfile.ZipFile(zipped_file, 'w', compression=zipfile.ZIP_DEFLATED) as f:
    f.write(file)

  return os.path.getsize(zipped_file)


print("Size of gzipped baseline Keras model: %.2f bytes" % (get_gzipped_model_size(keras_file)))
print("Size of gzipped pruned Keras model: %.2f bytes" % (get_gzipped_model_size(pruned_keras_file)))
print("Size of gzipped pruned TFlite model: %.2f bytes" % (get_gzipped_model_size(pruned_tflite_file)))
```

## Keras Model Quantization

```py
# applying post-training quantization to the pruned model for additional benefits
converter = tf.lite.TFLiteConverter.from_keras_model(model_for_export)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_and_pruned_tflite_model = converter.convert()

_, quantized_and_pruned_tflite_file = tempfile.mkstemp('.tflite')

with open(quantized_and_pruned_tflite_file, 'wb') as f:
  f.write(quantized_and_pruned_tflite_model)

print('Saved quantized and pruned TFLite model to:', quantized_and_pruned_tflite_file)

print("Size of gzipped baseline Keras model: %.2f bytes" % (get_gzipped_model_size(keras_file)))
print("Size of gzipped pruned and quantized TFlite model: %.2f bytes" % (get_gzipped_model_size(quantized_and_pruned_tflite_file)))
```