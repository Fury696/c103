import os
import shutil
fpath = "C:/Users/tharu/Downloads"
tpath = "C:/Users/tharu/Downloads/docs"
lfiles = os.listdir(fpath)
for fname in lfiles:
    n,ext = os.path.splitext(fname)
    if ext == "":
        continue
    if ext in [".pdf",".txt",".dat",".csv",".docx",".json"]:
        p1 = fpath + "/" + fname
        p2 = tpath + "/" + "Document Files"
        p3 = tpath + "/" + "Document Files" + "/" + fname
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)
