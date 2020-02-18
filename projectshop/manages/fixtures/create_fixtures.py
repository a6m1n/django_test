"""
CreateFixtureOrder - this class dont have field date_close_order. Only
date_create_order!

Need update - all fixtures to one file. (fixtures.json)
Need add to fixtures 4 users.
1) admin
2) boogalter
3) cashier
4) shop assistant
"""
import scripts.creator as mod

if __name__ == "__main__":
    OBJ = mod.CreateFixtureProduct()
    OBJ.create_data()
    print("Product - ", OBJ.write_to_file())

    OBJ = mod.CreateFixtureOrder()
    OBJ.create_data()
    print("Order - ", OBJ.write_to_file())
