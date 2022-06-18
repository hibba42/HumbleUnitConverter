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

"""
Thank you for downloading this software, and I hope that you enjoy it!
Here is an overview of how it is intended to work:

Prompt the user for the over-arching category that we are working with.  
    -For example, distance, temperature, weight (to be added later), and so on.
    -It should also create a respective object, such as a Distance() object or a Temperature() object.
From the over-arching category, show available options. 
    -For example, if the user selects 'distance,' show them meters, inches, and so on.
    -The category object then creates an object of the selected type, such as an Inch() or a Meter() object.
Prompt the user for the quantity of that unit, and pass that quantity to the above object.
Prompt the user for the unit that we want to convert to.
    -The above object should have a ConvertTo() function that accepts this as a parameter.
Finally, print out the details and prompt to run again or quit.

Please feel free to contact me at CharlesSimmons43@gmail.com with any questions.
"""

from HUC_Temperature import *
from HUC_Distance import *
from HUC_License_and_Warranty_Disclaimer import *


def UserPrompt(user_input = None, from_unit = None, to_unit = None, quantity = None):
    """
    Using a function with default parameters to interact with the user, instead of initializing variables.
    This is done mainly to avoid creating temporary variables just to hold things like quantity.
    """
    # Showing the basic license and warranty disclaimer:
    print("""Humble Unit Converter, Copyright 2022 Charles Simmons
This program comes with ABSOLUTELY NO WARRANTY; for details type 'W'.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'L' for details.
""")

    while user_input != "QUIT" and user_input != "Q":  # This will loop until the user terminates it.
        # Start with determining what our initial units that we are converting from are:
        user_input = input("What would you like to convert?     (T)emperature     (D)istance     OR     view (L)icense or (W)arranty disclaimer  :     ").upper()

        # Now that we have that, let's begin processing in terms of that category, or display the requested information.
        if user_input == "T":
            main_category = Temperature()
        elif user_input == "D":
            main_category = Distance()
        elif user_input == "L" or user_input == "LICENSE":
            ShowLicense()
            continue # We want the loop to restart at this point, bringing us back to the initial prompt.
        elif user_input == "W" or user_input == "WARRANTY":
            ShowWarranty()
            continue # We want the loop to restart at this point, bringing us back to the initial prompt.

        # More specifically, which units are we converting from?
        from_unit = input("Which units  would you like to convert from?  :  " + main_category.ShowAvailableUnits()).upper()

        # Create a unit object of that type:
        from_unit_object = main_category.CreateUnitObject(from_unit)

        # How many of that unit?
        quantity = float(input("How many?  :  "))
        from_unit_object.SetQuantity(quantity)

        # Prompt for what we're converting to.  Note that this excludes the current unit from the list.
        to_unit = input("Convert to?  :  " + main_category.ShowAvailableUnits(from_unit_object.GetAbbreviation()))

        for index in range(0, len(to_unit)):
            """
            Quick Detour: We want to print the to_unit abbreviation with the first letter capitalized,
            and the following letter(s) in lower-case.
            """
            if index == 0:
                return_string = to_unit[0].upper() # Start by capitalizing the first letter.
            else:
                return_string += to_unit[index].lower() # Lower-case for each otherwise, and add to the string.
        to_unit = return_string # Now we set our processed string back to the to_unit variable.

        # Perform the conversion and print it:
        print(from_unit_object.GetQuantity(), from_unit_object.GetAbbreviation(), "converts to ",
              from_unit_object.ConvertTo(to_unit.upper()), to_unit)

        # Now to prompt to run again or end:
        user_input = input("(R)un again or (Q)uit  :  ").upper()


# And finally, we call the above function to begin interaction with the user:
UserPrompt()
