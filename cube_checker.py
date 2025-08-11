from face import CubeFace
from cube_validator import ThreeSidedCubeValidator
import sys

def run_validation(top, right, left):
    """
    Main function to initialize and run the cube validation process.
    """

    # 1. Create CubeFace objects from the image files
    top_face = CubeFace(top)
    right_face = CubeFace(right)
    left_face = CubeFace(left)

    # 2. Create the validator with the face objects
    cube_validator = ThreeSidedCubeValidator(
        top_face=top_face,
        right_face=right_face,
        left_face=left_face
    )

    # 3. Run the complete validation process
    cube_validator.validate()




if __name__ == "__main__":
    run_validation()