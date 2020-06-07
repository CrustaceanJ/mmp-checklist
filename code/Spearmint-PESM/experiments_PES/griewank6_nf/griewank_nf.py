import numpy as np
import math


def griewank_nf(x):
    result = 1 + 1.0/4000 * (x**2).sum() - np.prod(np.cos(x/np.arange(1, x.size + 1)**0.5))
    result = float(result)
    dist = (x ** 2).sum()**.5
    print 'Result = %f' % result
    print 'Dist = %f' % dist
    return result

def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    x = np.array([params['x1'], params['x2'], params['x3'],
                  params['x4'], params['x5'], params['x6']], dtype=np.float)
    return griewank_nf(x)


def true_val():
    return 0.0
def true_sol():
    return {'x1' : 0.0, 'x2' : 0.0, 'x3' : 0.0,
            'x4' : 0.0, 'x5' : 0.0, 'x6' : 0.0}
true_func = main    