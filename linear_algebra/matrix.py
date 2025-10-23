from numbers.rational import RationalNumber
from .vector import Vector
class Matrix:
    def __init__(self, row_vectors):
        # Check types and length
        if len(row_vectors) == 0:
            raise ValueError('The matrix must have at least one row')
        length = row_vectors[0].length()
        for vector in row_vectors:
            if not isinstance(vector, Vector):
                raise TypeError('The vectors must be of class Vector')
            if vector.length() != length:
                raise TypeError('The vectors must have the same length')
        self.row_vectors = row_vectors

    def add(self, other_matrix):
        # Check that they match dimensions
        if len(self.row_vectors) != len(other_matrix.row_vectors):
            raise ValueError('The matrix must have the same number of rows')
        # We can only check once since Matrix obj definition already checks
        if self.row_vectors[0].length() != other_matrix.row_vectors[0].length():
            raise ValueError('The matrices must have the same number of columns')

        new_row_vectors = []
        for i in range(len(self.row_vectors)):
            new_row_vectors.append(self.row_vectors[i].add(other_matrix.row_vectors[i]))
        return Matrix(new_row_vectors)

    def subtract(self, other_matrix):
        # Check that they match dimensions
        if len(self.row_vectors) != len(other_matrix.row_vectors):
            raise ValueError('The matrix must have the same number of rows')
        # We can only check once since Matrix obj definition already checks
        if self.row_vectors[0].length() != other_matrix.row_vectors[0].length():
            raise ValueError('The matrices must have the same number of columns')

        new_row_vectors = []
        for i in range(len(self.row_vectors)):
            new_row_vectors.append(self.row_vectors[i].subtract(other_matrix.row_vectors[i]))
        return Matrix(new_row_vectors)

    def scale(self, scalar):
        if not isinstance(scalar, RationalNumber):
            raise TypeError('The scalar must be an RationalNumber')
        new_row_vectors = []
        for i in range(len(self.row_vectors)):
            new_row_vectors.append(self.row_vectors[i].scale(scalar))
        return Matrix(new_row_vectors)

    def multiply(self, other_matrix):
        # Check that number of rows of first one is the matching the number of columns of the second one
        if self.row_vectors[0].length() != len(other_matrix.row_vectors):
            raise ValueError('The matrices must have be compatible: A x B iff # columns of A = # rows of B')
        new_row_vectors = []
        for i in range(len(self.row_vectors)):
            new_vector = []
            for j in range(other_matrix.row_vectors[0].length()):
                new_vector.append(self.row_vectors[i].dot_product(other_matrix.get_column(j)))
            new_row_vectors.append(Vector(new_vector))
        return Matrix(new_row_vectors)

    def get_column(self, col_index):
        column = []
        for vector in self.row_vectors:
            column.append(vector.components[col_index])
        return Vector(column)

    def __repr__(self):
        return f"Matrix([\n  {'\n  '.join(map(str, self.row_vectors))}\n])"

    def swap_rows(self, i, j):
        self.row_vectors[i], self.row_vectors[j] = self.row_vectors[j], self.row_vectors[i]

    def scale_row(self, row_index, scalar):
        self.row_vectors[row_index] = self.row_vectors[row_index].scale(scalar)

    def add_row_multiple(self, target_row, source_row, scalar):
        self.row_vectors[target_row] = self.row_vectors[target_row].add(self.row_vectors[source_row].scale(scalar))

    def gaussian_elimination(self):
        current_row = 0
        negative_one = RationalNumber([1], [1]).negate()
        for column_index in range(self.row_vectors[0].length()):
            # Find pivot
            pivot_found = False
            for row_index in range(current_row, len(self.row_vectors)):
                if not self.row_vectors[row_index].components[column_index].is_zero():
                    pivot_row = row_index
                    pivot_found = True
                    break
            if not pivot_found:
                # This column is all zeros, just move to the next column
                continue
            # Swap
            self.swap_rows(pivot_row, current_row)
            # Scale
            pivot_element = self.row_vectors[current_row].components[column_index]
            self.scale_row(current_row,scalar=pivot_element.reciprocal())
            # Eliminate
            for row_index in range(0, len(self.row_vectors)):
                if row_index != current_row:
                    # Find the right scalar
                    scalar = self.row_vectors[row_index].components[column_index].multiply(negative_one)
                    self.add_row_multiple(row_index, current_row, scalar)
            current_row += 1
            if current_row >= len(self.row_vectors):
                break
