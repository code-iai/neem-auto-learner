from narrative2vec.narrative import Narrative
from grasping_learning_data_generator.orientation import generate_learning_data_from_neems as generate_orientation_data
from grasping_learning_data_generator.position import generate_learning_data_from_neems as generate_position_data
import grasping_position_inference.training.model_generator
from grasping_type_inference.learning import train_all_grasping_mlns
from os import listdir
from os.path import join

NARRATIVES_PATH = 'narratives'
VECTORS_PATH = 'vectors'
TRAINING_DATA_PATH = 'training_data'
MODELS_PATH = 'models'
MLN_PATH = join(MODELS_PATH, 'mln')


def transform_raw_neems_to_vec_neems(path, result_dir_path):
    for neemName in listdir(path):
            neem_path = join(path, neemName,'{}.owl'.format(neemName))

            narrative = Narrative(neem_path)
            narrative.transform_to_csv_file(result_dir_path)


def generate_grasping_learning_data(path, result_dir_path):
    generate_position_data(path, result_dir_path)
    generate_orientation_data(path, result_dir_path)


def generate_grasping_models():
    grasping_position_inference.training.model_generator.generate_models(TRAINING_DATA_PATH, MODELS_PATH)
    train_all_grasping_mlns(TRAINING_DATA_PATH,MLN_PATH)

print 'Starting transforming raw neems to vectors ...'
transform_raw_neems_to_vec_neems(NARRATIVES_PATH, VECTORS_PATH)
print 'Finished transforming raw neems to vectors'

print 'Starting generating training data for grasping ...'
generate_grasping_learning_data(VECTORS_PATH, TRAINING_DATA_PATH)
print 'Finished generating training data for grasping'

print 'Starting creating models for grasping ...'
generate_grasping_models()
print 'Finished creating models for grasping'

