from decorator import append

from arithmetic.calculator import add_binary, subtract_binary
from numbers.rational import RationalNumber


class Vector:
    def __init__(self, components):
        for component in components:
            if not isinstance(component, RationalNumber):
                raise TypeError('The component must be an RationalNumber')
        self.components = components

    def add(self, other_vector):
        # They need to be of the same length
        if not other_vector.length() == self.length():
            raise TypeError('The vectors must have the same length')
        new_components = []
        for i in range(0, self.length()):
            # element wise subtraction between RationalNumber
            new_components.append(self.components[i].add(other_vector.components[i]))
        return Vector(new_components)

    def subtract(self, other_vector):
        # They need to be of the same length
        if not other_vector.length() == self.length():
            raise TypeError('The vectors must have the same length')
        new_components = []
        for i in range(0, self.length()):
            # element wise subtraction between RationalNumber
            new_components.append(self.components[i].subtract(other_vector.components[i]))
        return Vector(new_components)

    def scale(self, scalar):
        if not isinstance(scalar, RationalNumber):
            raise TypeError('The scalar must be an RationalNumber')
        new_components = []
        for i in range(0, self.length()):
            new_components.append(self.components[i].multiply(scalar))
        return Vector(new_components)

    def dot_product(self, other_vector):
        # They need to be of the same length
        if not other_vector.length() == self.length():
            raise TypeError('The vectors must have the same length')
        running_sum = RationalNumber([0], [1])
        for i in range(0, self.length()):
            running_sum = running_sum.add(self.components[i].multiply(other_vector.components[i]))
        return running_sum

    def length(self):
        return len(self.components)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"