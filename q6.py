def find_first_negative(lst):
    if not isinstance(lst, list):
        return None  # handle non-list input

    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]  # return first negative number in 1st using a while loop
        i += 1 

    return "No negatives"

if __name__ == "__main__":
    # 1
    result1 = find_first_negative([3, 5, -1, 7, -2, 8])
    print(result1)  # should show: -1

    # 2
    result2 = find_first_negative([2, 10, 7, 0])
    print(result2)  # should show: "No negatives"