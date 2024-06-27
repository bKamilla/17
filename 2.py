#первая задача,где файл с 8 эл в строке
'''with open('123.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n',' ').split()
        lines_set.append(set(lines[i]))
    for i in range(len(lines)):
        count_nums=[]
        for num in lines_set:
            count_nums
print(lines)
print(lines_set)'''

with open('123.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n',' ').split()
        lines_set.append(set(lines[i]))
print(lines)
max_elems = []
lines_count_sorted = []
for i in range(lin(lines)):
    max_elems_i = []
    line_sort = []
    for j in lines[i]:
        if lines[i].count(j) == 1:
            max_elems_i.append(int(j))
        line_sort.append(lines[i].count(j))
         