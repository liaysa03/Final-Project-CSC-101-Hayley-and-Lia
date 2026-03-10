class County:

    def __init__(self, popEst, under5, under18, over65, white, black, NA, asian, PI, latinx, mixed, whiteA, rent,
                 under65D, under65HI, incomeH, incomeI, poverty, employment, childrenLA, seniorLA, whiteLA, blackLA,
                 latinxLA, asianLA, NALA, PILA, FDPIR, foodbank, SNAP, WIC, groceryStore):
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
        self.childrenLA = childrenLA
        self.seniorLA = seniorLA
        self.whiteLA = whiteLA
        self.blackLA = blackLA
        self.latinxLA = latinxLA
        self.asianLA = asianLA
        self.NALA = NALA
        self.PILA = PILA
        self.FDPIR = FDPIR
        self.foodbank = foodbank
        self.SNAP = SNAP
        self.WIC = WIC
        self.groceryStore = groceryStore

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
            self.incomeI, self.poverty, self.employment, self.childrenLA, self.whiteLA, self.blackLA, self.latinxLA,
            self.asianLA, self.NALA, self.PILA, self.FDPIR, self.foodbank, self.SNAP, self.WIC , self.groceryStore
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