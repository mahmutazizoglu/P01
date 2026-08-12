#!/usr/bin/env pythom3


class Plant():
    class _Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_coumt: int = 0
            self._show_count: int = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_coumt += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_coumt} age, {self._show_count} show")

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
        self._age = self.age + days
        self._stats.increment_age()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)
