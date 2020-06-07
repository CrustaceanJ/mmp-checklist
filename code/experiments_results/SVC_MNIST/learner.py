import argparse
import numpy as np
from torchvision import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.kernel_approximation import Nystroem
import sys
import os


def main(C, gamma):
    script_path = os.path.realpath(__file__)
    data_path = os.path.join(os.path.split(script_path)[0], 'data')
    train_data = datasets.MNIST(data_path, train=True, download=False)
    test_data = datasets.MNIST(data_path, train=False, download=False) 
    train_X, train_y = train_data.data.numpy(), train_data.targets.numpy()
    test_X, test_y = test_data.data.numpy(), test_data.targets.numpy()
    train_X = train_X.reshape(-1, train_X.shape[1] * train_X.shape[2])
    test_X = test_X.reshape(-1, test_X.shape[1] * test_X.shape[2])

    scaler = MinMaxScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)
    feature_map_nystroem = Nystroem(gamma=gamma,
                                    random_state=23,
                                    n_components=300)
    train_X = feature_map_nystroem.fit_transform(train_X)
    test_X = feature_map_nystroem.transform(test_X)
    svc = LinearSVC(C=C, random_state=23)
    svc.fit(train_X, train_y)
    print(svc.score(test_X, test_y))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gamma', help='RBF Kernel gamma', \
                        default=0.001, type=float)
    parser.add_argument('--C', help='C', \
                        default=1, type=float)
    args = parser.parse_args()
    
    C = args.C
    gamma = args.gamma
    main(C, gamma)