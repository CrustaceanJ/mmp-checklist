import numpy as np
import math


def hump_noisy(x, y):

    result = (4 - 2.1*x**2 + x**4/3)*x**2 + x*y + (-4 + 4*y**2)*y**2
    
    result = float(result)
    now = np.array([x, y], dtype=np.float)
    point1 = np.array([0.0898, -0.7126], dtype=np.float)
    point2 = np.array([-0.0898, 0.7126], dtype=np.float)
    dist = min(((point1 - now)**2).sum()**.5, ((point2 - now)**2).sum()**.5)
    noise = np.random.normal() * 0.1
    
    print 'Result = %f, noise %f, total %f' % (result, noise, result+noise)
    print 'Dist = %f' % dist
    return result + noise


# Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return hump_noisy(params['x'], params['y'])

