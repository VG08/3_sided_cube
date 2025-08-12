from cube_checker import run_validation
import numpy as np
from image_processing import image_to_color_array
from matrix_checker import check_cube

image1 = "logo.png" #top
image2 = "gn.png" #right
image3 = "iit.png" #left


matrix1 = image_to_color_array(image_path=image1)
matrix2 = image_to_color_array(image_path=image2)
matrix3 = image_to_color_array(image_path=image3)
matrix1_new = []
matrix2_new = []
matrix3_new = []
for i in range(30):
    matrix1_new.append([])
    matrix2_new.append([])
    matrix3_new.append([])
    for j in range(30):
        matrix1_new[i].append(int(matrix1[i][j].item()))
        matrix2_new[i].append(int(matrix2[i][j].item()))
        matrix3_new[i].append(int(matrix3[i][j].item()))
print(matrix1_new)
for i in range(10):
    for j in range(10):
        top_cube_matrix = []
        # print(list(matrix1_new[j*3][i*3:i*3+3]))
        cube_matrix = []
        print(i, j)
        top_cube_matrix.append(list((matrix1_new[j*3][i*3:i*3+3])))
        top_cube_matrix.append(list((matrix1_new[j*3][i*3:i*3+3])))
        top_cube_matrix.append(list((matrix1_new[j*3][i*3:i*3+3])))
        right_cube_matrix = []
        right_cube_matrix.append(list((matrix2_new[j*3][i*3:i*3+3])))
        right_cube_matrix.append(list((matrix2_new[j*3][i*3:i*3+3])))
        right_cube_matrix.append(list((matrix2_new[j*3][i*3:i*3+3])))
        left_cube_matrix = []
        left_cube_matrix.append(list((matrix3_new[j*3][i*3:i*3+3])))
        left_cube_matrix.append(list((matrix3_new[j*3][i*3:i*3+3])))
        left_cube_matrix.append(list((matrix3_new[j*3][i*3:i*3+3])))
        if not check_cube((top_cube_matrix, right_cube_matrix, left_cube_matrix)):
            input()
        # top_cube_matrix = np.array(top_cube_matrix)
        # right_cube_matrix = np.array(right_cube_matrix)
        # left_cube_matrix = np.array(left_cube_matrix)
        # print(top_cube_matrix)
        # run_validation(top_cube_matrix, right_cube_matrix, left_cube_matrix)
        # input()
