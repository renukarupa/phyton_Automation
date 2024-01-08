import datetime

file_content = open("currentTimeStamp.txt")  # return you a stream of objects .
# print(file_content)
# print(type(file_content))
print(file_content.read())

#Current TimeStamp
ts = datetime.datetime.now().timestamp()
print(ts)
readable = datetime.datetime.fromtimestamp(1704697560).isoformat()
print(readable)








