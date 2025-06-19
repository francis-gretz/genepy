import os


class Dish:
    def __init__(self, name: str, preparation_time, dish_type: str):
        self.name: str = name
        self.preparation_time = preparation_time
        self.dish_type: str = dish_type

    def __eq__(self, other):
        return self.preparation_time == other.preparation_time

    def __ne__(self, other):
        return self.preparation_time != other.preparation_time

    def __lt__(self, other):
        return self.preparation_time < other.preparation_time

    def __le__(self, other):
        return self.preparation_time <= other.preparation_time

    def __gt__(self, other):
        return self.preparation_time > other.preparation_time

    def __ge__(self, other):
        return self.preparation_time >= other.preparation_time


class Menu:
    def __init__(self, name: str):
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __add__(self, second):
        third = Menu(self.name + " & " + second.name)

        for dish in self.dishes:
            third.add_dish(dish)
        for dish in second.dishes:
            third.add_dish(dish)

        return third

    def filter_by_type(self, dish_type: str):
        return list(filter(lambda x: x.dish_type == dish_type, self.dishes))

    def get_starters(self):
        return self.filter_by_type("starter")

    def get_dishes(self):
        return self.filter_by_type("dish")

    def get_desserts(self):
        return self.filter_by_type("dessert")

    def get_minimum_preparation_time(self):
        sum = 0
        for value in ["starter", "dish", "dessert"]:
            sum += self.get_minimum_preparation_time_by_dish_type(value)
        return sum

    def get_minimum_preparation_time_by_dish_type(self, value):
        by_type = self.filter_by_type(value)
        if len(by_type) == 0:
            return 0
        by_type.sort(key=lambda x: x.preparation_time, reverse=False)

        return by_type[0].preparation_time

    def get_maximum_preparation_time(self):
        sum = 0
        for value in ["starter", "dish", "dessert"]:
            sum += self.get_maximum_preparation_time_by_dish_type(value)
        return sum

    def get_maximum_preparation_time_by_dish_type(self, value):
        by_type = self.filter_by_type(value)
        if len(by_type) == 0:
            return 0
        by_type.sort(key=lambda x: x.preparation_time, reverse=True)

        return by_type[0].preparation_time

    def __str__(self):
        output = []
        for dish_type in ["starter", "dish", "dessert"]:
            output.append(dish_type.upper())

            items = self.filter_by_type(dish_type)
            sorted_items = sorted(items, key=lambda x: x.preparation_time)

            for item in sorted_items:
                output.append(item.name)

            output.append("")

        return os.linesep.join(output)


menu = Menu("my menu")

menu.add_dish(Dish("eggs & mayonaise", 1, "starter"))
menu.add_dish(Dish("salad", 0.5, "starter"))

menu.add_dish(Dish("burger", 2, "dish"))
menu.add_dish(Dish("pizza", 3, "dish"))
menu.add_dish(Dish("coq au vin", 4, "dish"))

menu.add_dish(Dish("chocolate cookie", 5, "dessert"))
menu.add_dish(Dish("waffle", 3, "dessert"))


print(menu)
print(menu.get_maximum_preparation_time())


menu_monday = Menu("Monday")
menu_monday.add_dish(Dish("Eggs & Mayonnaise", 5, "starter"))
menu_monday.add_dish(Dish("Salad", 10, "starter"))
menu_monday.add_dish(Dish("pizza", 30, "dish"))
menu_monday.add_dish(Dish("Waffles", 10, "dessert"))
monday_starters = menu_monday.get_starters()
assert len(monday_starters) == 2
dishes_types = set([dish.dish_type for dish in monday_starters])
assert len(dishes_types) == 1  # Only starters expected out of get_starters.
new_var = dishes_types.pop()
print(f"new_var: {new_var}")
assert new_var == "starter"  # The only dish type should be "starter


menu_friday = menu + menu_monday
print(menu_friday)
