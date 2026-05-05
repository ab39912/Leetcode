class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
         # Result list to hold all rows
        triangle = []

        # Loop for each row
        for i in range(numRows):
            # Create a row with size (i+1) and initialize all elements to 1
            row = [1] * (i + 1)

            # Fill elements from index 1 to i-1 (middle values)
            for j in range(1, i):
                # Each element = sum of two elements above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Add current row to the triangle
            triangle.append(row)

        return triangle


# Complexity Analysis
#Time Complexity: O(N^2), we generate all the elements in first N rows sequentially one by one.
# Space Complexity: O(N^2), additional space used for storing the entire pascal triangle.