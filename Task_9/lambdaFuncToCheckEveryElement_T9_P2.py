from functools import reduce

test_list = [["Python",1,2,3],[ 4, "is"],[8, "language", 1]]

print("The original list : " + str(test_list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances is string : " + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The string instances is integer : " + str(res1))

