# PJ VanDussen
# 12/14/2024
# Fahrenheit Converter

def convert_to_fahrenheit(celsius):
    fahrenheit_temp = celsius * 1.8 + 32
    return fahrenheit_temp


for celsius in range(0, 7):
    convert_to_fahrenheit(celsius)
    print(f'Celsius: {celsius}  Fahrenheit: {fahrenheit_temp.convert_to_fahrenheit()}')