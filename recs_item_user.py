from scipy import spatial
import matplotlib.pyplot as plt
import itertools
from sklearn.neighbors import NearestNeighbors

# https://realpython.com/build-recommendation-engine-collaborative-filtering/
# conceptually we can say that these are users with explicit ratings for movies x and y
# or we could say that they're
pts = [
    [4, 1],
    [3.5, 0.5],
    [0.5, 4],
    [1.5, 5]
]

def points(xs):
    return [[x[0] for x in xs],[x[1] for x in xs]]

def plot(xs):
    ps = points(xs)
    plt.plot(ps[0],ps[1], 'ro')
    mx = max([max(ps[0]), max(ps[1])])
    mn = min([min(ps[0]), min(ps[1]), 0])
    plt.axis([mn, mx, mn, mx])

def distances(fn,points):
    return [[i,fn(i[0],i[1])] for i in itertools.combinations(points,2)]

    #return [fn(c,a), fn(b,c), fn(c,d), fn(a,b)]

print(distances(spatial.distance.euclidean,pts))

print(distances(spatial.distance.cosine,pts))

# Lets add a new user who gave movie x a certain rating but hasn't given one for movie y; what rating will she give to movie y?
# Let's say that her rating will be the average of the ratings given by the nearest 2 users for movie y
# TBD
def predicted_rating(x, pts):
    nearest_users = [(abs(x - p[0]), p) for p in pts]
    nearest_users.sort(key=lambda x: x[0])
    nearest_users = nearest_users[0:2]
    print(nearest_users)
    return sum([u[1][1] for u in nearest_users]) / 2

# What are some problems with what we've just done?

# That was an example of
#User-based collaborative filtering:
#Find the users who have similar taste of products as the current user , similarity is based on purchasing behavior of the user, so based on the neighbor purchasing behavior we can recommend items to the current user.



# now let's see if we can try using sklearn's nearest neighbour's library
neigh = NearestNeighbors(n_neighbors=1, metric='euclidean')
neigh.fit(pts)

neigh.kneighbors([[4,1.1]])

neigh.kneighbors([[4,1.1]])

neigh.kneighbors([[5,2]])

neigh.kneighbors([[0,0.25]])
# what's wrong with the result here?

def normalise(x):
    avg = (x[0] + x[1]) / 2
    return [x[0] - avg, x[1] - avg]

neigh = NearestNeighbors(n_neighbors=1)
neigh.fit([normalise(pt) for pt in pts])
neigh.kneighbors([[0.1,0]])

# this also helps us solve another problem; namely, how we use this to make recomendations
# to make a recommendation we have to have a case where the user hasn't actually rated something
# how do we represent that?
# if we have normalised our entries then it can be represented by '0'

#neigh = NearestNeighbors(n_neighbors=2)
#neigh.n_neighbors(1,0)

# TBD
# write a method to predict ratings for a point using NearestNeighbours and normalise
def predicted_rating(x, pts):
    #TBD
    return 0.1








neigh.kneighbors([[1.5,0]])
neigh.kneighbors([[0,1]])

# now we can try to add more dimensions
[
    []
]

#SVD -- model based approach



def dot_product(x,y):
    return x[0] * y[0] + x[1] * y[1]

def normalised_dot_product(x,y):
    return dot_product(normalise(x), normalise(y))

def normalised_euclidean(x,y):
    return spatial.distance.euclidean(normalise(x), normalise(y))


# You can predict that a user’s rating R for an item I will be close to the average of the ratings given to I by the top 5 or top 10 users most similar to U.

# problems with knn
# “popularity bias”, the other is “item cold-start problem”. There will be another limitation, “scalability issue”,


# Item-based collaborative filtering :
# Amazon "Users who viewed  this item also viewed these other items"
# Item-Item Collaborative Filtering: “Users who liked this item also liked …”
# User-Item Collaborative Filtering: “Users who are similar to you also liked

# matrix factorisation
#


# minkowski distance
#print(distances(normalised_dot_product,pts))

#print(distances(normalised_euclidean,pts))

#an = normalise(a)
#bn = normalise(b)
#cn = normalise(c)
#dn = normalise(d)

#collaborative filtering models are two types,

#I.Nearest neighbor

#II.Matrix factorization

pts = [
    [4., 1., None, None],
    [3.5, 0.5, None, 2.],
    [None, None, 3., 4.],
    [0.5, 4., None, None],
    [1.5, 5., None, None]
]

def normalise(xs):
    nxs = list(filter(lambda x: x is not None, xs))
    avg = sum(nxs) / len(nxs)
    return [0.0 if x is None else x - avg for x in xs]

def predicted_rating(x, pts):
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit([normalise(pt) for pt in pts])
    xn = normalise(x)
    kn = neigh.kneighbors([xn])
    return kn
