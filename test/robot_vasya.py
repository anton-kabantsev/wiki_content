x = 8
y = 0
num = 5
while x+num < 93:
    y = y + 1
    a = "шаг "+str(y)+" x =" + str(x) + "+" + str(num) + "=" + str(x + num)
    x = x + num
    print(a)
# print("this is x " + str(x))
# print("this is y " + str(y))
if x < 93:
    print("Нужно еще добавить "+str(93-x))
