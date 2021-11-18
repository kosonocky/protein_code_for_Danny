import os, platform
from filehandling import get_pdbids_from_txt, download_cif_files_from_rcsb
from data_analysis import count_amino_acids




def main():
    working_directory = os.path.dirname(os.path.abspath(__file__))
    txtfile_name = 'pdbids.txt' #
    pdbids_list = get_pdbids_from_txt(directory = working_directory, filename = txtfile_name)
    download_cif_files_from_rcsb(directory = working_directory, name_list= pdbids_list)


if __name__ == "__main__":
    main()