from image_to_matrix import convert_to_matrix
from matrix_checker import check_cube

top = convert_to_matrix("top.jpg")
right = convert_to_matrix("right.jpg")
left = convert_to_matrix("left.jpg")

check_cube((top, right, left))