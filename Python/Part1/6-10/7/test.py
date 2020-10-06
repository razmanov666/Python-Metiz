def persistence(n):
    i = 0 #len(str(n))
    mul = 1
    #print (type(len(str(n))))
    #length = len(str(n))
    while i < 5:
        i += 1
        n = list(str(n))
        for num in n:
            mul *= int(num)
    return i

print (persistence(123))
# k = 103
# print (list(str(k))[0])