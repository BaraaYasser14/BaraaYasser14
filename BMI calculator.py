Units = input("Imperial(Lbs, in) or Metric(Kg, CM): ")
def imperial(weight , height):
    bmi_imperial = (weight / (height * height)) * 703
    return bmi_imperial
def metirc(weight, height):
    height = height / 100
    bmi_metric = weight / (height * height)
    return bmi_metric
if Units.lower() == "imperial":
    weight = int(input("Enter your weight in lbs: "))
    height = int(input("Enter your height in in: "))
    print(f"Your BMI is {imperial(weight , height)}")
elif Units.lower() == "metric":
    weight = int(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    print(f"Your BMI is {metirc(weight, height)}")
else:
    print('Invalid Input.')