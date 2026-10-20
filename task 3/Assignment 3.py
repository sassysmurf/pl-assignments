
#this file contains a solution to the task accessible at:
#https://informatics.msk.ru/mod/statements/view.php?id=280#1

a = int(input())
b = int(input())

if a < b:
    for i in range(a, b):
        if i % 2 == 0:
            print(i, end=" ")

# if we enter 2 and 5, the output will be 2 4.