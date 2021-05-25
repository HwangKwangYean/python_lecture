def sum_nums(*args):
    result=0
    for n in args:
        result +=n
    return result
print(sum_nums(10,20,30))
print(sum_nums(10,20,30,40,50))