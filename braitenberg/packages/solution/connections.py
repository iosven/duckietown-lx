from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    # middle_index_vertical = 240
    # middle_index_horizontal = 320

    # we have zeros in the middle in res[:,315:325]
    # for corner cases when a duck is in front but mostly on one side
    middle_index_horizontal_gap_start = 315
    middle_index_horizontal_gap_end = 325

    # we have zeros above the horizon in res[0:80,:] to ignore things in sky, walls, background
    relevant_vertical_from_index = 10
    # we have zeros where we see the floor in res[400:480,:] to ignore markings on the floor
    relevant_vertical_to_index = 470
    # we have zeros on the far left res[:,0:80] to ignore things far left
    relevant_horizontal_from_index = 10
    # we have zeros on the far right res[:,560:640] to ignore things far right
    relevant_horizontal_to_index = 630

    # bias for steering right
    steering_right_bias_magic_number = 0.5

    # if there is a duck on the left, the left motor needs to be faster in order to turn right
    res[relevant_vertical_from_index:relevant_vertical_to_index, relevant_horizontal_from_index:middle_index_horizontal_gap_start] = (0.95 + steering_right_bias_magic_number)

    # if there is a duck on the right, the left motor needs to be slower in order to turn left
    res[relevant_vertical_from_index:relevant_vertical_to_index, middle_index_horizontal_gap_end:image_width] = -0.012

    # just in case set the areas we want to ignore to zero explicitly
    res[0:relevant_vertical_from_index, :] = 0.0
    res[relevant_vertical_to_index:image_height, :] = 0.0
    res[:, 0:relevant_horizontal_from_index] = 0.0
    res[:, relevant_horizontal_to_index:image_width] = 0.0

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")

    image_height = 480
    image_width = 640

    # middle_index_vertical = 240
    # middle_index_horizontal = 320

    # we have zeros in the middle in res[:,315:325]
    # for corner cases when a duck is in front but mostly on one side
    middle_index_horizontal_gap_start = 315
    middle_index_horizontal_gap_end = 325

    # we have zeros above the horizon to ignore some things in sky, walls, background
    relevant_vertical_from_index = 10
    # we have zeros where we see the floor
    relevant_vertical_to_index = 470
    # we have zeros on the far left to ignore things far left
    relevant_horizontal_from_index = 10
    # we have zeros on the far right to ignore things far right
    relevant_horizontal_to_index = 630

    # if there is a duck on the left, the left motor needs to be faster in order to turn right
    res[relevant_vertical_from_index:relevant_vertical_to_index, relevant_horizontal_from_index:middle_index_horizontal_gap_start] = -0.015

    # if there is a duck on the right, the left motor needs to be slower in order to turn left
    res[relevant_vertical_from_index:relevant_vertical_to_index, middle_index_horizontal_gap_end:image_width] = 0.95

    # just in case set the areas we want to ignore to zero explicitly
    res[0:relevant_vertical_from_index, :] = 0.0
    res[relevant_vertical_to_index:image_height, :] = 0.0
    res[:, 0:relevant_horizontal_from_index] = 0.0
    res[:, relevant_horizontal_to_index:image_width] = 0.0

    return res
