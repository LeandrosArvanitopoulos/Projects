import timeit
import random


class Timeit_wrapper:
    def __init__(self, func):
        self.func = func
        self.time = 0

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            result = self.func(*args, **kwargs)
            end = timeit.default_timer()
            self.time = end - start
            print(f"{self.func.__name__} took {self.time:.3e} seconds")
            return result

        return wrapper(*args, **kwargs)


def missing_int(input: list[int]) -> int:
    length = len(input)
    proper_length = max(input) - min(input) + 1
    if length <= 1 or proper_length == len(input):  # i think the problem is here
        return 0

    middle = (
        input[len(input) // 2 - 1] + 1
        if input[len(input) // 2 - 1] + 1 != input[len(input) // 2]
        else 0
    )
    if middle:
        return middle
    left = missing_int(input[: len(input) // 2])
    if left:
        return left
    right = missing_int(input[len(input) // 2 :])
    return right


@Timeit_wrapper
def best_solution(input: list[int]) -> int:
    l = len(input)
    return (l * (l + 1) // 2) - sum(input)


max_len = 1000
miss = random.randint(0, max_len)
li = [x for x in range(max_len) if x != miss]
my_solution = Timeit_wrapper(missing_int)

# assert my_solution(li) == miss
print(my_solution(li))
# assert best_solution(li) == miss
print(best_solution(li))
