import os
from filehandling import get_pdbids_from_txt, download_cif_files_from_rcsb
from data_analysis import count_amino_acids
from display import plot_residues_count, plot_residues_percentages




def main():
    working_directory = os.path.dirname(os.path.abspath(__file__))
    txtfile_name = 'pdbids.txt' #change name if using different txt file

    #get list of pdbids from provided txt file
    pdbids_list = get_pdbids_from_txt(directory = working_directory, filename = txtfile_name)

    #download cif files from rcsb using pdbids list
    download_cif_files_from_rcsb(directory = working_directory, name_list= pdbids_list)

    #on each unique chain, count residues & percentages of residues
    residue_counts = count_amino_acids(name_list = pdbids_list, directory = working_directory)

    #Loop structure that allows choice of which graph to check within command prompt.  Kept this simple with terminal i/o
    choice_complete = False
    while choice_complete == False:
        print("PDB IDs Provided: ")
        print(pdbids_list)
        inputted_name = input("Input PDB ID that you want to view (enter 'escape' to exit): \n")
        if inputted_name != "escape": #if not nothing entered, try to make plot associated with entry
            plot_residues_count(residues_dict_list = residue_counts, pdbids_list = pdbids_list, inputted_name = inputted_name)
            plot_residues_percentages(residues_dict_list = residue_counts, pdbids_list = pdbids_list, inputted_name = inputted_name)
        else:
            choice_complete = True  #if nothing entered, exit
    


if __name__ == "__main__":
    main()