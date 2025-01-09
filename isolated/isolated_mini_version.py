all_numbers = {str(i):None for i in range(10,100)}
for num in all_numbers:
    counter = 0
    this_num = num # operate on equivalent, not original
    while this_num != this_num[::-1]:
        counter += 1
        this_num = str(int(this_num) + int(this_num[::-1]))
    all_numbers[num] = counter
print(all_numbers)