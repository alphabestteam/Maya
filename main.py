from Product import Product
from Costumer import Costumer
from Register import Register

def main():
    register_obj = Register()
    costumer_name = input("please enter the costumer's name to begin the groceries' buying:\n")
    costumer_obj = Costumer(costumer_name)
    while True:
        user_choice = int(input("Please enter:\n1 to add a product\n2 to remove a product\n3 to finish shopping\n"))
        if user_choice == 1:
            product_name, product_units = input("please enter by order the product's name and number of units\n").split(" ")
            if int(product_units) > 0:
                product_obj = Product(product_name)
                costumer_obj.add_product(product_obj, int(product_units))
                print("action was successful!")
            else:
                print("your input is invalid")       
        elif user_choice == 2:
            delete_name, delete_units = input("please enter by order the product's name and number of units you want to delete \n").split(" ")
            if int(delete_units) > 0:
                product_removed = costumer_obj.remove_product(delete_name, int(delete_units))
                if product_removed:
                    print("action was successful!")
                else:
                    print("something went wrong\n")  
            else:
                print("your input is invalid")            
        elif user_choice == 3:
            register_obj.checkout_costumer(costumer_obj)
            print("Thank you for shopping! We will love to see you next time!\n")
            change_costumer = input("Please enter yes in order for a new costumer to pay, or anything else to close the cash register\n")
            if change_costumer == "yes":
                costumer_name = input("please enter the costumer's name to begin the groceries' buying:\n")
                costumer_obj = Costumer(costumer_name)
                continue
            else:
                break
        else:
            print("invalid input\n")
    print(register_obj.print_summary())

if __name__ == "__main__":
    main()
