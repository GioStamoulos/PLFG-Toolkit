from pathologic_generation import *

def main():
    pf = pathologic_generation()
    file = str(input('Give csv path: '))
    replicon = str(input('Give replicon name: '))
    # preprocessing csv
    data= pd.read_csv(file)
    data = data.fillna(' ')
    MJ5 = pf.separator(data, 1, 6)
    MJ21 = pf.separator(data, 8, 16)

    pathologic_headers = ['ID', 'ACCESSION-2', 'NAME', 'SYNONYM',f'REPLICON\t{replicon}', 
                              'STARTBASE', 'ENDBASE','PRODUCT-TYPE', 'FUNCTION', 'EC']
    with open('./Tier2.pf', 'w') as nf:
        for i in range(len(MJ21)):
        #check if current ID is the same with previous 
            if MJ21.iloc[i-1]['ID']!=MJ21.iloc[i]['ID']:
                pf.Tie2_filler(MJ21.iloc[i], MJ5.iloc[i], nf, pathologic_headers, i, nf)
            else:
                pass


if __name__ == "__main__":
    main()