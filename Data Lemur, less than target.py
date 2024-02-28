def intersection(a, b):
    result = []
    first_pointer = 0
    second_pointer = 0
    first_length = len(a)
    second_length = len(b)
    while first_pointer <= first_length - 1 and second_pointer <= second_length - 1:
        if a[first_pointer] == b[second_pointer]:
            result.append(a[first_pointer])
            first_pointer += 1
            second_pointer += 1

        elif a[first_pointer] > b[second_pointer]:
            second_pointer += 1

        elif a[first_pointer] < b[second_pointer]:
            first_pointer += 1

    return result
