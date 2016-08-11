from datetime import date
import csv
import copy

# Determine the season of the year
month = date.today().month
if month in range(5,10):
    current_season = "Summer"
else:
    current_season = "Winter"

def trim_idx(str_list):
    end_idx = 0
    for item in str_list:
        if len(item) != 0:
            end_idx += 1
    return end_idx

headers = []
rows = []
with open('recipes.csv', 'r') as f:
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

def ljust_trunc(str_in, width):
    if (len(str_in) > width):
        str_out = str_in[0:width]
    else:
        str_out = str_in.ljust(width)
    return str_out

def print_table_row(row, row_length):
    print(ljust_trunc(str(row[0]), 30), end='')
    for num in range(1, len(row)):
        if num < row_length:
            print(ljust_trunc(str(row[num]), 8), ' ', end='')
    print('')

def print_table(headers, rows):
    print_table_row(headers, len(headers))
    for item in rows:
        print_table_row(item, len(headers))

print_table(headers, rows)

# Read the recipes file and print only the enabled rows for this season
# list comprehension?
#    for line in reader:
#        if int(line['Enabled']) and \
#           ((line['Season'] == current_season) or \
#           (line['Season'] == 'Any')):
#                print(line['Recipe'].ljust(30),
#                      line['Season'].ljust(10),
#                      line['Enabled'])

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
