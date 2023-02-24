def read_recipies_file(filename):
    cook_book = {}
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            name, ingridients_number = line.strip('\n'), int(f.readline())
            cook_book.setdefault(name, [])
            for _ in range(ingridients_number):
                ingridient, value, measure_unit = f.readline().split('|')
                cook_book[name].append({'ingredient_name': ingridient.strip(' '), 'quantity': value.strip(' '), 'measure': measure_unit.strip('\n ')})
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipies_file("recipies.txt")
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count})
        else:
            return "Блюдо не найдено!"
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 8))