# this file will demonstrate read write and change product catalog
# the field catalog structure is product_id, product_name,product_quantety, product_price
import csv


def save_to_csv_file(catalog=dict(), file_name="catalog.csv"):
    handler = open(file_name,'w',newline="")
    data = csv.writer(handler)
    for i in catalog:
        ans=[i]+catalog[i]
        data.writerow(ans)
    handler.close()
    catalog=read_from_csv_file()
    return catalog

def read_from_csv_file(file_name="catalog.csv"):
    try:
        handler = open(file_name,'r')
    except IOError:
        return dict()
    csv_handler = csv.reader(handler)
    ans = dict()
    for record in csv_handler:
        ans[record[0]] =record[1:]
    handler.close()
    return ans

def add_record(catalog):
    prod_id = input("Enter product id: ")
    if prod_id in catalog:
        raise Exception("product in catalog can't add")
    prod_name = input("Enter product name: ")
    prod_quant = int(input("Enter product quantity: "))
    prod_price = int(input("Enter product price: "))
    catalog[prod_id]=[prod_name,prod_quant,prod_price]
    catalog =  save_to_csv_file(catalog)
    return catalog

def change_record(catalog):
    prod_id = input("Enter product id: ")
    if prod_id not in catalog:
        raise Exception("product not in catalog can't change")
    print(catalog[prod_id])
    prod_name = input("Enter product name: ")
    prod_quant = int(input("Enter product quantity: "))
    prod_price = int(input("Enter product price: "))
    catalog[prod_id] = [prod_name, prod_quant, prod_price]
    catalog = save_to_csv_file(catalog)
    return catalog

def display_catalog(catalog):
    if len(catalog)==0:
        print("Catalog empty")
        return
    for i in catalog:
        print("{}:\t{}\t{}\t{}\t".format(i, catalog[i][0], catalog[i][1], catalog[i][2]))


def display_menu():
    res="Main Menu\n"
    res += '*'*10
    res += "\n1.\tdisplay catalog \n2.\tadd to catalog\n3.\tchange record\n0.\tExit"
    print(res)

def get_input():
    try:
        ans = int(input("Enter your choice: "))
    except ValueError as e:
        print("input error try again")
        return get_input()
    return ans


def main():
    catalog = read_from_csv_file()
    while True:
        display_menu()
        choice = get_input()
        if choice == 0:
            print("Bye Bye !")
            break
        elif choice==1:
            display_catalog(catalog)
        elif choice==2:
            try:
                catalog = add_record(catalog)
            except Exception:
                print("INPUT ERROR!!! ")
        elif choice==3:
            catalog = change_record(catalog)

if __name__ == '__main__':
    main()
