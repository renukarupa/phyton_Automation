input_string = input(" Enter a String: ")
d = { }
for i in input_string:
   d[i] = 0
for i in input_string:
   d[i] = d[i] + 1
print(d)
for i in input_string:
    if (d[i] == 1):
        print(i)

