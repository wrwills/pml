from scipy import spatial
import matplotlib.pyplot as plt

a = [1, 2]
b = [2, 4]
c = [2.5, 4]
d = [4.5, 5]



def points(xs):
    return [[x[0] for x in xs],[x[1] for x in xs]]

def plot(xs):
    ps = points(xs)
    plt.plot(ps[0],ps[1], 'ro')
    mx = max([max(ps[0]), max(ps[1])])
    mn = min([min(ps[0]), min(ps[1]), 0])
    plt.axis([mn, mx, mn, mx])

def distances(fn):
    return [fn(c,a), fn(b,c), fn(c,d), fn(a,b)]

print(distances(spatial.distance.euclidean))

print(distances(spatial.distance.cosine))

def normalise(x):
    avg = (x[0] + x[1]) / 2
    return [x[0] - avg, x[1] - avg]

def dot_product(x,y):
    return x[0] * y[0] + x[1] * y[1]

def normalised_dot_product(x,y):
    return dot_product(normalise(x), normalise(y))

def normalised_euclidean(x,y):
    return spatial.distance.euclidean(normalise(x), normalise(y))

print(distances(normalised_dot_product))

print(distances(normalised_euclidean))

#an = normalise(a)
#bn = normalise(b)
#cn = normalise(c)
#dn = normalise(d)


