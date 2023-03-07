# how to specify the type of key-value pairs of a dictionary
# Python Doc: https://docs.python.org/3/library/typing.html
def do_somthing(my_input: dict[int, int]) -> dict[str, int]:
    res = {}
    for current_key in my_input:
        if len(current_key) > 2:
            res[current_key] = my_input[current_key]

    return res


x = do_somthing({10: 'x', "xx": 40})
print(x)

