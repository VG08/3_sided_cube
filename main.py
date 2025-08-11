from cube_checker import run_validation
import numpy as np
from image_processing import image_to_color_array
image1 = "logo.png" #top
image2 = "gn.png" #right
image3 = "iit.png" #left


matrix1 = image_to_color_array(image_path=image1)
matrix2 = image_to_color_array(image_path=image2)
matrix3 = image_to_color_array(image_path=image3)

for i in range(10):
    for j in range(10):
        top_cube_matrix = []
        print(list(matrix1[j*3][i*3:i*3+3]))
        cube_matrix = []
        top_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        top_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        top_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        right_cube_matrix = []
        right_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        right_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        right_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        left_cube_matrix = []
        left_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        left_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        left_cube_matrix.append(list((matrix1[j*3][i*3:i*3+3])))
        top_cube_matrix = np.array(top_cube_matrix)
        right_cube_matrix = np.array(right_cube_matrix)
        left_cube_matrix = np.array(left_cube_matrix)
        print(top_cube_matrix)
        run_validation(top_cube_matrix, right_cube_matrix, left_cube_matrix)
        input()
