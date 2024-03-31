import numpy as np
import pandas as np

import tensorflow_text as text
import tensorflow as tf
import tensorflow_hub as hub

AUTOTUNE = tf.data.AUTOTUNE
# under the hood, measures latency and does some data optimization for parallelism
# Data pipeline consiss of prefetch, batch, map, interleave

batch_size = 32
seed = 42

raw_train_ds = "placeholder"
