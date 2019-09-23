class Machine:
    def __init__(self, type, power):
        self.type = type
        self.power = power

    def get_machine_details(self):
        return 'Type: {}\t Power:{}\t'.format(self.type, self.power)


class Devices:
    def __init__(self, brand):
        self.brand = brand

    def get_device_details(self):
        return 'Brand: {}'.format(self.brand)


class Laptop(Machine, Devices):
    def __init__(self, ram, storage_capacity):
        self.ram = ram
        self.storage_capacity = storage_capacity
        Machine.__init__(self, 'Electronic', 'Electric')
        Devices.__init__(self, 'Lenovo')

    def get_laptop(self):
        return 'Ram: {}\t Storage: {}'.format(self.ram, self.storage_capacity)


class Bike(Machine, Devices):
    def __init__(self, engine_capacity, color):
        self.engine_capacity = engine_capacity
        self.color = color
        Machine.__init__(self, 'Machanical', 'Petrol')
        Devices.__init__(self, 'KTM')

    def bike_details(self):
        return 'Engine type: {}\t Color: {}'.format(self.engine_capacity, self.color)


lenovo = Laptop('16GB', '1TB')
print(lenovo.get_laptop())
print(lenovo.get_device_details())
print(lenovo.get_machine_details())
print()
print()
ktm = Bike('1000BHP', 'Black')
print(ktm.bike_details())
print(ktm.get_device_details())
print(ktm.get_machine_details())