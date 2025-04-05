def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Exemple d'utilisation
if __name__ == "__main__":
    temp_c = 25  # Celsius
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is equal to {temp_f}°F")

    temp_f = 77  # Fahrenheit
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is equal to {temp_c}°C")
    
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

# Exemple d'utilisation
if __name__ == "__main__":
    distance_km = 10  # kilomètres
    distance_miles = km_to_miles(distance_km)
    print(f"{distance_km} km is equal to {distance_miles} miles")

    distance_miles = 6.21  # miles
    distance_km = miles_to_km(distance_miles)
    print(f"{distance_miles} miles is equal to {distance_km} km")
