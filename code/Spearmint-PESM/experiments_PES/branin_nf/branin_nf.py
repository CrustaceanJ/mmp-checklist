import numpy as np
import math

def branin_nf(x, y):

    result = np.square(y - (5.1/(4*np.square(math.pi)))*np.square(x) + 
         (5/math.pi)*x - 6) + 10*(1-(1./(8*math.pi)))*np.cos(x) + 10
    
    result = float(result)
    now = np.array([x, y], dtype=np.float)
    point1 = np.array([-np.pi, 12.275], dtype=np.float)
    point2 = np.array([np.pi, 2.275], dtype=np.float)
    point3 = np.array([9.42478, 2.475], dtype=np.float)
    dist = min(((point1 - now)**2).sum()**.5, ((point2 - now)**2).sum()**.5)
    dist = min(dist, ((point3 - now)**2).sum()**.5)
    print('Result = %f' % result)
    print('Dist = %f' % dist)
    return result

# Write a function like this called 'main'
def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return branin_nf(params['x'], params['y'])
