items = [12,3,4,2,1,3]
print(iter(items))

li=iter(items)
print(next(li))
print(next(li))
print(next(li))
print(next(li))

#generators(custom iter)
"""
        expressin 
        function
"""

g=((oct(item),hex(item),bin(item)) for item in range(3))
print(g)

for element in g:
    print(element)








