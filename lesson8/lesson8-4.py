class Warehouse:
    def __init__(self, num_racks, num_shelfs, max_weight):
        self.num_racks = num_racks
        self.num_shelfs = num_shelfs
        self.max_weight = max_weight


class OfficeEquipment:
    def __init__(self, model, weight, height, width, depth, color):
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
    scanner = Scanner('Canon CanoScan LiDE 300', 1.7, 250, 42, 367, 'black', 6, 'A4')
    print(scanner.color)


run()
