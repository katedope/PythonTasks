t = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
a = set()
g = {}
y = type(g)
u = type(a)
l = []
p = type(l)
h = 0

for i in range(0, len(t)):
    r = type(t[i])
    if r == y or r == u or r == p:
        h = h+1
    else:
        a.add(t[i])
if h == len(t):
    print('folth')

print(a)