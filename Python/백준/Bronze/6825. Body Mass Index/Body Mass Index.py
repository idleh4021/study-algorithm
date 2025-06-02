weight = float(input())
height = float(input())
bmi = weight/(height**2)
print('Underweight' if bmi<18.5 else 'Overweight' if bmi>25 else 'Normal weight')