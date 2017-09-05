t = [1,2,3,4,5,6,7,8,9,0]
r = list(map(lambda x: x*x, t))
print(r)


r = list(filter(lambda x: x%2 is 0, t))
print(r)
