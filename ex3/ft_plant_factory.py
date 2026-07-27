class Plant():
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = float(height)
        self.age = age
        self.growth_rate = growth_rate
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += self.growth_rate


print("=== Plant Factory Output ===")
rose = Plant("Rose", 25.0, 30, 0.2)
oak = Plant("Oak", 200.0, 365, 0.2)
cactus = Plant("Cactus", 5.0, 90, 0.2)
sunflower = Plant("Sunflower", 80.0, 45, 0.2)
fern = Plant("Fern", 15.0, 120, 0.2)
