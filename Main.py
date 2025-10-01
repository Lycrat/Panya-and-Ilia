import HeadChef as H
import KitchenAppliances


chef = H.HeadChef("Ilia", "GOAT")
print(chef)

fridge = KitchenAppliances.Fridge(["Ilia", "Beer", "Ano", "MORE BEER"])
print(fridge)


smartFridge = KitchenAppliances.SmartFridge(["Ilia"], 0, 1)

try:
    smartFridge.dispense_ice()
except KitchenAppliances.NoIceException as e:
    print(e)
finally:
    print(f"current ice level: {smartFridge.ice}")