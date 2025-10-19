class CustomSet:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def contains(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def union(self, other_set):
        new_set = CustomSet()
        for element in self.elements:
            new_set.add(element)
        for element in other_set.elements:
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        new_set = CustomSet()
        for element in self.elements:
            if other_set.contains(element):
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        new_set = CustomSet()
        for element in self.elements:
            if not (other_set.contains(element)):
                new_set.add(element)
        return new_set

    def cartesian_product(self, other_set):
        from .relations import create_ordered_pair
        product_set = CustomSet()
        for element in self.elements:
            for other_element in other_set.elements:
                pair_set = create_ordered_pair(element, other_element)
                product_set.add(pair_set)
        return product_set

    def is_subset(self, other_set):
        for element in self.elements:
            if not other_set.contains(element):
                return False
        return True

    def is_equal(self, other_set):
        if len(self.elements) != len(other_set.elements):
            return False
        for element in self.elements:
            if not other_set.contains(element):
                return False
        return True

    def symmetric_difference(self, other_set):
        new_set = self.union(other_set).difference(self.intersection(other_set))
        return new_set

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return "{"+",".join(map(str, self.elements))+"}"

