print("******** Pyramid of numbers ********")

for i in range(1,21):
     for j in range(21 - i):
         print(" ",end = " ")
     for j in range(1,i):
         print(j, end = " ")
     for i in range (i,0,-1):
         print(i, end = " ")
     print ("\n")


