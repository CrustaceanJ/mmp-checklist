import numpy as np
import math

def rosenbrock_noisy(x, y):
    result = 100*(y - x**2)**2 + (x - 1)**2
    result = float(result)

    now = np.array([x, y], dtype=np.float)
    point1 = np.array([1, 1], dtype=np.float)
    dist = ((point1 - now)**2).sum()**.5
    noise = np.random.normal() * 0.1
    print 'Result = %f, noise %f, total %f' % (result, noise, result+noise)
    print 'Dist = %f' % dist
    return result + noise


# Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return rosenbrock_noisy(params['x'], params['y'])