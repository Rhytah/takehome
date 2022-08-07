# Write a decorator in python that will count how many times the 
# decorated function was called. It should print the number every time
#  the decorated function is executed.

def function_call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper


@function_call_counter
def check_counter_working(x):
    return x + 1


print(check_counter_working(9))
