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


print("=== Garden Security System ===")
Rose = Plant("Rose", 15.0, 10, 1)
print(f"Plant created: {Rose.name}: {round(Rose.get_height(), 1)}cm,"
      f" {Rose.get_age()} days old\n")
Rose.set_height(25)
Rose.set_age(30)

Rose.set_height(-1)
Rose.set_age(-1)
print(f"Current state: {Rose.name}: {round(Rose.get_height(), 1)}cm,"
      f" {Rose.get_age()} days old")
