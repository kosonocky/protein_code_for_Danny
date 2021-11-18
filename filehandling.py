import os


def get_pdbids_from_txt(filename, filelocation):
    try:
        with open(os.path.join(filelocation,filename), "r") as pdbid_txt: 
            pdbid_list = pdbid_txt.readlines()
        return pdbid_list
    except:
        print("Are you sure the filename you specified exists?")
