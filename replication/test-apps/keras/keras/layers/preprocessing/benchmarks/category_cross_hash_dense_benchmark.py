# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Benchmark for KPL implementation of categorical cross hash columns with dense inputs."""

import tensorflow.compat.v2 as tf

import keras
from tensorflow.python.eager.def_function import function as tf_function
from keras.layers.preprocessing import category_crossing
from keras.layers.preprocessing import hashing
from keras.layers.preprocessing.benchmarks import feature_column_benchmark as fc_bm

# This is required as of 3/2021 because otherwise we drop into graph mode.
tf.compat.v1.enable_v2_behavior()

NUM_REPEATS = 10
BATCH_SIZES = [32, 256]


def embedding_varlen(batch_size, max_length):
  """Benchmark a variable-length embedding."""
  # Data and constants.

  num_buckets = 10000
  vocab = fc_bm.create_vocabulary(32768)
  data_a = fc_bm.create_string_data(
      max_length, batch_size * NUM_REPEATS, vocab, pct_oov=0.0)
  data_b = fc_bm.create_string_data(
      max_length, batch_size * NUM_REPEATS, vocab, pct_oov=0.0)

  # Keras implementation
  input_1 = keras.Input(shape=(None,), name="data_a", dtype=tf.string)
  input_2 = keras.Input(shape=(None,), name="data_b", dtype=tf.string)
  crossed_data = category_crossing.CategoryCrossing()([input_1, input_2])
  hashed_data = hashing.Hashing(num_buckets)(crossed_data)
  model = keras.Model([input_1, input_2], hashed_data)

  # FC implementation
  fc = tf.feature_column.crossed_column(["data_a", "data_b"], num_buckets)

  # Wrap the FC implementation in a tf.function for a fair comparison
  @tf_function()
  def fc_fn(tensors):
    fc.transform_feature(tf.__internal__.feature_column.FeatureTransformationCache(tensors), None)

  # Benchmark runs
  keras_data = {
      "data_a":
          data_a.to_tensor(default_value="", shape=(batch_size, max_length)),
      "data_b":
          data_b.to_tensor(default_value="", shape=(batch_size, max_length)),
  }
  k_avg_time = fc_bm.run_keras(keras_data, model, batch_size, NUM_REPEATS)

  fc_data = {
      "data_a":
          data_a.to_tensor(default_value="", shape=(batch_size, max_length)),
      "data_b":
          data_b.to_tensor(default_value="", shape=(batch_size, max_length)),
  }
  fc_avg_time = fc_bm.run_fc(fc_data, fc_fn, batch_size, NUM_REPEATS)

  return k_avg_time, fc_avg_time


class BenchmarkLayer(fc_bm.LayerBenchmark):
  """Benchmark the layer forward pass."""

  def benchmark_layer(self):
    for batch in BATCH_SIZES:
      name = "cross_hash|dense|batch_%s" % batch
      k_time, f_time = embedding_varlen(batch_size=batch, max_length=256)
      self.report(name, k_time, f_time, NUM_REPEATS)


if __name__ == "__main__":
  tf.test.main()
