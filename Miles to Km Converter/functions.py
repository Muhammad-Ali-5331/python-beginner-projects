class Functions:
    def __init__(self):
        # Initialize the available choices for conversion
        self.choices_1 = ["Miles", "Km", "Lb", "Meters", "Cm", "Feet", "Inch", "Gram", "Kg", "Yards", "Ounces","Liters","Milliliters", "Gallons"]
        # Copy the list for secondary choices
        self.choices_2 = self.choices_1.copy()
        # Define invalid conversion pairs for each unit
        self.invalid_conversions = {
            "Miles": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Km": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Meters": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Cm": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Feet": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Inch": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],
            "Yards": ["Lb", "Gram", "Kg", "Ounces","Liters", "Gallons"],


            "Lb": ["Miles", "Km", "Meters", "Cm", "Feet", "Inch", "Yards","Liters","Milliliters", "Gallons"],
            "Gram": ["Miles", "Km", "Meters", "Cm", "Feet", "Inch", "Yards","Liters","Milliliters", "Gallons"],
            "Kg": ["Miles", "Km", "Meters", "Cm", "Feet", "Inch", "Yards","Liters","Milliliters", "Gallons"],
            "Ounces": ["Miles", "Km", "Meters", "Cm", "Feet", "Inch", "Yards","Liters","Milliliters", "Gallons"],

            "Milliliters": ["Miles", "Km", "Lb", "Meters", "Cm", "Feet", "Inch", "Gram", "Kg", "Yards"],
            "Liters": ["Miles", "Km", "Lb", "Meters", "Cm", "Feet", "Inch", "Gram", "Kg", "Yards"],
            "Gallons": ["Miles", "Km", "Lb", "Meters", "Cm", "Feet", "Inch", "Gram", "Kg", "Yards"],
        }
        # Map conversion operations to specific methods, return function name
        self.calculations = {
            "Miles_to_Km": self.Miles_to_Km,
            "Miles_to_Meters": self.Miles_to_Meters,
            "Miles_to_Cm": self.Miles_to_Cm,
            "Miles_to_Feet": self.Miles_to_Cm,
            "Miles_to_Inch": self.Miles_to_Inch,
            "Miles_to_Yards": self.Miles_to_Yards,

            "Km_to_Miles": self.Km_to_Miles,
            "Km_to_Meters": self.Km_to_Meter,
            "Km_to_Cm": self.Km_to_Cm,
            "Km_to_Feet": self.Km_to_Feet,
            "Km_to_Inch": self.Km_to_Inch,
            "Km_to_Yards": self.Km_to_Yards,

            "Meters_to_Miles": self.Meters_to_Miles,
            "Meters_to_Km": self.Meters_to_Km,
            "Meters_to_Cm": self.Meters_to_Cm,
            "Meters_to_Inch": self.Meters_to_Inch,
            "Meters_to_Feet": self.Meters_to_Feet,
            "Meters_to_Yards": self.Meters_to_Yards,

            "Cm_to_Inch": self.Cm_to_Inch,
            "Cm_to_Meters": self.Cm_to_Meters,
            "Cm_to_Miles": self.Cm_to_Miles,
            "Cm_to_Km": self.Cm_to_Km,
            "Cm_to_Feet": self.Cm_to_Feet,
            "Cm_to_Yards": self.Cm_to_Yards,

            "Feet_to_Meters": self.Feet_to_Meters,
            "Feet_to_Miles": self.Feet_to_Miles,
            "Feet_to_Km": self.Feet_to_Km,
            "Feet_to_Cm": self.Feet_to_Cm,
            "Feet_to_Inch": self.Feet_to_Inch,
            "Feet_to_Yards": self.Feet_to_Yards,

            "Inch_to_Miles": self.Inch_to_Miles,
            "Inch_to_Km": self.Inch_to_Km,
            "Inch_to_Yards": self.Inch_to_Yards,
            "Inch_to_Meters": self.Inch_to_Meters,
            "Inch_to_Feet": self.Inch_to_Feet,
            "Inch_to_Cm": self.Inch_to_Cm,

            "Yards_to_Miles": self.Yards_to_Miles,
            "Yards_to_Km": self.Yards_to_Km,
            "Yards_to_Inch": self.Yards_to_Inch,
            "Yards_to_Feet": self.Yards_to_Feet,
            "Yards_to_Cm": self.Yards_to_Cm,
            "Yards_to_Meters": self.Yards_to_Meters,

            "Milliliters_to_Liters": self.Milliliters_to_Liters,
            "Milliliters_to_Ounces": self.Milliliters_to_Ounces,
            "Milliliters_to_Gallons": self.Milliliters_to_Gallons,

            "Liters_to_Gallons": self.Liters_to_Gallons,
            "Liters_to_Milliliters": self.Liters_to_Milliliters,
            "Liters_to_Ounces": self.Liters_to_Ounces,

            "Gallons_to_Liters": self.Gallons_to_Liters,
            "Gallons_to_Milliliters": self.Gallons_to_Milliliters,
            "Gallons_to_Ounces": self.Gallons_to_Ounces,

            "Lb_to_Gram": self.Lb_to_Gram,
            "Lb_to_Kg": self.Lb_to_Kg,
            "Lb_to_Ounces": self.Lb_to_Ounces,

            "Grams_to_Kg": self.Grams_to_Kg,
            "Grams_to_Lb": self.Grams_to_Lb,
            "Grams_to_Ounces": self.Grams_to_Ounces,

            "Kg_to_Lb": self.Kg_to_Pounds,
            "Kg_to_Gram": self.Kg_to_Gram,
            "Kg_to_Ounces": self.Kg_to_Ounces,

            "Ounces_to_Kg": self.Ounces_to_Kg,
            "Ounces_to_Gram": self.Ounces_to_Gram,
            "Ounces_to_Lb": self.Ounces_to_Lb,
        }

    def value_converter(self, **kwargs):
        # Extract user input for conversion from kwargs
        option_1 = kwargs["choice_1"]
        option_2 = kwargs["choice_2"]
        value = kwargs["value_1"]

        # If the units are the same, return the value as it is
        if option_1 == option_2:
            return float(value)
        else:
            # Form the conversion key and call the relevant conversion function
            to_convert = option_1 + "_to_" + option_2
            return self.calculations[to_convert](value)

    def valid_conversion_checker(self, choice1):
        # Get the invalid conversions for the selected unit
        conversions_to_remove = self.invalid_conversions.get(choice1)
        # Remove invalid conversions from the second choice options
        self.choices_2 = [unit for unit in self.choices_2 if unit not in conversions_to_remove]

    ##### -------- Functions used for Calculations ------- ####
    @staticmethod
    def Miles_to_Km(miles):
        return float(miles) * 1.60934

    @staticmethod
    def Miles_to_Meters(miles):
        return float(miles) * 1609.34

    @staticmethod
    def Miles_to_Cm(miles):
        return float(miles) * 160934

    @staticmethod
    def Miles_to_Feet(miles):
        return float(miles) * 5280

    @staticmethod
    def Miles_to_Inch(miles):
        return float(miles) * 63360

    @staticmethod
    def Miles_to_Yards(miles):
        return float(miles) * 1760

    @staticmethod
    def Km_to_Miles(km):
        return float(km) / 1.60934

    @staticmethod
    def Km_to_Meter(km):
        return float(km) * 1000

    @staticmethod
    def Km_to_Cm(km):
        return float(km) * 100000

    @staticmethod
    def Km_to_Feet(km):
        return float(km) * 3281

    @staticmethod
    def Km_to_Inch(km):
        return float(km) * 39370

    @staticmethod
    def Km_to_Yards(km):
        return float(km) * 1094

    @staticmethod
    def Meters_to_Miles(meters):
        return float(meters) / 1609.34

    @staticmethod
    def Meters_to_Km(meters):
        return float(meters) / 1000

    @staticmethod
    def Meters_to_Cm(meters):
        return float(meters) * 100

    @staticmethod
    def Meters_to_Inch(meters):
        return float(meters) * 39.37

    @staticmethod
    def Meters_to_Feet(meters):
        return float(meters) / 0.3048

    @staticmethod
    def Meters_to_Yards(meters):
        return float(meters) * 1.09361

    @staticmethod
    def Cm_to_Inch(cm):
        return float(cm) / 2.54

    @staticmethod
    def Cm_to_Meters(cm):
        return float(cm) / 100

    @staticmethod
    def Cm_to_Miles(cm):
        return float(cm) / 160934

    @staticmethod
    def Cm_to_Km(cm):
        return float(cm) / 100000

    @staticmethod
    def Cm_to_Feet(cm):
        return float(cm) / 30.48

    @staticmethod
    def Cm_to_Yards(cm):
        return float(cm) / 91.44

    @staticmethod
    def Feet_to_Meters(feet):
        return float(feet) * 0.3048

    @staticmethod
    def Feet_to_Miles(feet):
        return float(feet) / 5280

    @staticmethod
    def Feet_to_Km(feet):
        return float(feet) / 3281

    @staticmethod
    def Feet_to_Cm(feet):
        return float(feet) * 30.48

    @staticmethod
    def Feet_to_Inch(feet):
        return float(feet) * 12

    @staticmethod
    def Feet_to_Yards(feet):
        return float(feet) / 3

    @staticmethod
    def Inch_to_Miles(inch):
        return float(inch) / 63360

    @staticmethod
    def Inch_to_Km(inch):
        return float(inch) / 39370

    @staticmethod
    def Inch_to_Yards(inch):
        return float(inch) / 36

    @staticmethod
    def Inch_to_Meters(inch):
        return float(inch) / 39.37

    @staticmethod
    def Inch_to_Feet(inch):
        return float(inch) / 12

    @staticmethod
    def Inch_to_Cm(inch):
        return float(inch) * 2.54

    @staticmethod
    def Yards_to_Miles(yards):
        return float(yards) / 1760

    @staticmethod
    def Yards_to_Km(yards):
        return float(yards) / 1094

    @staticmethod
    def Yards_to_Inch(yards):
        return float(yards) * 36

    @staticmethod
    def Yards_to_Feet(yards):
        return float(yards) * 3

    @staticmethod
    def Yards_to_Cm(yards):
        return float(yards) * 91.44

    @staticmethod
    def Yards_to_Meters(yards):
        return float(yards) / 1.09361

    @staticmethod
    def Milliliters_to_Liters(milliliters):
        return float(milliliters) / 1000

    @staticmethod
    def Milliliters_to_Ounces(milliliters):
        return float(milliliters) / 29.574

    @staticmethod
    def Milliliters_to_Gallons(milliliters):
        return float(milliliters) / 3785

    @staticmethod
    def Liters_to_Gallons(liters):
        return float(liters) / 3.78541

    @staticmethod
    def Liters_to_Milliliters(liters):
        return float(liters) * 1000

    @staticmethod
    def Liters_to_Ounces(liters):
        return float(liters) * 33.814

    @staticmethod
    def Gallons_to_Liters(gallons):
        return float(gallons) * 3.78541

    @staticmethod
    def Gallons_to_Milliliters(gallons):
        return float(gallons) * 3785

    @staticmethod
    def Gallons_to_Ounces(gallons):
        return float(gallons) * 128

    @staticmethod
    def Lb_to_Gram(lb):
        return float(lb) * 453.6

    @staticmethod
    def Lb_to_Kg(lb):
        return float(lb) / 2.205

    @staticmethod
    def Lb_to_Ounces(lb):
        return float(lb) * 16

    @staticmethod
    def Grams_to_Kg(grams):
        return float(grams) / 1000

    @staticmethod
    def Grams_to_Lb(grams):
        return float(grams) / 453.6

    @staticmethod
    def Grams_to_Ounces(grams):
        return float(grams) / 28.3495

    @staticmethod
    def Kg_to_Pounds(kg):
        return float(kg) * 2.205

    @staticmethod
    def Kg_to_Gram(kg):
        return float(kg) * 1000

    @staticmethod
    def Kg_to_Ounces(kg):
        return float(kg) * 35.274

    @staticmethod
    def Ounces_to_Kg(ounces):
        return float(ounces) / 35.274

    @staticmethod
    def Ounces_to_Gram(ounces):
        return float(ounces) * 28.3495

    @staticmethod
    def Ounces_to_Lb(ounces):
        return float(ounces) / 16