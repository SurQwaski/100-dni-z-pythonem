import random
"""Fragment kodu z kursu 100 dni Pythona. Dzis nie trzeba bylo pisac wlasnorecznie kodu, jedynie weryfikowac juz przygotowany."""

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item += item
    b_list.append(new_item)
    print(b_list)


mutate([2,5,10,12,17,22,31,44])
