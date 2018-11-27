
#split the text files to multiple text files




"""splits a large text file into smaller ones, based on line count

Original is left unmodified.

Resulting text files are stored in the same directory as the original file.

Useful for breaking up text-based logs or blocks of login credentials.

"""

import os
from glob import glob

def split_file(filepath, lines_per_file=1000):
    """splits file at `filepath` into sub-files of length `lines_per_file`
    """
    lpf = lines_per_file
    path, filename = os.path.split(filepath)
    with open(filepath, 'r',encoding="utf8") as r:
        name, ext = os.path.splitext(filename)
        try:
            w = open(os.path.join(path, '{}_{}{}'.format(name, 0, ext)), 'w')
            for i, line in enumerate(r):
                if not i % lpf:
                    #possible enhancement: don't check modulo lpf on each pass
                    #keep a counter variable, and reset on each checkpoint lpf.
                    w.close()
                    filename = os.path.join(path,
                                            '{}_{}{}'.format(name, i, ext))
                    w = open(filename,'w',encoding="utf8")
                w.write(line)
        finally:
            w.close()


# def split_file(filepath,lines=10):
#     path, filename = os.path.split(filepath)
#     basename,ext=os.path.splitext(filename)
# with open(filepath, 'r') as f_in:
#     try:
#         f_out = open(os.path.join(path, '{}_{}{}'.format(basename, 0, ext)), 'w')
# # loop over all lines in the input file, and number them
#     for i, line in enumerate(f_in):
# # every time the current line number can be divided by the
# # wanted number of lines, close the output file and open a
# # new one
#                 if i % lines == 0:
#                     f_out.close()
#                     f_out = open(os.path.join(path, '{}_{}{}'.format(basename, i, ext)), 'w')
# # write the line to the output file
#                 f_out.write(line)
#         finally:
# # close the last output file
#             f_out.close()
#
#
# if __name__ == '__main__':
#     with open('split_file.txt', 'w') as f:
#         for x in range(950):
#             f.write('{}\n'.format(x))
#     split_file('split_file.txt')

def toDel(i):
#to delte the base file
    if os.path.exists(i):
        os.remove(i)
#All file in folder path
folderPath=glob("C:/Users/asojasingarayar/CaseClassification/CaseClassifier/document/*/*.txt")
for i in folderPath:

#Specific file to split
#i="C:/Users/asojasingarayar/CaseClassification/CaseClassifier/document/ABSENCES/file.txt"
    try:
        split_file(i,1000)
    finally:
        toDel(i)



if __name__=='__main__':
    with open('split_file.txt','w') as f:

            f.write('{}\n')
    split_file('split_file.txt')
