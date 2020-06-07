import numpy as np
import math
import subprocess


def learn_svm(C, gamma):
    command = ['../../../experiments_results/SVC_MNIST/learn.sh',
               '--gamma', str(float(gamma)), '--C', str(float(C))]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    # p = subprocess.Popen(['../../../experiments_results/SVC_MNIST/test.sh'],
    #                      stdout=subprocess.PIPE)
    result, _ = p.communicate()
    result = float(result)
    print 'Result = %f' % result
    return -result

def main(job_id, params):
    print 'Anything printed here will end up in the output directory for job #%d' % job_id
    print params
    return learn_svm(params['C'], params['gamma'])
