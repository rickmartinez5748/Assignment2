def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if height <= 0:
            return "Invalid height"
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except (ValueError, TypeError):
        return "Invalid input"
