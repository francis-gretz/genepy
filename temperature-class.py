class Temperature:
    CELSIUS_KELVIN = 273.15
    FAHRENHEIT_KELVIN = 459.67

    def get_celsius(self):
        """Get the temperature in celsius."""
        return self._celsius

    def set_celsius(self, value):
        """Set the temperature in celsius."""
        self._celsius = value
        self._fahrenheit = Temperature.convert_from_celsius_to_fahrenheit(value)
        self._kelvin = Temperature.convert_from_celsius_to_kelvin(value)

    celsius = property(get_celsius, set_celsius)

    def get_fahrenheit(self):
        """Get the temperature in fahrenheit."""
        return self._fahrenheit

    def set_fahrenheit(self, value):
        """Set the temperature in fahrenheit."""
        self._fahrenheit = value
        self._celsius = Temperature.convert_from_fahrenheit_to_celsius(value)
        self._kelvin = Temperature.convert_from_fahrenheit_to_kelvin(value)

    fahrenheit = property(get_fahrenheit, set_fahrenheit)

    def get_kelvin(self):
        """Get the temperature in kelvin."""
        return self._kelvin

    def set_kelvin(self, value):
        """Set the temperature in kelvin."""
        self._kelvin = value
        self._celsius = Temperature.convert_from_kelvin_to_celsius(value)
        self._fahrenheit = Temperature.convert_from_kelvin_to_fahrenheit(value)

    kelvin = property(get_kelvin, set_kelvin)

    # from Celsius to Kelvin:	    (x + 273.15) K
    # from Kelvin to Celsius:       (x − 273.15) °C
    # From Celsius to Fahrenheit:   (x * 9/5 ⁠+ 32) °F
    # From Fahrenheit to Celsius:   ((x − 32) * ⁠5/9)⁠ °C
    # from Kelvin to Fahrenheit: 	(x * 9/5 − 459.67) °F
    # From Fahrenheit to Kelvin:    ((x + 459.67) * ⁠5/9⁠) K
    def convert_from_celsius_to_kelvin(value):
        return value + Temperature.CELSIUS_KELVIN

    def convert_from_kelvin_to_celsius(value):
        return value - Temperature.CELSIUS_KELVIN

    def convert_from_celsius_to_fahrenheit(value):
        return value * (9 / 5) + 32

    def convert_from_fahrenheit_to_celsius(value):
        return (value - 32) * (5 / 9)

    def convert_from_fahrenheit_to_kelvin(value):
        return (value + Temperature.FAHRENHEIT_KELVIN) * (5 / 9)

    def convert_from_kelvin_to_fahrenheit(value):
        return value * (9 / 5) - Temperature.FAHRENHEIT_KELVIN


# c = Temperature()
# c.celsius = 50
# c.celsius += 1
# print(c.celsius)
# print(c.kelvin)
# print(c.fahrenheit)
# print("--------")

# c.fahrenheit += 50
# print(c.celsius)
# print(c.kelvin)
# print(c.fahrenheit)


# Converting -459.67°F to celsius: found -477.4477777777778, expected -273.15
t0 = Temperature()
t0.fahrenheit = -459.67
print(t0.celsius)
print(t0.fahrenheit)
print(t0.kelvin)
