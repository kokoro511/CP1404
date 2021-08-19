COLOUR_CODES = {"AliceBlue": "#f0f8ff", "LawnGreen": "#7cfc00",
                "LavenderBlush1": "#fff0f5", "LavenderBlush2": "#eee0e5",
                "LavenderBlush3": "#cdc1c5", "LavenderBlush4": "#8b8386",
                "OrangeRed1": "#ff4500", "OrangeRed2": "#ee4000",
                "OrangeRed3": "#cd3700", "OrangeRed4": "#8b2500",
                "PapayaWhip": "#ffefd5", "snow1": "#fffafa", "snow2": "#eee9e9",
                "snow3": "#cdc9c9", "snow4": "#8b8989"}

colour_name = input("Please enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")