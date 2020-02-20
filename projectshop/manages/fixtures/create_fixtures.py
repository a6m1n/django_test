"""
CreateFixtureOrder - this class dont have field date_close_order. Only
date_create_order!

Need update - all fixtures to one file. (fixtures.json)
Need add to fixtures 4 users.
1) admin
2) boogalter
3) cashier
4) shop assistant

import scripts.creator as mod - if you wont run from terminal and you in this
directories are located. Check the directory in the terminal command:

$ ls

"""
import manages.fixtures.scripts.creator as mod


def main():
    """Func start creation fixture product & order"""
    obj = mod.CreateFixtureProduct()
    obj.create_data()
    print("Product - ", obj.write_to_file("data_products.json"))

    obj = mod.CreateFixtureOrder()
    obj.create_data()
    print("Order - ", obj.write_to_file("data_orders.json"))


if __name__ == "__main__":
    main()
