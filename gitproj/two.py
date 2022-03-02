def function(values_list):
    another_list = []
    if all(values_list):
        for i in values_list:
            another_list.append(i * 2)
        return another_list
    elif values_list:
        for i in values_list:
            if isinstance(i, int):
                another_list.append(i + 1)
            else:
                another_list.append("was None")
        if all(another_list):
            return another_list
    else:
        return values_list


some_list = [5, 0, 8, None]

print(function(some_list))
[10, 0, 16, 0]
[6, 1, 9, 1]
[6, 1, 9, "was None"]
SyntaxError