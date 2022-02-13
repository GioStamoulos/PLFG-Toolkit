from preprocessing import *

def main():
    
    print('Give inputs\n')
    file_path, output_csv_name, product_type = input().split()
    pre = preprocessing(file_path, output_csv_name, product_type)
    pre.xlsx_to_csv()
    pre.add_product_type()



if __name__ == "__main__":
    main()