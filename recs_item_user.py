from scipy import spatial
a = [1, 2]
b = [2, 4]
c = [2.5, 4]
d = [4.5, 5]

def distances(fn):
    return [fn(c,a), fn(b,c), fn(c,d), fn(a,b)]

print(distances(spatial.distance.euclidean))

print(distances(spatial.distance.cosine))
