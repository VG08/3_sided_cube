from face import CubeFace
from cube_validator import ThreeSidedCubeValidator
import sys

def run_validation():
    """
    Main function to initialize and run the cube validation process.
    """
    try:
        # 1. Create CubeFace objects from the image files
        top_face = CubeFace("top.jpg")
        right_face = CubeFace("right.jpg")
        left_face = CubeFace("left.jpg")

        # 2. Create the validator with the face objects
        cube_validator = ThreeSidedCubeValidator(
            top_face=top_face,
            right_face=right_face,
            left_face=left_face
        )

        # 3. Run the complete validation process
        cube_validator.validate()

    except FileNotFoundError as e:
        print(f"CRITICAL ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_validation()