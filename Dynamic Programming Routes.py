import timeit


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


@Timeit_wrapper
def countRoutes(rows, columns):
    dp = [[0 for i in range(columns)] for j in range(rows)]
    dp[0][0] = 1
    for i in range(rows):
        for j in range(columns):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[rows - 1][columns - 1]


def recurringCountRoutes(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return recurringCountRoutes(rows - 1, columns) + recurringCountRoutes(
        rows, columns - 1
    )


countRoutes(3, 3)
time1 = countRoutes.time
##how to use wrapper for recursive functions
##if you don't want to have wrapper repeat for every recursion
recurr = Timeit_wrapper(recurringCountRoutes)
recurr(3, 3)
time2 = recurr.time
overall_speedup = time1 / time2
print(f"The recursive function had a speedup {overall_speedup:.3f}")
