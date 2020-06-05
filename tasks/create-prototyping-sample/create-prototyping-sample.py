import datetime as dt
import glob
import os
import shutil
import sys

import numpy as np
from pydicom.filereader import dcmread

# Mutate path if necessary
if os.getenv("ENV") != "laptop":
    sys.path.append("/kaggle/input/melanoma-foo")

import foo


SAMPLE_PROPORTION = 0.01


# Create sample of files to copy to working directory
files = glob.glob("/kaggle/input/siim-isic-melanoma-classification/train/*")
num_sampled = int(SAMPLE_PROPORTION * len(files))
sample = np.random.choice(files, num_sampled)


# Create the directory if necessary
dir_target = "/kaggle/working/prototyping-sample"
if not os.path.exists(dir_target):
    os.mkdir("/kaggle/working/prototyping-sample")

# Delete contents if the directory already exists
existing = glob.glob(os.path.join(dir_target, "*"))
for path in existing:
    os.remove(path)


# Copy files
for src in sample:
    dst = os.path.join(dir_target, src.split("/")[-1])
    shutil.copyfile(src, dst)
