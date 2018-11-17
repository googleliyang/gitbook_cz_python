class Tem:
    def __del__(self):
        print('I was destroyed')


tem = Tem()
tem1 = tem
del tem