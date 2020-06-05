#!/bin/bash

export ENV="laptop"

# TODO: Factor out into a separate step
kaggle d version -m hi -p /app/lib -d

# TODO: Programmatically wait for upload completion
echo "sleeping 5s to allow dataset upload to complete"
sleep 5s

kaggle kernels push -p /app/tasks/$TASK_NAME
python3 poll.py --task_name melanoma-$TASK_NAME
kaggle kernels output punzalan/melanoma-$TASK_NAME
cat melanoma-$TASK_NAME.log
