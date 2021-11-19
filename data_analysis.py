import gemmi
import os

def count_amino_acids(name_list, directory):
    """
    This parses the .cif files for the entire provided cif_list using gemmi and returns list of dictionaries (one for each pdbid) keyed with residue names and values of [count,percentage] for unique chains

        Parameters:
            name_list (list): list of strings of pdbids
            directory (str): filepath to working directory

        Returns:
            combined_residue_count_dict (list): list of dicts {key = amino acid letter, values = [count, percentage]}
    
    """
    
    #initialize list variables
    combined_residue_count_dict = []
    
    for i in range(0,len(name_list)):
        model = gemmi.read_structure(os.path.join(directory,'cif_files',f"{name_list[i]}.cif"), merge_chain_parts = True)    #Create model object from read cif file
        polymer_letters=model[0][0].get_polymer().make_one_letter_sequence()    #Obtain letters sequence of polymer chain
        polymer_length=model[0][0].get_polymer().length()   #get length of polymer chain
        residue_count_dict = {} #initialize polymer_count_dictionary

        for i in range(0,polymer_length):
            try:    #try to add to existing dictionary entry
                residue_count_dict[str(polymer_letters[i])] += 1
                
            except: #if no existing entry, create entry and set to 1
                residue_count_dict[str(polymer_letters[i])] = 1

        for k in residue_count_dict:
            #Convert dictionary single value count into a 2-dimension list following [count, percentage]
            residue_count_dict[k] = [residue_count_dict[k], residue_count_dict[k] / polymer_length]
    
        combined_residue_count_dict += [residue_count_dict]     #add new dict to ongoing list   
    return combined_residue_count_dict



