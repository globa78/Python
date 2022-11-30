a = [ 1, 2,3,5,8,15,23,38]
def f(i):
    return i**2
b = [(i, f(i)) for i in a if i%2==0]
print(b)