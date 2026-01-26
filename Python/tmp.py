s = "aacc"
t = "cacc"

store = set()
lst = set(s)
lts = set(t)

if len(t) != len(s):
    print(False)


for i in lst:
    if i in lts:
        store.add(i)

print(lst == store)
