class Customer:
    def __init__(self, id, name, country, city):
        self._id = id
        self._name = name
        self._country = country
        self._city = city

    def setID(self, id):
        self._id = id
    
    def setName(self, name):
        self._name = name

    def setLocation(self, city, country):
        self._city = city
        self._country = country
    
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name

    def getCountry(self):
        return self._country
    
    def getCity(self):
        return self._city
    
    def __str__(self):
        return f"ID: {str(self._id).zfill(3)}, Name: {self._name}, Location: {self._city}, {self._country}"
    
    def nameIDString(self):
        return f"{self._id},{self._name}"
    
    def locationString(self):
        return f"{self._country},{self._city}"