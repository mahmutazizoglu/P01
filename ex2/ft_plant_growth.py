class Plant():
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float
            ) -> None:
        self.name = name
        self.height = height
        self.age_ = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_ = self.age_ + 1


rose = Plant("Rose", 25, 30, 0.8)
# sunflower = Plant("Sunflower", 80, 40, 2)

print("=== Garden Plant Growth ===")
for plant in [rose]:
    start_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.show()
        plant.age()
        plant.grow()
    increase = plant.height - start_height
    print(f"Growth this week: {round(increase, 0)}cm\n")
