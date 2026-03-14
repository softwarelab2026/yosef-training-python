def summer(some_list):
    result = some_list[0]
    for i in some_list[1:]:
        result += i
    return result

print(summer([10, 11, 12, 0.75]))
print(summer([True, False, True, True]))
print(summer(['aa', 'bb', 'cc']))
print(summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]))