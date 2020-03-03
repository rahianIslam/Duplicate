import os
import hash_functions as hfcs
import dir_functions as dfcs
import argparse

dirname = 'files/'



def get_hash(filename):
    """ Obtains a file and assigns the contents of the file to a value known as hash value
    Input : A text file 
    Output: A value using the md5 hashing function 
    """

    fin = open(filename, 'rb')
    message = fin.read()
    return hfcs.hash8(message, hfcs.create_table())


def get_all_hashes(dirname):
    """Organize and obtain hash via the files within 
    the dir by creating a dictionary and giving them hash values.
    Input : string containing the address of the directory
    Output: dictionary containg key = hash , value = file name.
    """
    
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
    """
    """

    for h, names in hash_dict.items():     

        if len(names)>1:
            print("These files have the same hash:")
            for name in names:
                print(f"\t{name}")




#argparse for commandline interface
parser = argparse.ArgumentParser(description = 'Find copies of same files')
parser.add_argument('dirname', help = 'Program to find duplicate files')
# parser.add_argument('-e','--extension', help ='')
args = parser.parse_args()




file_hashes = hfcs.hashmd5(args.dirname)
print_duplicates(file_hashes) 
print(file_hashes)