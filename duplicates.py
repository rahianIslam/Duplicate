import os
import hash_functions as hfcs
import dir_functions as dfcs

def get_hash(filename):
    fin = open(filename, 'rb')
    message = fin.read()
    return hfcs.hash8(message, hfcs.create_table())


def get_all_hashes(dirname):
    
    file_names = dfcs.walk(dirname)
    
    d = {}

    for name in file_names:

        h = get_hash(name)

        if h in d:
            d[h].append(name)
        else:
            d[h] = [name]
    return d

def print_duplicates(hash_dict):

    for h, names in hash_dict.items():
        if len(names)>1:
            print("These files have the same hash:")
            for name in names:
                print(f"\t{name}")


dirname = 'files/'

file_hashes = get_all_hashes(dirname)
print_duplicates(file_hashes) 