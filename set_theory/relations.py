from .custom_set import CustomSet

def create_ordered_pair(a, b):
    set_a = CustomSet()
    set_a.add(a)
    set_ab = CustomSet()
    set_ab.add(a)
    set_ab.add(b)
    final_set = CustomSet()
    final_set.add(set_a)
    final_set.add(set_ab)
    return final_set

def is_function(relation_set, domain_set):
    for element in domain_set.elements:
        counter = 0
        for pair in relation_set.elements:
            try:
                first_element = get_first_element(pair)
                if first_element == element:
                    counter += 1
            except ValueError:
                continue
        if counter != 1:
            return False
    return True

def get_first_element(pair_set):
    for element in pair_set.elements:
        if len(element) == 1:
            return element.elements[0]
    raise ValueError('No element in pair_set')