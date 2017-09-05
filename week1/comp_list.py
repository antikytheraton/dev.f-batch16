i = [1,2,3,4,5,6,7,8,9]
u = [[1,2,3],[4,5,6],[7,8]]

e = [j for i in u for j in i]

f = [j for j in u if len(j) > 2]

g = [j if len(j) > 2 else 'nope' for j in u]

print(u)
print(e)
print(f)
print(g)
