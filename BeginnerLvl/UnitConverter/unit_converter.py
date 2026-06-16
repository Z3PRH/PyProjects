# Categories:
# Temperature ( C to F and Vice versa)
# Distance (Km to Miles and Vice versa)
# Weight (Kg to Pounds and Vice versa)

def convert(category, unit):
    if category == "Temperature":  # Checking which category they picked before coversion
        direction = input(
            "Do you want to Covert it into Celsius or Fahrenheit : ")
        T_unit = unit
        if direction == "C".lower():
            converted_unit = (T_unit - 32) * 5/9
            print(
                f"Temperature in Fahrenheit: {T_unit}F \nTemperature in Celsius : {converted_unit}C")
        else:
            converted_unit = (T_unit * 9/5) + 32
            print(
                f"Temperature in Celsius: {T_unit}C \nTemperature in Fahrenheit : {converted_unit}F")

    elif category == "Distance":
        direction = input("Do you want to Covert it into Km or Miles : ")
        D_unit = unit
        if direction == "Km".lower():
            converted_unit = D_unit/(0.621371)
            print(
                f"Distance in Miles: {D_unit}Miles \nDistance in Km : {converted_unit}Km")
        else:
            converted_unit = D_unit * 0.62137
            print(
                f"Distance in Km: {D_unit}Km \nDistance in Miles : {converted_unit}mi")

    else:
        direction = input("Do you want to Covert it into Kg or Pounds : ")
        W_unit = unit
        if direction == "Kg".lower():
            converted_unit = W_unit/(2.20462)
            print(
                f"Weight in Pounds: {W_unit}lb \nWeight in Kg : {converted_unit}Kg")
        else:
            converted_unit = W_unit * 2.20462
            print(
                f"Weight in Kg: {W_unit}Kg \nWeight in Pounds : {converted_unit}lb")


print("=="*12, "Welcome to Unit Coverter", "=="*12)

while True:
    print("1.Temperature\n2.Distance\n3.Weight")
    category = input("Please Enter the Category from the Above Three : ")
    unit = float(input("Please Enter the Values : "))
    convert(category, unit)
    choice = input("Wanna Try Again (Yes/No)? : ").lower()
    if choice != "yes":
        print("Adios")
        break
        