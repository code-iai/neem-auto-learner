import sys

import auto_learner.auto_learner as auto_learner

if __name__ == "__main__":
    args = sys.argv[1:]
    raw_neems_path = args[0]
    vec_neems_path = args[1]

    auto_learner.transform_raw_neems_to_vec_neems(raw_neems_path, vec_neems_path)
