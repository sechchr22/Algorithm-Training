"""
Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

Note: Do not use ternary operators!
"""
from typing import Union

class Package():
    VOLUME_LIMIT = 1000000

    def __init__(self,
                 width: Union[int, float],
                 height: Union[int, float],
                 length: Union[int, float],
                 mass: Union[int, float]
                ):
        if not Package.validator(width, height, length, mass):
            raise Exception("Please provide correct values for package info")
        self.width = round(width)
        self.height = round(height)
        self.lenght = round(length)
        self.mass = round(mass)
    
    @staticmethod
    def validator(width, height, length, mass):
        if any(not isinstance(val, (int, float)) for val in [width, height, length, mass]):
            return False
        if any(val < 0 for val in [width, height, length, mass]):
            return False
        return True
    
    @property
    def volume(self) -> int:
        """Package volume in cm3"""
        return self.width*self.height*self.lenght

    
    def sort(self) -> str:
        """
            Sorts package depending on volumn and mass
            Returns: string telling the category
        """
        category = []
        if any(value >= 150 for value in [self.width, self.height, self.lenght]) or self.volume >= self.VOLUME_LIMIT:
            category.append("bulky")
        if self.mass >= 20:
            category.append("heavy")
        
        if "bulky" in category and "heavy" in category:
            return "REJECTED"
        elif "bulky" in category or "heavy" in category:
            return "SPECIAL"
        else:
            return "STANDARD"

if __name__ == "__main__":
    # I would write a unit test for each case
    # but for simplicity on having it in just 1 file i will test this way
    #--------------------------------------------------------------------
    # Standard
    print("------STANDARD PACKAGES------")
    standard = Package(20, 30, 10, 10)
    if standard.sort() != "STANDARD":
        print("test case package: {} failed".format(vars(standard)))
    else:
        print("test case package: {} succeded".format(vars(standard)))
    # Special
    print("------SPECIAL PACKAGES------")
    special = []
    special.append(Package(20, 30 , 10, 20)) # mass equal to 20
    special.append(Package(20, 30 , 10, 30)) # mass greater than 20
    special.append(Package(150, 10, 10, 10)) # width equal to 150
    special.append(Package(10, 150, 10, 10)) # height equal to 150
    special.append(Package(10, 10, 150, 10)) # lenght equal to 150
    special.append(Package(151, 10, 10, 10)) # width greater than 150
    special.append(Package(10, 151, 10, 10)) # height greater than 150
    special.append(Package(10, 10, 151, 10)) # lenght greater than 150
    special.append(Package(100, 100, 100, 10)) # volume equal to 1.000.000
    special.append(Package(101, 100, 100, 10)) # volume greater than 1.000.000
    special.append(Package(20, 30 , 10, 19.99)) # rounded mass equal to 20
    special.append(Package(149.99, 10, 10, 10)) # rounded width equal to 150
    special.append(Package(10, 149.99, 10, 10)) # rounded height equal to 150
    special.append(Package(10, 10, 149.99, 10)) # rounded lenght equal to 150
    for package in special:
        if package.sort() != "SPECIAL":
            print("test case package: {} failed".format(vars(package)))
        else:
            print("test case package: {} succeded".format(vars(package)))
    # Rejected
    print("------REJECTED PACKAGES------")
    rejected = []
    rejected.append(Package(150, 10, 10, 20)) # width equal to 150 and mass equal to 20
    rejected.append(Package(10, 150, 10, 20)) # height equal to 150 and mass equal to 20
    rejected.append(Package(10, 10, 150, 20)) # lenght equal to 150 and mass equal to 20
    rejected.append(Package(151, 10, 10, 20)) # width greater than 150 and mass equal to 20
    rejected.append(Package(10, 151, 10, 20)) # height greater than 150 and mass equal to 20
    rejected.append(Package(10, 10, 151, 20)) # lenght greater than 150 and mass equal to 20
    rejected.append(Package(100, 100, 100, 20)) # volume equal to 1.000.000 and mass equal to 20
    rejected.append(Package(101, 100, 100, 20)) # volume greater than 1.000.000 and mass equal to 20
    for package in rejected:
        if package.sort() != "REJECTED":
            print("test case package: {} failed".format(vars(package)))
        else:
            print("test case package: {} succeded".format(vars(package)))
    # Wrong input
    print("------WRONG INPUT------")
    try:
        Package("22", 4, 5, 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, "4", 5, 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, 4, "5", 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, 4, 5, "20")
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(-22, 4, 5, 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, -4, 5, 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, 4, -5, 20)
        print("test case failed")
    except Exception:
        print("test case succeded")
    try:
        Package(22, 4, 5, -20)
        print("test case failed")
    except Exception:
        print("test case succeded")
