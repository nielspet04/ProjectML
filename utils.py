import pandas as pd


def load_data():
    data = pd.read_csv('data/hour.csv', sep=',', header=None)
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("data/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
