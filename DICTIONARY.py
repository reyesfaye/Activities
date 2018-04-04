elements = {1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron",
          6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Flourine", 10: "Neon",
          11: "Sodium", 12: "Magnesium", 13: "Aluminum", 14: "Silicon",
          15: "Phosphorus", 16: "Sulphur", 17: "Chlorine", 18: "Argon",
          19: "Potassium", 20: "Calcium"}
while True:
    element_position = int(input("Enter the element's position(1-20):"))
    if element_position == " ":
        break
    else:
        print(element_position, ": ", elements[element_position])
