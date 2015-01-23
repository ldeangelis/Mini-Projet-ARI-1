__author__ = 'Koorge'

def jeSaisPas(n, m, op, k):
    if op == 1:
        x = n + ((1 / k) * m)
        return x
    else:
        x = k * (m - n)
        return x

def tengenToppaGurrenLagann(op, k, tuple1, tuple2):
    position = 0
    solution = []
    for i in range(3):
        temp = jeSaisPas(op, k, tuple1[position], tuple2[position])
        solution.append(temp)
        position += 1

    solution = tuple(solution)
    return solution
