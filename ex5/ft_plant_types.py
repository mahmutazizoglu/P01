class Plant():
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float
                 ) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, heght can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days\n")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, amount: float) -> None:
        self._height = self._height + amount

    def age(self, days: int) -> None:
        self._age = self._age + days


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float,
                 color: str
                 ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._has_bloomed: bool = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, new_color: str) -> None:
        self._color = new_color

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._has_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, new_diameter: float) -> None:
        self._trunk_diameter = new_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float,
                 harvest_season: str
                 ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_harvest_season(self, new_season: str) -> None:
        self._harvest_season = new_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def grow(self, amount: float) -> None:
        super().grow(amount)

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 1.0, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 1.0, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
