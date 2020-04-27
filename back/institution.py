

class Institution:

    def __init__(self):
        self.id = None
        self.address = None
        self.benefit = None
        self.car_park = None
        self.locality = None
        self.phone = None
        self.place = None
        self.provider = None
        self.regon = None
        self.is_fav = False

    def p_print(self):
        print('************** institution **************')
        print(self.id)
        print(self.address)
        print(self.benefit)
        print(self.car_park)
        print(self.locality)
        print(self.phone)
        print(self.place)
        print(self.provider)
        print(self.regon)
        print()
