#если копируем путь до файла, то \ меняем на /
with open('123.txt') as f:
    n = ['0','1','2','3','4','5','6','7','8','9']
    nums = f.readline()
    nums = nums.split()

    correct_nums = []

    for num in nums:
        flag = True
        for symb in num:
            if symb not in n:
                flag = False
        if flag:
            correct_nums.append(int(num))
print(correct_nums)

