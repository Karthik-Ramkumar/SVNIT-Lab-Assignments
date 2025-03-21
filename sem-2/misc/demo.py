'''a = [1,2,3,4,5]
a = iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a)) 

items = [1,2,3,4,5]
list_iter = iter(items)
try:
    x = next(list_iter)
    while x:
        print(x)
        x = next(list_iter)
except StopIteration:
    print('Exhausted the generator') 

# ---------------------
class multiplier:
    def __init__(self, n,max):
        self.multi = n
        self.start = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.max :
            temp = self.start
            self.start += 1
            return temp * self.multi
        else:
            raise StopIteration
obj = multiplier(6,10)
iterator = iter(obj)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("iterators is exhausted")    '''
# ---------------------
def multi(n,max):
    start = 1
    while start <= max:
        yield start * n
        start += 1

multi(4,5)



