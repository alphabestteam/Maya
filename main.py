from Product import Product
from Costumer import Costumer
from Register import Register

def main():
    while True:
        register_obj = Register()
        costumer_name = input("please enter the costumer's name to begin the groceries' buying:\n")
        costumer_obj = Costumer(costumer_name)
        user_choice = int(input("Please enter:\n1 to add a product\n2 to remove a product\n3 to finish shopping\n"))
        if user_choice == 1:
            product_name, product_units = input("please enter by order the product's name and number of units\n").split(" ")
            if int(product_units) > 0:
                product_obj = Product(product_name)
                costumer_obj.add_product(product_obj, product_units)
                print("action was successful!")
            else:
                print("your input is invalid")       
        elif user_choice == 2:
            delete_name, delete_units = input("please enter by order the product's name and number of units you want to delete \n").split(" ")
            if int(delete_units) > 0:
                product_removed = costumer_obj.remove_product(delete_name, delete_units)
                if product_removed:
                    print("action was successful!")
                else:
                    print("something went wrong\n")  
            else:
                print("your input is invalid")            
        elif user_choice == 3:
            register_obj.checkout_costumer(costumer_obj)
            break
        else:
            print("invalid input\n")
    register_obj.print_summary()

if __name__ == "__main__":
    main()
