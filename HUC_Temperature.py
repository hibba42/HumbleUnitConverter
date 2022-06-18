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

"""Classes relating to temperature conversions can be found in this file."""


class Temperature:
    """
    A class for when the user wishes to work with temperature objects.
    Handles tracking which temperature options we have available, and creating a relevant object.
    """
    def __init__(self):
        """Temperature will be aware the various measurement units:"""
        self._units = {"C" : "Celsius", "F" : "Fahrenheit"}

    def ShowAvailableUnits(self, optional_exclude_unit=""):
        """
        We want the output in the form of (C)elsius, (F)ahrenheit, and so on.
        Note: the parameter is optional, and is used to specify if there is a unit in the list that we do NOT
        want printed.  For example, if we are working with a Celsius object, we don't want it to print Celsius as
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
        if desired_unit == "C":
            return Celsius()
        elif desired_unit == "F":
            return Fahrenheit()

class Template_Temperature:
    """
    This exists as a parent class for all temperature-related objects.
    Generally, it should not be used to create its own objects, but rather share code between the other object classes.
    """

    def GetQuantity(self):
        """A Get accessor for the number of degrees."""
        return self._degrees

    def SetQuantity(self, degrees_input):
        """A set accessor for the number of degrees."""
        self._degrees = degrees_input

    def GetAbbreviation(self):
        """A get accessor for the shorthand; useful for printing output."""
        return self._shorthand


class Celsius(Template_Temperature):
    """A class to represent Celsius degrees, and what they can convert to.
    Accepts an initial number of degrees as a parameter."""
    def __init__(self):
        self._shorthand = "C"  # An abbreviation for the unit name.
        self._degrees = None  # Initializing a variable to hold the number of degrees.

    def ConvertTo(self, target_unit):
        """The function that converts the degrees from one type to another."""
        if target_unit == "F":
            return (9/5 * float(self._degrees) + 32)


class Fahrenheit(Template_Temperature):
    """A class to represent Fahrenheit degrees, and what they can convert to."""
    def __init__(self):
        self._shorthand = "F"  # An abbreviation for the unit name.
        self._degrees = None  # Initializing a variable to hold the number of degrees.

    def ConvertTo(self, target_unit):
        """The function that converts the degrees from one type to another."""
        if target_unit == "C":
            return (5/9 * float(self._degrees) - (160/9))

