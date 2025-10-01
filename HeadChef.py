class HeadChef:
    """
    Head Chef class.
    """


    _company_name = "Sky Chefs"

    def __init__(self, name, specialty):
        self.__specialty = specialty
        self.__name = name
        self.nickname = name[:3]


    
    def cook(self):
        """
        Makes them cook.
        """
        print(f"Cooking {self.specialty}")
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        

    @property
    def specialty(self):
        return self.__specialty
    
    @specialty.setter
    def specialty(self,specialty):
        self.specialty = specialty


    @classmethod
    def get_company_name(self):
        return _company_name
    

    def __str__(self):
        return f"name: {self.name} specialty: {self.specialty}"
