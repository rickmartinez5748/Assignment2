#Function to calculate BMI

def bmi_calculation(weight, height):
    weight = float(weight)
    height = float(height)
    if height <= 0:
        return "The height is invalid"
    bmi=weight/(height**2)
    return round(bmi,2)

