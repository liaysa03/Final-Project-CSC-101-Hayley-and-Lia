# countyClass.py  (ONLY required change: store the original dict on the object)

class County:

    def __init__(self, data_dict):
        self.data = data_dict

        self.popEst = data_dict["Population estimates (July 1, 2024)"]
        self.under5 = data_dict["Persons under 5 years (%)"]
        self.under18 = data_dict["Persons under 18 years (%)"]
        self.over65 = data_dict["Persons 65 years and over (%)"]
        self.white = data_dict["White alone (%)"]
        self.black = data_dict["Black alone (%)"]
        self.NA = data_dict["American Indian and Alaska Native alone (%)"]
        self.asian = data_dict["Asian alone (%)"]
        self.PI = data_dict["Native Hawaiian and Other Pacific Islander alone (%)"]
        self.latinx = data_dict["Hispanic or Latino (%)"]
        self.mixed = data_dict["Two or More Races (%)"]
        self.whiteA = data_dict["White alone, not Hispanic or Latino (%)"]
        self.rent = data_dict["Median gross rent (2020–2024)"]
        self.under65D = data_dict["With a disability, under age 65 years (%)"]
        self.under65HI = data_dict["Persons without health insurance, under age 65 years (%)"]
        self.incomeH = data_dict["Median household income (2024 dollars)"]
        self.incomeI = data_dict["Per capita income (2024 dollars)"]
        self.poverty = data_dict["Persons in poverty (%)"]
        self.employment = data_dict["Total employment (2023)"]
        self.childrenLA = data_dict["Children,low access to store (2019)"]
        self.seniorLA = data_dict["Seniors, low access to store (2019)"]
        self.whiteLA = data_dict["White, low access to store (2019)"]
        self.blackLA = data_dict["Black, low access to store (2019)"]
        self.latinxLA = data_dict["Hispanic, low access to store (2019)"]
        self.asianLA = data_dict["Asian, low access to store (2019)"]
        self.NALA = data_dict["American Indian or Alaska Native, low access to store (2019)"]
        self.PILA = data_dict["Hawaiian or Pacific Islander, low access to store (2019)"]
        self.FDPIR = data_dict["FDPIR Sites(2015)"]
        self.foodbank = data_dict["Food Banks (2021)"]
        self.SNAP = data_dict["SNAP Authorized Stores"]
        self.WIC = data_dict["WIC Authorized Stores"]
        self.groceryStore = data_dict["Grocery stores (2020)"]

    def __repr__(self):
        return (
            "Population Estimation = {}, Under 5 Years Old = {}, Under 18 Years Old = {}, Over 65 Years Old = {},"
            "Race: White Percentage = {}, Race: Black Percentage = {}, Race: Native American Percentage = {},"
            "Race: Asian Percentage = {},Race: Pacific Islander Percentage = {}, Race: Latinx Percentage = {},"
            "Race: Mixed Percentage = {}, Race: White Alone Percentage = {}, Rent Price = {}, "
            "Under 65 with Disability = {}, Under 65 without Health Insurance = {}, Household Income = {},"
            "Individual Income = {}, Poverty Percentage = {}, Employment Percentage= {}, "
            "Children with Low Access to Stores Percentage = {}, Seniors with Low Access to Stores Percentage = {},"
            "White People with Low Access to Stores Percentage = {}, Black People with Low Access to Stores Percentage = {},"
            "LatinX People with Low Access to Stores Percentage = {}, Asian People with Low Access to Stores Percentage = {},"
            "Native American People with Low Access to Stores Percentage = {}, Pacific Islanders with Low Access to Stores Percentage = {},"
            "Number of FDPIR Sites = {}, Number of Food Banks = {}, Number of SNAP Stores = {}, Number of WIC Stores"
            "Number of Grocery Stores").format(
            self.popEst, self.under5, self.under18, self.over65, self.white, self.black, self.NA, self.asian,
            self.PI, self.latinx, self.mixed, self.whiteA, self.rent, self.under65D, self.under65HI, self.incomeH,
            self.incomeI, self.poverty, self.employment, self.childrenLA, self.seniorLA, self.whiteLA, self.blackLA, self.latinxLA,
            self.asianLA, self.NALA, self.PILA, self.FDPIR, self.foodbank, self.SNAP, self.WIC, self.groceryStore
        )

    def __eq__(self, other):
        return (
            self.popEst == other.popEst and self.under5 == other.under5 and self.under18 == other.under18 and
            self.over65 == other.over65 and self.white == other.white and self.black == other.black and
            self.NA == other.NA and self.asian == other.asian and self.PI == other.PI and self.latinx == other.latinx
            and self.mixed == other.mixed and self.whiteA == other.whiteA and self.rent == other.rent
            and self.under65D == other.under65D and self.under65HI == other.under65HI and
            self.incomeH == other.incomeH and self.incomeI == other.incomeI and self.poverty == other.poverty
            and self.employment == other.employment and self.childrenLA == other.childrenLA and self.seniorLA == other.seniorLA
            and self.whiteLA == other.whiteLA and self.blackLA == other.blackLA and self.latinxLA == other.latinxLA
            and self.asianLA == other.asianLA and self.NALA == other.NALA and self.PILA == other.PILA and
            self.FDPIR == other.FDPIR and self.foodbank == other.foodbank and self.SNAP == other.SNAP and
            self.WIC == other.WIC and self.groceryStore == other.groceryStore
        )