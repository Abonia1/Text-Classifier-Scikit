import errno
import os
from fsplit.filesplit import FileSplit

fs = FileSplit(file="C:Users/asojasingarayar/CaseClassification/CaseClassifier/FORMATION/file.txt", splitsize=100000,output_dir="C:Users/asojasingarayar/CaseClassification/CaseClassifier/FORMATION/")
fs.split()


raise FileNotFoundError(
    errno.ENOENT, os.strerror(errno.ENOENT), filename)
