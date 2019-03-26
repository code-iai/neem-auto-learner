from os import listdir
from os.path import join

from narrative2vec import Narrative
from grasping_learning_data_generator.orientation import generate_learning_data_from_neems as generate_orientation_data
from grasping_learning_data_generator.position import generate_learning_data_from_neems as generate_position_data
import grasping_position_inference.training.model_generator
from grasping_type_inference.learning import train_all_grasping_mlns


def transform_raw_neems_to_vec_neems(path, result_dir_path):
    for neemName in listdir(path):
            neem_path = join(path, neemName,'{}.owl'.format(neemName))

            narrative = Narrative(neem_path)
            narrative.transform_to_csv_file(result_dir_path)


def generate_grasping_learning_data(path, result_dir_path):
    generate_position_data(path, result_dir_path)
    generate_orientation_data(path, result_dir_path)


def generate_grasping_models(training_data_path):
    grasping_position_inference.training.model_generator.generate_models(training_data_path)
    train_all_grasping_mlns(training_data_path)

