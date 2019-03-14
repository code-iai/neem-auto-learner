import sys

import auto_learner.auto_learner as auto_learner

if __name__ == "__main__":
    args = sys.argv[1:]
    raw_neems_path = args[0]
    vec_neems_path = args[1]
    training_data_result_path = args[2]

    print 'Transforming NEEMs into vectors ...'
    auto_learner.transform_raw_neems_to_vec_neems(raw_neems_path, vec_neems_path)
    print 'DONE Transforming NEEMs into vectors'
    print 'Extracting grasping data from vectors...'
    auto_learner.generate_grasping_learning_data(vec_neems_path, training_data_result_path)
    print 'DONE Extracting grasping data from vectors'
    print 'Training grasping models ...'
    auto_learner.generate_grasping_models(training_data_result_path)
    print 'DONE Training grasping models'
