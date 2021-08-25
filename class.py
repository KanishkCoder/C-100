class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print('Stopted')

    def accelarate(self):
        print('Accelarating..')

    def change_gear(self,gear_type):
        print('Gear changed')

Audi=Car('A6','Blue', 'Audi', '300km')
print(Audi.color)
print(Audi.company)
print(Audi.model)
print(Audi.speed_limit)