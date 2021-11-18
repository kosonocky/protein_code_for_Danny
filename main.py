import os, platform
from filehandling import get_pdbids_from_txt




def main():
    working_directory = os.path.dirname(os.path.abspath(__file__))
    txtfile_name = 'pdbids.txt'
    pdbids_list = get_pdbids_from_txt(filelocation = working_directory, filename = txtfile_name)
    


if __name__ == "__main__":
    main()