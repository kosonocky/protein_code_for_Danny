


def get_pdbids_from_txt(filename, filelocation):
    with open(f"{filelocation}\{filename}", "r") as pdbid_txt: 
        pdbid_list = pdbid_txt.readlines()
    return pdbid_list

