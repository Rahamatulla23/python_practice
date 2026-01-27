words="the quick brown fox jump over the lazy dog".split()
l=[[w.upper(),len(w)] for w in words]
print(l)