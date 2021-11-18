import os, platform
from filehandling import get_pdbids_from_txt, download_cif_files_from_rcsb
from data_analysis import count_amino_acids
from display import plot_residues_count, plot_residues_percentages




def main():
    working_directory = os.path.dirname(os.path.abspath(__file__))
    txtfile_name = 'pdbids.txt'
    pdbids_list = get_pdbids_from_txt(directory = working_directory, filename = txtfile_name)
    download_cif_files_from_rcsb(directory = working_directory, name_list= pdbids_list)
    
    residue_counts = []
    residue_counts = count_amino_acids(cif_list = pdbids_list, directory = working_directory)

    choice_complete = False
    while choice_complete == False:
        print("PDB IDs Provided: \n")
        print(pdbids_list)

        inputted_name = input("Input PDB ID that you want to view: \n")
        plot_residues_count(residue_counts, pdbids_list, inputted_name)
        plot_residues_percentages(residue_counts, pdbids_list, inputted_name)

        exit_plots = input("View another plot? (y/n)\n")
        if exit_plots != 'y':
            choice_complete = True
    


if __name__ == "__main__":
    main()