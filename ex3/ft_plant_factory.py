class Plant():
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float
                 ) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate


print("=== Plant Factory Output ===")
rose = Plant("Rose", 25.0, 30, 0.2)
rose.show()
oak = Plant("Oak", 200.0, 365, 0.2)
oak.show()
cactus = Plant("Cactus", 5.0, 90, 0.2)
cactus.show()
sunflower = Plant("Sunflower", 80.0, 45, 0.2)
sunflower.show()
fern = Plant("Fern", 15.0, 120, 0.2)
fern.show()
