import os
import wget

def get_pdbids_from_txt(filename, directory):
    """
    Takes .txt file located at specified directory and returns list of pdbids

        Parameters:
            filename (str): txt file contiaining pdbids; 'pdbids.txt'
            directory (str): filepath to where 'pdbids.txt' file is located
       
        Returns:
            pdbid_list (list): list of strings of pdbids
    """
    
    try:
        with open(os.path.join(directory,filename), "r") as pdbid_txt:
            pdbid_list = pdbid_txt.read().splitlines()  #Read .txt file and ignore the linebreaks
        return pdbid_list
    except Exception as error:
        print(error)
        print("Are you sure the filename you specified exists?")


def download_cif_files_from_rcsb(name_list, directory):
    """
    Takes list of pdbids and current directory, and uses wget module to download cif files into 'cif_files' folder located in working directory
    
        Parameters:
            name_list (list): list of strings of pdbids
            directory (str): filepath to working directory

    """

    #Create cif_files folder in working directory if not exists
    if not os.path.exists(os.path.join(directory, 'cif_files')):
        os.makedirs(os.path.join(directory,'cif_files'))

    try:
        print("Downloading...")
        for i in range(0,len(name_list)):  
            url = f"https://files.rcsb.org/download/{name_list[i]}.cif" #make url string from list
            cif_directory_path = os.path.join(directory, 'cif_files')   #make output path into cif_files folder within working directory
            if not os.path.exists(f"{os.path.join(cif_directory_path,name_list[i])}.cif"):  #Ensures no duplicate downloads
                wget.download(url, out=cif_directory_path)  #Download cif files from list
        print("Download Complete")
    except Exception as error:
        print(error)

