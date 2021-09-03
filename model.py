import sqlite3

from database import Database


class FoodData:
    def __init__(self):
        pass

    def get_nutrition_info(self):
        result = Database().search('nutrition')
        return result

    def get_food_info(self):
        result = Database().search('food')
        return result

    def get_ingredients_info(self):
        result = Database().search('ingredient')
        return result

    def get_web_links(self):
        f = open("./.data/WebLinks.csv", "r", encoding='utf-8-sig')
        reader = csv.reader(f)
        for row in reader:
            self.weblinks_info.append(row)
        f.close()
        return self.weblinks_info

    def get_food_avoided(self):
        f = open("./.data/Aged2YearsAndOverTypeOfFoodAvoided.csv", "r", encoding='utf-8-sig')
        reader = csv.reader(f)
        for row in reader:
            self.food_avoided.append(row)
        f.close()
        return self.food_avoided


class Hospital:

    def __init__(self):
        pass

    def get_hospital_data(self):
        result = Database().search('hospitals')
        return result
