class A:
    vc = 234
    def __init__(self):
        vc = 456    
a = A()
b = A()
a.vc = 432
print(a.vc)
print(b.vc)
print(A.vc)