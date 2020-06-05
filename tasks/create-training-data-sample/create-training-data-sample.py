import os
import sys

import dask

# Mutate path if necessary
if os.getenv("ENV") != "laptop":
    sys.path.append("/kaggle/input/melanoma-foo")

import foo
