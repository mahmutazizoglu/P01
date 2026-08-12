#!/usr/bin/env pythom3


class Plant():
    class _Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

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
        self._stats = Plant._Stats()

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
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
        self._stats.increment_show()

    def grow(self, amount: float) -> None:
        self._height = self._height + amount
        self._stats.increment_grow()

    def age(self, days: int) -> None:
        self._age = self._age + days
        self._stats.increment_age()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


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
    def __init__(self, name: str,
                 height: float,
                 age: int,
                 growth_rate: float,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        self._shade_count: int = 0

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, new_diameter: float) -> None:
        self._trunk_diameter = new_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produce a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter} cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shade_count} shade")


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

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth_rate: float,
                 color: str,
                 seeds: int = 0
                 ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds: int = seeds

    def get_seeds(self) -> int:
        return self._seeds

    def set_seeds(self, new_seeds: int) -> None:
        self._seeds = new_seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[Statistics for {plant.name}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year?  -> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year?  -> "
          f"{Plant.is_older_than_a_year(400)}")

    print("\n===Flower")
    rose = Flower("Rose", 15.0, 10, 1.0, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n===Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n===Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 1.0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)
