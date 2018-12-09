from time import perf_counter,sleep

#class NegativeDelayError
def time_it(func):
    def time_it_handler(*args):
        ts=perf_counter()
        value=func(*args)
        print('elapsed time:',perf_counter()-ts)
        return value
    return time_it_handler



class Custom:
    @time_it
    def execute(self,delay):
        if delay<0:
            pass
        sleep(delay)

if __name__=='__main__':
    c=Custom()
    c.execute(3)
    print()
    print(c)
