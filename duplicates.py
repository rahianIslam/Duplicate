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
    return hfcs.hashmd5(message)


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

def print_duplicates(hash_dict,extension):
    """ Prints all the duplicate files takiing into consideration 
    which file or directory has been asked for in the 
    command interface 
    """
    

    if extension == '.pdf':
        for h, names in hash_dict.items():     
            if len(names)>1 and any('.pdf' in name for name in names):
                print("These files have the same hash:")
                for name in names:
                    print(f"\t{name}")

    
    elif extension == '.txt':
        for h, names in hash_dict.items():     
            if len(names)>1 and any('.txt' in name for name in names):
                print("These files have the same hash:")
                for name in names:
                    print(f"\t{name}")

    elif extension != '.pdf' or '.txt':
        for h, names in hash_dict.items():     
            if len(names)>1:
                print("These files have the same hash:")
                for name in names:
                    print(f"\t{name}")
                        
        
#argparse for commandline interface

parser = argparse.ArgumentParser(description = 'Find copies of same files')
parser.add_argument('dirname', help = 'Program to find duplicate files')
parser.add_argument('-e','--extension', help ='This allows the user to chose files and find duplicates only in that file')
args = parser.parse_args()


# assigning all the hashed files to file_hashes
file_hashes = get_all_hashes(dirname)

#using the print functon to print the duplicate files based on the input
print_duplicates(file_hashes,args.extension)

