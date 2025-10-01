class Fridge:
    def __init__(self, ingredients, temp=3):
        self.__temp = temp
        self.__ingredients = ingredients
        

    def get_ingredients(self):
        return self.__ingredients
    
    def add_ingredients(ingredients):
        self.__ingredients.append(ingredients)
        
    def empty_fridge(self):
        self.__ingredients = []

    def get_temp(self):
        return self.__temp
    

    def set_temp(self, temp):
        self.__temp = temp 
        

    def __str__(self):
        return f"ingredients: {','.join(self.__ingredients)} \ntemperature: {self.__temp}"