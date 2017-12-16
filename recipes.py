import csv
import copy
import random

def trim_idx(str_list):
    end_idx = 0
    for item in str_list:
        if len(item) != 0:
            end_idx += 1
    return end_idx

def ljust_trunc(str_in, width):
    if (len(str_in) > width):
        str_out = str_in[0:width]
    else:
        str_out = str_in.ljust(width)
    return str_out

def print_table_row(row, row_length):
    print(ljust_trunc(str(row[0]), 30), end='')
    for num in range(1, len(row)-1):
        if num < row_length:
            print(ljust_trunc(str(row[num]), 6), ' ', end='')
    print(ljust_trunc(str(row[len(row)-1]), 35), end='')
    print('')

class Recipes(object):
    def __init__(self):
        self.rows = []
        self.headers = []

    def load_from_file(self, filename):
        headers = []
        rows = []

        # Read the data
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            count = 0
            for line in reader:
                if count == 0:
                    headers = copy.deepcopy(line)
                    headers = headers[:trim_idx(headers)]
                else:
                    row = copy.deepcopy(line)
                    row = row[:trim_idx(row)]
                    rows.append(row)
                count += 1

        f.closed

        #Format the data.
        recipes = []
        for row in rows:
            recipe = {}
            for num in range(len(headers) - 1):
                recipe[headers[num]] = row[num]
            grocery_list = []
            for num in range(len(headers)-1, len(row)):
                grocery_list.append(row[num])
            recipe[headers[len(headers) - 1]] = grocery_list
            recipes.append(recipe)

        self.rows = recipes
        self.headers = headers

    def pretty_print(self):
        print_table_row(self.headers, len(self.headers))
        names = []
        for dict_item in self.rows:
            as_list = []
            names.append(dict_item[self.headers[0]]);
            for num in range(len(self.headers)):
                as_list.append(dict_item[self.headers[num]])
            print_table_row(as_list, len(as_list))
        print('(%s, ' % names[0], end='');
        for i in range(1,len(names)-1):
            print('%s, ' % names[i], end='');
        print('%s)' % names[len(names)-1]);

    def filter(self, key, allowed_values):
        other = Recipes()
        other.headers = self.headers

        for row in self.rows:
            #print('(%s, %s, %s)' % (key, row[key], allowed_values))
            if row[key] in allowed_values:
                other.rows.append(row)
        return other

    def random_recipe(self):
        rand_int = random.randrange(len(self.rows))
        other = Recipes()
        other.headers = self.headers
        other.rows.append(self.rows[rand_int])
        return other

    def add(self, other):
        #FIXUP: If headers not the same, throw a fit
        for row in other.rows:
            self.rows.append(row)

    def print_grocery_list(self):
        print('Grocery list: -------------')
        grocery_list = []
        for row in self.rows:
            for item in row['Grocery list']:
                grocery_list.append(item)
        grocery_list = list(set(grocery_list))
        for item in grocery_list:
            print(item)
