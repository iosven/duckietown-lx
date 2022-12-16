from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    #middle_index_vertical_exclusive = 240
    middle_index_horizontal_exclusive = 320

    relevant_vertical_from_index = 200
    relevant_vertical_to_index_exclusive = 400
    relevant_horizontal_from_index = 100
    relevant_horizontal_to_index_exclusive = 540

    #relevant_bar_vertical = (relevant_vertical_from_index, relevant_vertical_to_index_exclusive)
    #relevant_bar_horizon = (relevant_horizontal_from_index, relevant_horizontal_to_index_exclusive)

    # if there is a duck on the left, the left motor needs to be faster in order to turn right
    res[relevant_vertical_from_index:relevant_vertical_to_index_exclusive, relevant_horizontal_from_index:middle_index_horizontal_exclusive] = 0.75

    # if there is a duck on the right, the left motor needs to be slower in order to turn left
    res[relevant_vertical_from_index:relevant_vertical_to_index_exclusive, middle_index_horizontal_exclusive:image_width] = 0.25

    # area above considered irrelevant
    res[0:relevant_vertical_from_index, :] = 0.0

    # area below considered irrelevant
    res[relevant_vertical_to_index_exclusive:image_height, :] = 0.0

    # area on the left considered irrelevant
    res[:, 0:relevant_horizontal_from_index] = 0.0

    # area on the right considered irrelevant
    res[:, relevant_horizontal_to_index_exclusive:image_width] = 0.0

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    #middle_index_vertical_exclusive = 240
    middle_index_horizontal_exclusive = 320

    relevant_vertical_from_index = 200
    relevant_vertical_to_index_exclusive = 400
    relevant_horizontal_from_index = 100
    relevant_horizontal_to_index_exclusive = 540

    #relevant_bar_vertical = (relevant_vertical_from_index, relevant_vertical_to_index_exclusive)
    #relevant_bar_horizon = (relevant_horizontal_from_index, relevant_horizontal_to_index_exclusive)

    # if there is a duck on the left, the right motor needs to be slower
    res[relevant_vertical_from_index:relevant_vertical_to_index_exclusive, relevant_horizontal_from_index:middle_index_horizontal_exclusive] = 0.25

    # if there is a duck on the right, the right motor needs to be faster
    res[relevant_vertical_from_index:relevant_vertical_to_index_exclusive, middle_index_horizontal_exclusive:image_width] = 0.75

    # area above considered irrelevant
    res[0:relevant_vertical_from_index, :] = 0.0

    # area below considered irrelevant
    res[relevant_vertical_to_index_exclusive:image_height, :] = 0.0

    # area on the left considered irrelevant
    res[:, 0:relevant_horizontal_from_index] = 0.0

    # area on the right considered irrelevant
    res[:, relevant_horizontal_to_index_exclusive:image_width] = 0.0

    return res
