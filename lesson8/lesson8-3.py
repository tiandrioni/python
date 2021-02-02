class ListError(Exception):
    def __init__(self, text):
        self.text = text

    @classmethod
    def check(cls, num_str: str):
        try:
            num = int(num_str)
        except ValueError:
            print('Ввели не число')
            return False
        else:
            return num


def run():
    out_list = []
    while True:
        inp_data = input('Введите число: ')
        if inp_data == 'stop':
            break
        check_num = ListError.check(inp_data)
        if check_num:
            out_list.append(check_num)
    print(out_list)


run()
