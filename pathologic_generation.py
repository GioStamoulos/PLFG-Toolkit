import pandas as pd
import sys
import os
from EC_Validation import *

class pathologic_generation:

    def separator(self, data, start, stop):
        MJ = data.iloc[:,start:stop]
        MJ.columns = MJ.iloc[0,:]
        MJ = MJ.drop([0], axis=0)
        MJ["ID"].iloc[1]
        return MJ

    def Tie2_filler(self, MJ21_row, MJ5_row, nf, pathologic_headers, row_index, file):
        if (MJ21_row['ID']!= '-'):
    #write ID and ACCESSION-2
            nf.write('{0}\t{1}\n'.format(pathologic_headers[0], MJ21_row['ID']))
            nf.write('{0}\t{1}\n'.format(pathologic_headers[1],MJ21_row['ID']))
    #write NAME if exists
            if MJ21_row['NAME'] != ' ':
                nf.write('{0}\t{1}\n'.format(pathologic_headers[2], MJ21_row['NAME']))
            else:
                pass
    #write SYNONYM
            nf.write('{0}\t{1}\n'.format(pathologic_headers[3], MJ21_row['ID'][3:]))
    #write SYNONYM from MJ2005 if exists
            if MJ5_row['ID']!= '-':
                nf.write('{0}\t{1}\n'.format(pathologic_headers[3], MJ5_row['ID']))
            else:
                pass
    #write REPLICON
            nf.write('{}\n'.format(pathologic_headers[4]))
    #write STARTBASE & ENDBASE & Product type
            nf.write('{}\t{}\n'.format(pathologic_headers[5], MJ21_row['start']))
            nf.write('{}\t{}\n'.format(pathologic_headers[6], MJ21_row['end']))
            nf.write('{}\t{}\n'.format(pathologic_headers[7], MJ21_row['Product Type']))
    #write fuction
            nf.write('{0}\t{1}\n'.format(pathologic_headers[8],MJ21_row['description']))
    # write EC number if exists
            if  MJ5_row['EC']!= ' ':
    # write more than one EC numbers if exists
                MJ5_row['EC'] = MJ5_row['EC'].split('/')
                for i in range(len(MJ5_row['EC'])):
                    ec = EC_Validation(MJ5_row['EC'][i])
    # EC syntax checker 
                    if ec.EC_check():
                        nf.write('{0}\t{1}\n'.format(pathologic_headers[9], MJ5_row['EC'][i].encode("utf-8")))
                    else:
        # delete temporary Tier2 file
                        file.close()
                        os.remove("./Tier2.pf")
        # break - error message
                        sys.exit(f"Wrong syntax of EC number in row {row_index+3}")    
            else:
                pass
            nf.write('//\n')
        else:
            pass