for num in {str(i):None for i in range(10,100)}:
    counter, this_num = 0, num # operate on equivalent, not original
    while this_num != this_num[::-1]:
        counter += 1
        this_num = str(int(this_num) + int(this_num[::-1]))
    print(f"{num} depth-{counter}")