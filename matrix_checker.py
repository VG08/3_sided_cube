## matrix format
##

##[
## [1, 2, 3],
## [4, 5, 6],
## [7, ,8 ,9] 
## ]

'''Colour formatting is as follows:
    - White - 1
    - Yellow - 6
    - Green - 2
    - Blue - 5
    - Orange - 3
    - Red - 4 
'''
from collections import Counter
top = [
    [5, 4, 3],
    [4, 2, 5],
    [1, 5, 2]
] 

right = [
    [4, 3, 1],
    [1, 4, 4],
    [4, 5, 4]
]

left = [
    [1, 5, 2],
    [2, 1, 3],
    [5, 5, 5]
]
#(WOB, WBR,WRG,WGO, YBO,YOG,YGR,YRB)
CENTER_CYCLIC_ORDER =[(1, 3, 5), (1, 5, 4), (1, 4, 2), (1, 2, 3), (6, 5, 3), (6, 3, 2), (6, 2, 4), (6, 4, 5)]



def check_centers(centers):
    # centers = (side1[1][1], side2[1][1], side3[1][1])
    # for center in centers:
    #     if center == 1:
            
    #     elif center == 6:
    #         pass
    if centers[0] == 1 or centers[0] == 6 :
        to_compare = centers
    elif centers[1] == 1 or centers[1] == 6:
        to_compare = (centers[1], centers[2], centers[0])
    elif centers[2] == 1 or centers[2] == 6:
        to_compare = (centers[2], centers[0], centers[1])
    else:
        return False
    

    if to_compare in CENTER_CYCLIC_ORDER:
        return True
    else:
        return False
    

def check_edges(edges):    
    color_counter = [0, 0, 0, 0, 0, 0]

    for edge in edges:
        i = edge - 1
        color_counter[i] +=1
        if color_counter[i] > 4:
            return False
    return True
def check_common_edges(edges):
    for edge in edges:
        if edge[0] == edge[1]:
            return False
        elif edge[0] + edge[1] == 7:
            return False
    return True



def corner_check(top, right, left):
    two_face_corners = [(top[0][0], left[0][0]), (top[2][2], right[0][2]), (right[2][0], left[2][2])]
    three_face_corner = (top[2][0], right[0][0], left[0][2])
    
    corner_list = [
                    (1, 3, 5), (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1),
                    (1, 5, 4), (1, 4, 5), (5, 1, 4), (5, 4, 1), (4, 1, 5), (4, 5, 1),
                    (1, 4, 2), (1, 2, 4), (4, 1, 2), (4, 2, 1), (2, 1, 4), (2, 4, 1),
                    (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1),
                    (6, 5, 3), (6, 3, 5), (5, 6, 3), (5, 3, 6), (3, 6, 5), (3, 5, 6),
                    (6, 3, 2), (6, 2, 3), (3, 6, 2), (3, 2, 6), (2, 6, 3), (2, 3, 6),
                    (6, 2, 4), (6, 4, 2), (2, 6, 4), (2, 4, 6), (4, 6, 2), (4, 2, 6),
                    (6, 4, 5), (6, 5, 4), (4, 6, 5), (4, 5, 6), (5, 6, 4), (5, 4, 6)
                ]
    print(three_face_corner)
    print(two_face_corners)
    
    if three_face_corner in corner_list:
        print('Corner exists!')
    else:
        print("Failed Task")
    
    
    for i in range(len(three_face_corner)):
        for j in range(i + 1, len(three_face_corner)):
            test_face_1 = three_face_corner[i]
            test_face_2 = three_face_corner[j]
            counter = 0
            for corner in two_face_corners:
                if test_face_1 in corner and test_face_2 in corner:
                    counter += 1
    
            if counter > 1:
                print("You got cooked")
                return False
            else:
                print("You suceeded")
    
    corner_color_list = [
                            top[0][0], top[2][0], top[0][2], top[2][2], 
                            right[0][0], right[2][0], right[0][2], right[2][2], 
                            left[0][0], left[2][0], left[0][2], left[2][2]
                        ]
    color_count(corner_color_list)
    
def color_count(corners):
    counts = Counter(corners)
    print(counts)
    for element, value in counts.items():
        if value > 4:
            print(f"Too many corner faces with {element} colour code")


def check_cube(sides):

    centers = (sides[0][1][1], sides[1][1][1], sides[2][1][1])
    common_edges = ((sides[0][1][0], sides[2][0][1]), (sides[0][2][1],sides[1][0][1]), (sides[1][1][0],sides[2][1][2]))
    all_edges = []
    for side in sides:
        all_edges.extend([side[0][1], side[1][0], side[1][2], side[2][1]])

    
    
    print("Centers:", check_centers(centers))
    print("Edges: ", check_edges(all_edges))
    print("Common Edges", check_common_edges(common_edges))
    print("Corners", corner_check(sides[0], sides[1], sides[2]))


# check_cube((top, right, left))