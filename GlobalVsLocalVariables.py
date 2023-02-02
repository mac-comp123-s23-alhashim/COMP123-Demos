glo = 1

def fun1(x):
    global glo
    loc = 2
    glo = 100
    return

print(glo)
fun1(10)
print(glo)

