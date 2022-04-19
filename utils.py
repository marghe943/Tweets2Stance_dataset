import pickle

def save_pickle(obj, path, filename):
    with open(path + filename + '.pkl', 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_pickle(path, filename):
    with open(path + filename + '.pkl', 'rb') as input:
        obj= pickle.load(input)
        return obj


# raw dataset, not preprocessed.
D3 = load_pickle('./', 'IT_D3')
D4 = load_pickle('./', 'IT_D4')
D5 = load_pickle('./', 'IT_D5')
D7 = load_pickle('./', 'IT_D7')
