import scripts.creator as mod

if __name__ == '__main__':
    obj = mod.CreateFixtureProduct()
    obj.create_data()
    print('Product - ' ,obj.write_to_file())

    obj = mod.CreateFixtureOrder()
    obj.create_data()
    print('Order - ' ,obj.write_to_file())

# CreateFixtureOrder - this class dont have field date_close_order. Only date_create_order!
