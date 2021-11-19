import matplotlib.pyplot as plt
import numpy as np

def plot_residues_count(residues_dict_list, pdbids_list, inputted_name):    
    """
    Plots residue counts on simple bar chart based on selected pdbid

        Parameters:
            residues_dict_list (list): list of dicts {key = amino acid letter, values = [count, percentage]}
            pdbids_list (list): list of pdbids
            inputted_name (str): pdbid selected to plot
    """
    for i in range(0,len(residues_dict_list)): 
        if inputted_name == pdbids_list[i]: #align correct data
            labels = [*residues_dict_list[i]]    #get amino acid labels
            
            residue_data = []
            for j in range(0,len(labels)):  #get data into simple list format
                residue_data += [residues_dict_list[i][labels[j]][0]]

            x = np.arange(len(labels))
            width = 0.35
            fig, ax = plt.subplots()
            rects1 = ax.bar(x, residue_data, width, label = 'Counts')
            ax.set_ylabel('Counts')
            ax.set_title(f'Amino Acid Counts for {pdbids_list[i]}')
            ax.set_xticks(x, labels)
            ax.legend()
            ax.bar_label(rects1, padding=3)
            fig.tight_layout()
            plt.ion()
            plt.show(block=False)
    


def plot_residues_percentages(residues_dict_list, pdbids_list, inputted_name):
    """
    Plots residue percentages on simple bar chart based on selected pdbid

    Parameters:
        residues_dict_list (list): list of dicts {key = amino acid letter, values = [count, percentage]}
        pdbids_list (list): list of pdbids
        inputted_name (str): pdbid selected to plot
    
    """    
    for i in range(0,len(residues_dict_list)):
        if inputted_name == pdbids_list[i]: #align correct data
            labels = [*residues_dict_list[i]]    #get amino acid labels
            
            residue_data = []
            for j in range(0,len(labels)):  #get data into simple list format
                residue_data += [residues_dict_list[i][labels[j]][1] * 100]

            x = np.arange(len(labels))
            width = 0.35
            fig, ax = plt.subplots()
            rects1 = ax.bar(x, residue_data, width, label = 'Percentages')
            ax.set_ylabel('Percentages')
            ax.set_title(f'Amino Acid Percentages for {pdbids_list[i]}')
            ax.set_xticks(x, labels)
            ax.legend()
            ax.bar_label(rects1, padding=3)
            fig.tight_layout()
            plt.ion()
            plt.show(block=False)