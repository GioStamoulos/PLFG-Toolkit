import pandas as pd


# xlsx files that contain ";" might lead to wrong csv conversion.
# Thus, replace ";" with "/" or another symbol

class preprocessing:
    
    def __init__(self, file_path, output_csv_name, product_type):  
        self.file_path = file_path
        self.product_type = product_type
        self.output_csv_name = output_csv_name

    def xlsx_to_csv(self):
        data_xlsx = pd.read_excel(f'{self.file_path}', index_col=None)
        data_xlsx.to_csv(f'{self.output_csv_name}', encoding='utf-8', index=False)
        

    def add_product_type(self):
        data= pd.read_csv(f'{self.output_csv_name}')
        with open(f'{self.product_type}', 'r') as f:
            a = f.readlines()
            f.close
        df = {'ID':[], 'PD':[]}
        for i in a:
            if ('ID' in i) == True:
                df['ID'].append(i[3:-1])
            elif ('PRODUCT-TYPE' in i) == True:
                df['PD'].append(i[13:-1])
            else:
                 pass
        data['Unnamed: 14'][0] = 'Product Type'
        for i in range(1,len(data['MJ_biocyc'])):
            try:
                index_type = df['ID'].index(data['MJ_biocyc'][i])
                data['Unnamed: 14'][i] = df['PD'][index_type]
            except:
                print(data['MJ_biocyc'][i])
                pass
        data.to_csv(f'{self.output_csv_name}',index=False)

