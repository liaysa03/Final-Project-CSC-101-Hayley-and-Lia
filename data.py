import typing

class foodSecurity:

    def __init__(self, popEst, under5, under18, over65, white, black, NA, asian, PI, latinx, mixed, whiteA, rent,
                 under65D, under65HI, incomeH, incomeI, poverty, employment):
        self.popEst = popEst
        self.under5 = under5
        self.under18 = under18
        self.over65 = over65
        self.white = white
        self.black = black
        self.NA = NA
        self.asian = asian
        self.PI = PI
        self.latinx = latinx
        self.mixed = mixed
        self.whiteA = whiteA
        self.rent = rent
        self.under65D = under65D
        self.under65HI = under65HI
        self.incomeH = incomeH
        self.incomeI = incomeI
        self.poverty = poverty
        self.employment = employment

    def __repr__(self):
        return (
            "Population Estimation = {}, Under 5 Years Old = {}, Under 18 Years Old = {}, Over 65 Years Old = {},"
            "Race: White Percentage = {}, Race: Black Percentage = {}, Race: Native American Percentage = {},"
            "Race: Asian Percentage = {},Race: Pacific Islander Percentage = {}, Race: Latinx Percentage = {},"
            "Race: Mixed Percentage = {}, Race: White Alone Percentage = {}, Rent Price = {}, "
            "Under 65 with Disability = {}, Under 65 without Health Insurance = {}, Household Income = {},"
            "Individual Income = {}, Poverty Percentage = {}, Employment Percentage= {}").format(
            self.popEst, self.under5, self.under18, self.over65, self.white, self.black, self.NA, self.asian,
            self.PI, self.latinx, self.mixed, self.whiteA, self.rent, self.under65D, self.under65HI, self.incomeH,
            self.incomeI, self.poverty, self.employment
            )

    def __eq__(self, other):
        return (
                self.popEst == other.popEst and self.under5 == other.under5 and self.under18 == other.under18 and
                self.over65 == other.over65 and self.white == other.white and self.black == other.black and
                self.NA == other.NA and self.asian == other.asian and self.PI == other.PI and self.latinx == other.latinx
                and self.mixed == other.mixed and self.whiteA == other.whiteA and self.rent == other.rent
                and self.under65D == other.under65D and self.under65HI == other.under65HI and
                self.incomeH == other.incomeH and self.incomeI == other.incomeI and self.poverty == other.poverty
                and self.employment == other.employment
        )