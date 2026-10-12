class car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f"brand: {self.brand}, model: {self.model}, color: {self.color}")

car1 = car("Chevrolet", "Suburban", "Blanco")
car2 = car("Toyota", "Tacoma", "Azul")

car1.show_info()
car2.show_info()