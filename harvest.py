############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType ("musk", 1998, "green", True, True,"Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f" - {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dictionary = {}
    for melon in melon_types:
        if melon not in melon_dictionary:
            melon_dictionary[melon.code] = melon
    return melon_dictionary


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape, color, field, harvester):
        """ Initializes melon instance"""
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self):
        """ Determines if melon can be sold """
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []
    melons_dictionary = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_dictionary["yw"], 8, 7, 2, "Shiela")
    melon_2 = Melon(melons_dictionary["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_dictionary["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_dictionary["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_dictionary["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_dictionary["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_dictionary["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_dictionary["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_dictionary["yw"], 7, 10, 3, "Michael")

    melons.extend(
        [
            melon_1,
            melon_2,
            melon_3,
            melon_4,
            melon_5,
            melon_6,
            melon_7,
            melon_8,
            melon_9,
        ]
    )

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        sellable = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"Harvested by {melon.harvester} from Field {melon.field} ({sellable})")
