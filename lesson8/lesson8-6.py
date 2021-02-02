class TypeError(Exception):
    @classmethod
    def check_type(cls, obj, true_data):
        if type(obj) == type(true_data):
            return True
        else:
            print('Неверный тип атрибута!')
            return False


class House:
    def reception(self, obj):
        if obj.model in self.base.keys():
            self.base[obj.model]['count'] += 1
            self.base[obj.model]['obj'].append(obj)
        else:
            self.base[obj.model] = {'count': 1, 'obj': [obj, ]}

    def print_info(self):
        print(self.base)


class Warehouse(House):
    def __init__(self, num_racks, num_shelfs, max_weight):
        self.num_racks = num_racks
        self.num_shelfs = num_shelfs
        self.max_weight = max_weight
        self.base = {}

    def transfer(self, subdivision, obj):
        self.base[obj.model]['count'] -= 1
        if self.base[obj.model]['count'] == 0:
            self.base.pop(obj.model)
        else:
            self.base[obj.model]['obj'].remove(obj)
        subdivision.reception(obj)


class Subdivision(House):
    def __init__(self, name):
        self.name = name
        self.base = {}


class OfficeEquipment:
    def __init__(self, model, weight, height, width, depth, color):
        true_data = ['abc', 1.0, 100, 100, 100, 'red']
        data = [model, weight, height, width, depth, color]
        check = True
        for i in range(len(data)):
            if not TypeError.check_type(data[i], true_data[i]):
                check = False
        if check == True:
            self.model = model
            self.weight = weight
            self.height = height
            self.width = width
            self.depth = depth
            self.color = color


class Printer(OfficeEquipment):
    def __init__(self, model, weight, height, width, depth, color, print_speed, print_type, print_format):
        OfficeEquipment.__init__(self, model, weight, height, width, depth, color)
        self.print_speed = print_speed
        self.print_type = print_type
        self.print_format = print_format


class Xerox(OfficeEquipment):
    def __init__(self, model, weight, height, width, depth, color, copy_speed, print_type, copy_format):
        OfficeEquipment.__init__(self, model, weight, height, width, depth, color)
        self.copy_speed = copy_speed
        self.print_type = print_type
        self.copy_format = copy_format


class Scanner(OfficeEquipment):
    def __init__(self, model, weight, height, width, depth, color, copy_speed, scan_format):
        OfficeEquipment.__init__(self, model, weight, height, width, depth, color)
        self.copy_speed = copy_speed
        self.copy_format = scan_format


def run():
    scanner1 = Scanner('Canon CanoScan LiDE 300', 1.7, 250, 42, 367, 'black', 6, 'A4')
    scanner2 = Scanner('Canon CanoScan LiDE 300', 1.7, 250, 42, 367, 'black', 6, 'A4')
    print(scanner1.color)
    warehouse = Warehouse(20, 20, 300)
    warehouse.reception(scanner1)
    warehouse.reception(scanner2)
    warehouse.print_info()
    subdivision = Subdivision('office')
    warehouse.transfer(subdivision, scanner1)
    warehouse.print_info()
    subdivision.print_info()
    warehouse.transfer(subdivision, scanner2)
    warehouse.print_info()
    subdivision.print_info()


run()
