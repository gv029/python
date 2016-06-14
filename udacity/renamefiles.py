import os

#get names from folder
#rename file from folder
def renamefiles():
    file_list = os.listdir("/home/boludo29/Documents/python2.7/udacity/prank/prank")
    os.chdir("/home/boludo29/Documents/python2.7/udacity/prank/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
        

renamefiles()
