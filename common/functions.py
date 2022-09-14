def C2K(degree_Celsius):
    degree_Kelvin = degree_Celsius + 273.15
    return degree_Kelvin


def C2F(degree_Celsius):
    degree_Fahrenheit = degree_Celsius * 9 / 5 + 32
    return degree_Fahrenheit



def K2C(degree_Kelvin):
    degree_Celsius = degree_Kelvin - 273.15
    return degree_Celsius


def K2F(degree_Kelvin):
    degree_Fahrenheit = (degree_Kelvin - 273.15) * 9 / 5 + 32
    return degree_Fahrenheit


def F2C(degree_Fahrenheit):
    degree_Celsius = (degree_Fahrenheit - 32) * 5 / 9
    return degree_Celsius


def F2K(degree_Fahrenheit):
    degree_Kelvin = (degree_Fahrenheit - 32) * 5 / 9 + 273.15
    return degree_Kelvin
