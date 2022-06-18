"""
Humble Unit Converter: A simple program to convert units from one type to another.
Copyright 2022 Charles Simmons

This file is part of Humble Unit Converter.

Humble Unit Converter is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

Humble Unit Converter is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Humble Unit Converter. If not,
see <https://www.gnu.org/licenses/>.
"""

"""Classes relating to distance conversions can be found in this file."""


class Distance:
    """
    A class for when the user wishes to work with distance objects.
    Handles both Imperial and Metric measurement conversions (miles to km, meters to km, inches to feet, etc...)
    """
    def __init__(self):
        """Distance will be aware the various measurement units:"""
        self._units = {"In" : "Inches",
                       "Ft" : "  Feet",
                       "Yd" : "  Yards",
                       "Mi" : "Miles",
                       "Me" : "Meters",
                       "Cm" : "  Centimeters",
                       "Km" : "  Kilometers"}
        # Note: The extra spacing is there to ensure that the below function prints the names cleanly.
        # Else, we were getting results like "Ftet" and "Ydards."

    def ShowAvailableUnits(self, optional_exclude_unit=""):
        """
        We want the output in the form of (In)ches, (Me)ters and so on.
        Note: the parameter is optional, and is used to specify if there is a unit in the list that we do NOT
        want printed.  For example, if we are working with an Inches object and do not want it to show inches as
        an option to convert to.
        """
        return_string = ""  # Initialize a variable to hold the available units.
        for unit in self._units:
            if unit != optional_exclude_unit: # Checks if we want to exclude a unit from printing.
                # The below prints the key in parentheses, and then the rest of the value after.
                return_string += "(" + unit + ")" + self._units[unit][len(unit):] + "     "
        return return_string

    def CreateUnitObject(self, desired_unit):
        """Creates and returns an object that should match with one of the units below."""
        if desired_unit == "IN":
            return Inch()
        elif desired_unit == "FT":
            return Foot()
        elif desired_unit == "YD":
            return Yard()
        elif desired_unit == "MI":
            return Mile()
        elif desired_unit == "ME":
            return Meter()
        elif desired_unit == "CM":
            return Centimeter()
        elif desired_unit == "KM":
            return Kilometer()


class Template_Distance:
    """
    This exists as a parent class for all temperature-related objects.
    Generally, it should not be used to create its own objects, but rather share code between the other object classes.
    """

    def GetQuantity(self):
        """A Get accessor for the number of units."""
        return self._quantity

    def SetQuantity(self, quantity_input):
        """A set accessor for the number of units."""
        self._quantity = quantity_input

    def GetAbbreviation(self):
        """A get accessor for the shorthand; useful for printing output."""
        return self._shorthand


class Inch(Template_Distance):
    """
    Represents an inch, and handles conversions related to it.  This will be the base of our Imperial
    measurements, as feet, meters, and miles can all be converted into inches.
    """
    def __init__(self):
        self._shorthand = "In"
        self._quantity = None

    def ConvertTo(self, target_unit):
        """The function that converts the inches to another measurement."""
        if target_unit.upper() == "FT":
            return self._quantity / 12
        elif target_unit.upper() == "YD":
            return self._quantity / 36
        elif target_unit.upper() == "MI":
            return self._quantity / (12 * 5280)
        elif target_unit.upper() == "ME":
            return self._quantity / 39.37
        elif target_unit.upper() == "CM":
            return self._quantity / 0.3937
        elif target_unit.upper() == "KM":
            return self._quantity / 39370


class Foot(Template_Distance):
    """Represents a foot, based off of inches."""
    def __init__(self):
        self._shorthand = "Ft"
        self._quantity = None
        self._base_unit = Inch()

    def ConvertTo(self, target_unit):
        """
        The function that converts the feet to another measurement.
        Using inch as the base unit for consistency. The line below converts
        the feet into inches, and then we apply the inch functions for the conversions.
        """
        self._base_unit.SetQuantity(12 * self._quantity) # 1 foot is 12 inches.
        if target_unit.upper() == "IN":
            return self._base_unit.GetQuantity() # Inch is the base, so we just return the number of inches.
        else:
            return self._base_unit.ConvertTo(target_unit) # Otherwise, a foot is just 12 * any of the inch conversions.


class Yard(Template_Distance):
    """Represents a yard, based off of inches."""
    def __init__(self):
        self._shorthand = "Yd"
        self._quantity = None
        self._base_unit = Inch()

    def ConvertTo(self, target_unit):
        """
        The function that converts the yards to another measurement.
        Using inch as the base unit for consistency. The line below converts
        the yards into inches, and then we apply the inch functions for the conversions.
        """
        self._base_unit.SetQuantity(36 * self._quantity) # 1 yard is 36 inches.
        if target_unit.upper() == "IN":
            return self._base_unit.GetQuantity() # Inch is the base, so we just return the number of inches.
        else:
            return self._base_unit.ConvertTo(target_unit) # Otherwise, a yard is just 36 * any of the inch conversions.


class Mile(Template_Distance):
    """Represents a mile, based off of inches."""
    def __init__(self):
        self._shorthand = "Mi"
        self._quantity = None
        self._base_unit = Inch()

    def ConvertTo(self, target_unit):
        """
        The function that converts the miles to another measurement.
        Using inch as the base unit for consistency. The line below converts
        the miles into inches, and then we apply the inch functions for the conversions.
        """
        self._base_unit.SetQuantity(12 * 5280 * self._quantity) # 1 foot is 12 inches; 1 mile is 5,280 feet.
        if target_unit.upper() == "IN":
            return self._base_unit.GetQuantity() # Inch is the base, so we just return the number of inches.
        else:
            return self._base_unit.ConvertTo(target_unit) # Otherwise, convert using the Inch() object's methods.


class Meter(Template_Distance):
    """
    Represents a meter, and handles conversions related to it.  This will be the base of our Metric
    measurements, as centimeters, kilometers, and so on can all be converted into meters.
    """
    def __init__(self):
        self._shorthand = "Me"
        self._quantity = None

    def ConvertTo(self, target_unit):
        """The function that converts the quantity from one type to another."""
        if target_unit.upper() == "IN":
            return self._quantity * 39.37
        if target_unit.upper() == "FT":
            return (self._quantity * 39.37) / 12
        if target_unit.upper() == "YD":
            return (self._quantity * 39.37) / 36
        if target_unit.upper() == "MI":
            return (self._quantity * 39.37) / (12 * 5280)
        if target_unit.upper() == "CM":
            return self._quantity * 100
        if target_unit.upper() == "KM":
            return self._quantity / 1000


class Centimeter(Template_Distance):
    """Represents a centimeter, based off of meters."""

    def __init__(self):
        self._shorthand = "Cm"
        self._quantity = None
        self._base_unit = Meter()

    def ConvertTo(self, target_unit):
        """
        The function that converts centimeters to another measurement.
        Using meter as the base unit for consistency. The line below converts
        the centimeters into meters, and then we apply the meter functions for the conversions.
        """
        self._base_unit.SetQuantity(self._quantity / 100)  # 1 meter is 100 centimeters.
        if target_unit.upper() == "ME":
            return self._base_unit.GetQuantity()  # Meter is the base, so we just return the number of meters.
        else:
            return self._base_unit.ConvertTo(target_unit)  # Otherwise, convert using the Meter() object's methods.


class Kilometer(Template_Distance):
    """Represents a kilometer, based off of meters."""
    def __init__(self):
        self._shorthand = "Km"
        self._quantity = None
        self._base_unit = Meter()

    def ConvertTo(self, target_unit):
        """
        The function that converts kilometers to another measurement.
        Using meter as the base unit for consistency. The line below converts
        the kilometers into meters, and then we apply the meter functions for the conversions.
        """
        self._base_unit.SetQuantity(self._quantity * 1000)  # 1 kilometer is 1000 meters.
        if target_unit.upper() == "ME":
            return self._base_unit.GetQuantity()  # Meter is the base, so we just return the number of meters.
        else:
            return self._base_unit.ConvertTo(target_unit)  # Otherwise, convert using the Meter() object's methods.
