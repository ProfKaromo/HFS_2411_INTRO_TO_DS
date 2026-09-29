#Loops
# x = [3,4,5,6,7,8,9,3,9,2,5]
# even_no = odd_no = 0
# for i in range(0,len(x)):
#     if x[i] % 2 == 0:
#         even_no += 1
#         print(x[i]," is an even number.")
#     else:
#         odd_no += 1
#         print(x[i]," is an odd number.")
# print("There are ",even_no,"even numbers in the list. and ",odd_no,"odd numbers in the list.")

for i in range(1,6):
    for j in range(1,6):
        if j==i or i==1 or i==5:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print("\n")

#While loop
x = 6
while x<=10:
    print(x)
    x+=1

for x in range(6,11):
    print(x)