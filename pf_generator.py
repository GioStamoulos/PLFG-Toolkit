import pandas as pd
import sys
import os

def separator(data, start, stop):
  MJ = data.iloc[:,start:stop]
  MJ.columns = MJ.iloc[0,:]
  MJ = MJ.drop([0], axis=0)
  MJ["ID"].iloc[1]
  return MJ

def EC_check(EC):
  try:
    EC = EC.split('.')
    if len(EC)==4:
      if (int(EC[0])<=7 and int(EC[0])>=1):
        return True
      else:
        return False
    else:
      return False
  except:
    return False


def Tie2_filler(MJ21_row, MJ5_row, nf, pathologic_headers, row_index, file):
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
        print(MJ5_row['EC'][i])
        # EC syntax checker 
        if EC_check(MJ5_row['EC'][i]):
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

def main():
    file = str(input('Give csv path: '))
    replicon = str(input('Give replicon name: '))
    # preprocessing csv
    data= pd.read_csv(file)
    data = data.fillna(' ')
    MJ5 = separator(data, 1, 6)
    MJ21 = separator(data, 8, 16)

    pathologic_headers = ['ID', 'ACCESSION-2', 'NAME', 'SYNONYM',f'REPLICON\t{replicon}', 
                              'STARTBASE', 'ENDBASE','PRODUCT-TYPE', 'FUNCTION', 'EC']
    with open('./Tier2.pf', 'w') as nf:
        for i in range(len(MJ21)):
        #check if current ID is the same with previous 
            if MJ21.iloc[i-1]['ID']!=MJ21.iloc[i]['ID']:
                Tie2_filler(MJ21.iloc[i], MJ5.iloc[i], nf, pathologic_headers, i, nf)
            else:
                pass


if __name__ == "__main__":
    main()
