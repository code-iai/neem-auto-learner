from os import listdir
from os.path import join

from narrative2vec import Narrative


def transform_raw_neems_to_vec_neems(path, result_dir_path):
    for neemName in listdir(path):
            neem_path = join(path, neemName)

            narrative = Narrative(neem_path)
            narrative.transform_to_csv_file(result_dir_path)
