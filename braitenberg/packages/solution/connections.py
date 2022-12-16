from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    # middle_index_vertical = 240
    # middle_index_horizontal = 320
    # minimal bias to steering right by using a smaller blind gap in the middle of the optical perceptor
    middle_index_horizontal_gap_start = 302
    middle_index_horizontal_gap_end = 338

    # relevant_vertical_speed_source_to_index = 190

    relevant_vertical_from_index = 200
    relevant_vertical_to_index = 400
    relevant_horizontal_from_index = 95
    relevant_horizontal_to_index = 545

    # relevant_bar_vertical = (relevant_vertical_from_index, relevant_vertical_to_index)
    # relevant_bar_horizon = (relevant_horizontal_from_index, relevant_horizontal_to_index)

    # more bias for steering right
    steering_right_bias_magic_number = 0.15

    # if there is a duck on the left, the left motor needs to be faster in order to turn right
    res[relevant_vertical_from_index:relevant_vertical_to_index, relevant_horizontal_from_index:middle_index_horizontal_gap_start] = (0.8 + steering_right_bias_magic_number)

    # if there is a duck on the right, the left motor needs to be slower in order to turn left
    res[relevant_vertical_from_index:relevant_vertical_to_index, middle_index_horizontal_gap_end:image_width] = 0.04

    # area above considered irrelevant
    res[0:relevant_vertical_from_index, :] = 0.0
    # tried to use some far away duckies on the horizon as source of speed
    # res[0:relevant_vertical_speed_source_to_index, :] = 0.02

    # area below considered irrelevant
    res[relevant_vertical_to_index:image_height, :] = 0.0

    # area on the far left considered irrelevant
    res[:, 0:relevant_horizontal_from_index] = 0.0

    # area on the far right considered irrelevant
    res[:, relevant_horizontal_to_index:image_width] = 0.0

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    # middle_index_vertical = 240
    # middle_index_horizontal = 320
    middle_index_horizontal_gap_start = 295
    middle_index_horizontal_gap_end = 354

    # relevant_vertical_speed_source_to_index = 190

    relevant_vertical_from_index = 200
    relevant_vertical_to_index = 400
    relevant_horizontal_from_index = 95
    relevant_horizontal_to_index = 545

    # relevant_bar_vertical = (relevant_vertical_from_index, relevant_vertical_to_index)
    # relevant_bar_horizon = (relevant_horizontal_from_index, relevant_horizontal_to_index)

    # if there is a duck on the left, the right motor needs to be slower
    res[relevant_vertical_from_index:relevant_vertical_to_index, relevant_horizontal_from_index:middle_index_horizontal_gap_start] = 0.04

    # if there is a duck on the right, the right motor needs to be faster
    res[relevant_vertical_from_index:relevant_vertical_to_index, middle_index_horizontal_gap_end:image_width] = 0.8

    # area above considered irrelevant
    res[0:relevant_vertical_from_index, :] = 0.0
    # tried to use some far away duckies on the horizon as source of speed
    # res[0:relevant_vertical_speed_source_to_index, :] = 0.02

    # area below considered irrelevant
    res[relevant_vertical_to_index:image_height, :] = 0.0

    # area on the far left considered irrelevant
    res[:, 0:relevant_horizontal_from_index] = 0.0

    # area on the far right considered irrelevant
    res[:, relevant_horizontal_to_index:image_width] = 0.0

    return res
