class ConversionTools:
    def __init__(self):
        pass

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kilometers_to_miles(self, kilometers):
        return kilometers * 0.621371

    def miles_to_kilometers(self, miles):
        return miles / 0.621371

    def pounds_to_kilograms(self, pounds):
        return pounds * 0.453592

    def kilograms_to_pounds(self, kilograms):
        return kilograms / 0.453592
    
    def inches_to_centimeters(self, inches):
        return inches * 2.54
    
    def centimeters_to_inches(self, centimeters):
        return centimeters / 2.54
    
    def liters_to_gallons(self, liters):
        return liters * 0.264172
    
    def gallons_to_liters(self, gallons):
        return gallons / 0.264172

    def kilograms_to_grams(self, kilograms):
        return kilograms * 1000

    def grams_to_kilograms(self, grams):
        return grams / 1000

    def meters_to_feet(self, meters):
        return meters * 3.28084

    def feet_to_meters(self, feet):
        return feet / 3.28084
        
    def centimeters_to_meters(self, centimeters):
        return centimeters / 100
    
    def meters_to_centimeters(self, meters):
        return meters * 100
    
    def meters_to_kilometers(self, meters):
        return meters / 1000
    
    def kilometers_to_meters(self, kilometers):
        return kilometers * 1000
    
    def seconds_to_minutes(self, seconds):
        return seconds / 60
    
    def minutes_to_seconds(self, minutes):
        return minutes * 60
    
    def hours_to_minutes(self, hours):
        return hours * 60
    
    def minutes_to_hours(self, minutes):
        return minutes / 60
    
    def days_to_weeks(self, days):
        return days / 7
    
    def weeks_to_days(self, weeks):
        return weeks * 7
    
    def years_to_months(self, years):
        return years * 12
    
    def months_to_years(self, months):
        return months / 12
    
    def years_to_days(self, years):
        return years * 365.25
    
    def days_to_years(self, days):
        return days / 365.25
    
    def hours_to_seconds(self, hours):
        return hours * 3600
    
    def seconds_to_hours(self, seconds):
        return seconds / 3600
    
    def liters_to_milliliters(self, liters):
        return liters * 1000
    
    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000
    
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    
    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32
