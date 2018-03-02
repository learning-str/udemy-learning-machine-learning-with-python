data_list = []

data_list_file = open('data.csv')

for datum in data_list_file:
    datum = datum.rstrip().split(',')
    data_list.append([datum[0], int(datum[1])])

data_list_file.close()

print data_list
