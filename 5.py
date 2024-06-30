# Моя первая
count = 0
with open("input.txt","r") as input_file:
    for line in input_file:
        numbers = list(map(int, line.split()))
        counts = {}
        for number in numbers:
            if number in counts:
                counts[number] += 1
            else:
                count[number] = 1
        count_values = list(count.values())
        count_values.sort()
        if count_values == [1, 1, 3, 5]:
            avg = sum(numbers) / 10
            unique_elements = []
            for number in numbers:
                if counts[number] == 1:
                    unique_elements.append(number)
            for number in unique_elements:
                if number in unique_elements:
                    if number > avg:
                        count += 1
                        break
print(count)
