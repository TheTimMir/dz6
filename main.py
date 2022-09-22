result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # we can't use dict as a name of dict element
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as ex:
        ex_formated = str(type(ex)).split("'")[1]
        print(f"Caught {ex_formated}: element {key}")

print(result)
