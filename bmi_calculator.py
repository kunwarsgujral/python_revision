# bmi =  weight(kg) / height ** 2(m**2)

print("Hello & Welcome to the BMI Calculator") 
weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in meters: "))
bmi =  weight/(height * height)
print("Your BMI is: "+str(bmi))
