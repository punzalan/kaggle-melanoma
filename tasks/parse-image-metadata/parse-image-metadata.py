import glob
import json
import os

import pandas as pd
import pydicom


DIR_BASE = "/kaggle/input/siim-isic-melanoma-classification/train"
PATHS = glob.glob(os.path.join(DIR_BASE, "*"))


def jsonify_sequence(sequence):
    if len(sequence) == 0:
        return []
    return [datum.to_json_dict() for datum in sequence]


def parse_image_metadata(path):

    dcm = pydicom.dcmread(path)

    fields_camel = [
        field
        for field in dir(dcm)
        if field.lower() != field and not field.startswith("_")
    ]

    data = {}
    for camel in fields_camel:
        elem = getattr(dcm, camel)
        if isinstance(elem, pydicom.sequence.Sequence):
            data[camel] = json.dumps(jsonify_sequence(elem))
        elif isinstance(elem, (str, int)):
            data[camel] = elem
        elif isinstance(
            elem, (pydicom.valuerep.PersonName, pydicom.valuerep.PersonName3)
        ):
            data[camel] = str(elem)
        elif isinstance(elem, pydicom.multival.MultiValue):
            data[camel] = json.dumps(list(elem))
        elif camel == "PixelData":
            pass
        else:
            print(elem, type(elem))
            raise RuntimeError

    return data


records = [parse_image_metadata(path) for path in PATHS]
metadata = pd.DataFrame.from_records(records)
metadata.to_parquet("/kaggle/working/metadata.parquet")
