def answer(x,k):

    MAX = pow(10,k) - 1

    return (MAX - (MAX % x))

x = 30
k = 3

print(answer(x, k));




