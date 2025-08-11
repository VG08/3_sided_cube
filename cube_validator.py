from collections import Counter
from face import CubeFace

class ThreeSidedCubeValidator:
    """
    Validates the state of a 3-sided view of a Rubik's cube.
    """
    _COLOR_NAMES = {
        1: "White", 2: "Green", 3: "Orange", 
        4: "Red", 5: "Blue", 6: "Yellow"
    }
    
    _VALID_CENTER_COMBOS = [
        (1, 3, 5), (1, 5, 4), (1, 4, 2), (1, 2, 3), # White-centric
        (6, 5, 3), (6, 3, 2), (6, 2, 4), (6, 4, 5)  # Yellow-centric
    ]

    def __init__(self, top_face: CubeFace, right_face: CubeFace, left_face: CubeFace):
        """
        Initializes the validator with three CubeFace objects.
        """
        self.top = top_face
        self.right = right_face
        self.left = left_face
        self.results = {}

    def _check_centers(self):
        """Checks if the center piece combination is valid."""
        centers = (self.top.center, self.right.center, self.left.center)
        
        # Normalize the order to check against the valid combinations
        if centers[0] in [1, 6]: to_compare = centers
        elif centers[1] in [1, 6]: to_compare = (centers[1], centers[2], centers[0])
        elif centers[2] in [1, 6]: to_compare = (centers[2], centers[0], centers[1])
        else: return False, "No White or Yellow center found."

        if to_compare in self._VALID_CENTER_COMBOS:
            return True, "Center combination is valid."
        else:
            return False, f"Invalid center combination: {centers}."

    def _check_edge_counts(self):
        """Checks if any color appears more than 4 times across all edges."""
        all_edges = self.top.edges + self.right.edges + self.left.edges
        counts = Counter(all_edges)
        
        for color, count in counts.items():
            if count > 4:
                return False, f"Invalid edge count: {self._COLOR_NAMES[color]} appears {count} times (max 4)."
        return True, "Edge piece counts are valid."

    def _check_common_edges(self):
        """Checks for invalid adjacent edge pairs (same or opposite colors)."""
        common_edges = [
            (self.top.matrix[1, 0], self.left.matrix[0, 1]),   # Top-Left
            (self.top.matrix[2, 1], self.right.matrix[0, 1]),  # Top-Right
            (self.right.matrix[1, 0], self.left.matrix[1, 2]) # Right-Left
        ]
        
        for c1, c2 in common_edges:
            if c1 == c2: return False, f"Invalid edge: Two adjacent pieces are {self._COLOR_NAMES[c1]}."
            if c1 + c2 == 7: return False, f"Invalid edge: Opposite colors ({self._COLOR_NAMES[c1]}, {self._COLOR_NAMES[c2]}) are adjacent."
        return True, "Common edges are valid."

    def _check_corners(self):
        """Checks for invalid corner configurations."""
        # Check 1: No color should appear on more than 4 corner stickers
        all_corners = self.top.corners + self.right.corners + self.left.corners
        counts = Counter(all_corners)
        for color, count in counts.items():
            if count > 4:
                return False, f"Invalid corner count: {self._COLOR_NAMES[color]} appears {count} times (max 4)."

        # Check 2: A single corner piece cannot have opposite colors
        three_face_corner = (self.top.matrix[2, 0], self.right.matrix[0, 0], self.left.matrix[0, 2])
        colors = list(three_face_corner)
        for i in range(3):
            for j in range(i + 1, 3):
                if colors[i] + colors[j] == 7:
                    return False, f"Invalid corner: Opposite colors ({self._COLOR_NAMES[colors[i]]}, {self._COLOR_NAMES[colors[j]]}) on one piece."
        return True, "Corner pieces are valid."

    def validate(self):
        """Runs all validation checks and prints a summary report."""
        print("--- Cube State---")
        print(f"Top Face:\n{self.top}\n")
        print(f"Right Face:\n{self.right}\n")
        print(f"Left Face:\n{self.left}\n")
        
        # Run all checks
        self.results['Centers'] = self._check_centers()
        self.results['Edge Counts'] = self._check_edge_counts()
        self.results['Common Edges'] = self._check_common_edges()
        self.results['Corners'] = self._check_corners()
        
        print("--- Validation Results ---")
        overall_valid = True
        for check, (is_valid, message) in self.results.items():
            status = "✅ PASSED" if is_valid else "❌ FAILED"
            print(f"{check:<15} {status} - {message}")
            if not is_valid: overall_valid = False
        
        print("\n--- Overall Status ---")
        if overall_valid:
            print("🎉 The cube configuration appears to be VALID.")
        else:
            print("😟 The cube configuration appears to be INVALID.")
        
        return overall_valid