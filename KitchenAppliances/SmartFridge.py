import KitchenAppliances.Fridge as Fridge
import KitchenAppliances.NoIceException as NoIceException

class SmartFridge(Fridge):
    def __init__(self, ingredients, ice, temp=0):
        super().__init__( ingredients, temp)

        self.ice = ice


    def dispense_ice(self):
        if self.ice > 0:
            print("DISPENSING ICE...")
            self.ice -= 1 
        else:
            raise NoIceException.NoIceException("NO ICE", 400)
                    
    def empty_fridge(self):
        self.ingredients = []
        self.ice = 0
        

    def add_ice(self, amount):
        self.ice += amount




    
    