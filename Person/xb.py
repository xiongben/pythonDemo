

class XB:
    name = "XB class"
    def __init__(self, age):
        super().__init__()
        self.age = age
        print('====ggg====={0}'.format(self.age))
        print(XB.name)