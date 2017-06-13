__author__ = 'Guilherme Matsumoto'

from sklearn.utils import tosequence
import time


def dict_to_list(dict):
    aux = []
    keys = list(dict.keys())
    vals = list(dict.values())
    for i in range(len(dict)):
        aux.append([keys[i], vals[i]])
    return aux

def tuple_list_to_list(tup_list):
    aux = []
    for i in range(len(tup_list)):
        aux.append([tup_list[i][0], tup_list[i][1]])
    return aux
    pass

def dict_to_tuple_list(dict):
    aux = []
    list = dict_to_list(dict)
    for i in range(len(list)):
        aux.append((list[i][0], list[i][1]))
    return aux


if __name__ == '__main__':
    aux1 = {'key1': 1.0, 'key2': 2.3, 'key3': 3.5, 'key4': 4.8}
    aux = [('key1', 1.0), ('key2', 2.3), ('key3', 3.5), ('key4', 4.8)]
    #list1 = dict_to_list(aux1)
    #list = tuple_list_to_list(aux)
    #list_to_sequence = tosequence(aux)
    #print(list)
    #print(list1)

    #tuple_list = dict_to_tuple_list(aux1)

    test = tosequence(aux)
    print(test)
    print(test[-1][-1])
    time.sleep(20)

    #print(tuple_list)