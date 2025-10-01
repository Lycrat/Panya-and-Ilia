import HeadChef as H
import Fridge as F
from SmartFridge import SmartFridge
from NoIceException import NoIceException
chef = H.HeadChef("Ilia", "GOAT")
print(chef)

fridge = F.Fridge(["Ilia", "Beer", "Ano", "MORE BEER"])
print(fridge)


smartFridge = SmartFridge(["Ilia"], 0, 1)

try:
    smartFridge.dispense_ice()
except NoIceException as e:
    print(e)
finally:
    print(f"current ice level: {smartFridge.ice}")