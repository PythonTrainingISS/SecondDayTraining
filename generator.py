def demo():
    print('before1')
    return 12
    print('after1')

    print('before2')
    return 12.21
    print('after2')

    print('before3')
    return 'pam'
    print('after3')

def demo2():
    print('before1')
    yield 12
    print('after1')

    print('before2')
    yield 12.21
    print('after2')

    print('before3')
    yield 'pam'
    print('after3')

print(demo())
g= demo2()
print(next(g))
print('-'*22)
print(next(g))
print('-'*22)
print(next(g))
print('-'*22)

def get_integers():
    i=1

    while True:
        yield i
        i+=1
