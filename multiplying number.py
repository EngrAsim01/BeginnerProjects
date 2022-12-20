
# Simple challange to get the multiplication of 2 number without using * operator....

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

      # Method 1
# def multiply(number):
#     new = 0
#     for i in range(n2):
#         new = new + n1
#         i += 1
#     return new
#
# number1 = multiply(n1)
# print(number1)

#         #Method 2
# new = 0
# for i in range(n2):
#     new = new + n1
#     i += 1
# print(new)

        # Method 3
i = 0
new = 0
while i <n2:
    new = new +n1
    i+=1
print(new)
