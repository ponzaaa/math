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