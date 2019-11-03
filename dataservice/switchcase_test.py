
def Gas_Control_05_03_01(b):
    print(b[0])
print('register 01')
def Gas_Control_05_03_02(b):
    print('register 02')

def Gas_Control_05_03_03(b):
    print('register 03')

def Gas_Control_05_03_04(b):
    print('register 04')
def Gas_Control_05_03_14(b):
    print('register 02')

def Gas_Control_05_03_15(b):
    print('register 03')

def Gas_Control_05_03_16(b):
    print('register 04')

def Gas_Control_05_03_17(b):
    print('register 02')

def Gas_Control_05_03_18(b):
    print('register 03')








def register_case(x,b):
    cases={
        b'\x01': Gas_Control_05_03_01,
        b'\x02': Gas_Control_05_03_02,
        b'\x03': Gas_Control_05_03_03,
        b'\x04': Gas_Control_05_03_04,
        b'\x14': Gas_Control_05_03_14,
        b'\x15': Gas_Control_05_03_15,
        b'\x16': Gas_Control_05_03_16,
        b'\x17': Gas_Control_05_03_17,
        b'\x18': Gas_Control_05_03_18,
    }
    func=cases.get(x,None)
    return func(b)


if __name__=="__main__":
    print('hello')
    b='hello world'
    register_case(b'\x01',b)
    register_case(b'\x03',b)
    register_case(b'\x02',b)
    register_case(b'\x04', b)

