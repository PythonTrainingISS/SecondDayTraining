
def get_integers():
    i=1

    while True:
        yield i
        i+=1

squares = (i**2 for i in get_integers())

def take_n(count,seq):
    for element in range(count):
        yield next(seq)

if __name__=='__main__':
    for value in take_n(5,squares):
        print(value)