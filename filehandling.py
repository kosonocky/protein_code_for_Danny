import os
import wget

def get_pdbids_from_txt(filename, directory):
    try:
        with open(os.path.join(directory,filename), "r") as pdbid_txt:
            pdbid_list = pdbid_txt.read().splitlines()  #Read .txt file and ignore the linebreaks
        return pdbid_list
    except Exception as error:
        print(error)#
        print("Are you sure the filename you specified exists?")


def download_cif_files_from_rcsb(name_list, directory):
    try:
        for i in range(0,len(name_list)):
            url = f"https://files.rcsb.org/download/{name_list[i]}.cif" #make url string from list
            cif_directory_path = os.path.join(directory, 'cif_files')   #make output path into cif_files folder within working directory
            if not os.path.exists(f"{os.path.join(cif_directory_path,name_list[i])}.cif"):  #Ensures no duplicate downloads
                wget.download(url, out=cif_directory_path)  #Download cif files from list
    except Exception as error:
        print(error)

