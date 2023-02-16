class Tk:
    def __init__(self):
        print('sajjad from A')

    def add(self):
        print('add')    


class App(Tk):
    def __init__(self):
        # super().__init__()
        print('sajjad from B ')


sajjad = Tk()
sajjad.add()       