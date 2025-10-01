class Fridge:
    """
    Fridge class.
    """
    def __init__(self, ingredients, temp=3):
        self.__temp = temp
        self.__ingredients = ingredients
        

    def get_ingredients(self):
        """
        Returns all ingredients in the fridge.
        
        Returns: list[string]
        """
        return self.__ingredients
    
    def add_ingredients(self, ingredients):
        """
        Add ingredients to the fridge
        
        Params: list[string]
        """
        self.__ingredients.append(ingredients)
        
    def empty_fridge(self):
        """
        Removes all ingredients from fridge
        """
        self.__ingredients = []

    def get_temp(self):
        """
        Return the temperature of the fridge

        Returns: Int
        """
        return self.__temp
    

    def set_temp(self, temp):
        """
        Set the temperature of the fridge

        Params: Int
        """
        self.__temp = temp 
        

    def __str__(self):
        return f"ingredients: {','.join(self.__ingredients)} \ntemperature: {self.__temp}"