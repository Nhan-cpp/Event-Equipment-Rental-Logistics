from utils.utils import validate_ID

class Equipment():
    _Id = None
    _powerRating = None
    _hourlyRentalRate = None
    _currentStatus = None
    MIN_ID_LEN = 8
    MAX_ID_LEN = 20

    def __init__(self,Id,powerRating,hourlyRentalRate,currentStatus):
        self._Id = Id
        self._powerRating = powerRating
        self._hourlyRentalRate = hourlyRentalRate
        self._currentStatus = currentStatus
    
    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value : str):
        if(len(new_value) < self.MIN_ID_LEN and self.MAX_ID_LEN < len(new_value)):
            raise ValueError(f"Equipment id need length from {self.MIN_ID_LEN} to {self.MAX_ID_LEN}")
        for character in new_value:
            if not character.isalnum():
                raise ValueError("Equipment Id only contain character or digit.")
        self._Id = new_value
    @property
    def powerRating(self):
        return self._powerRating
    @powerRating.setter
    def powerRating(self,new_value):
        try:
            new_value = float(new_value)
        except ValueError:
            raise ValueError("Equipment power rating must be a number.")
        
        if new_value <= 0.0:
            raise ValueError("Equipment power rating must be greater than 0.")
            
        self._powerRating = new_value
    @property
    def hourlyRentalRate(self):
        return self._hourlyRentalRate
    @hourlyRentalRate.setter
    def hourlyRentalRate(self,new_value):
        try:
            new_value = float(new_value)
        except ValueError:
            raise ValueError("Equipment hourly rental rate must be a number.")
            
        if new_value <= 0.0:
            raise ValueError("Equipment hourly rental rate must be greater than 0.")
            
        self._hourlyRentalRate = new_value
    @property
    def currentStatus(self):
        return self._currentStatus
    @currentStatus.setter
    def currentStatus(self,new_value):
        try:
            self._currentStatus = bool(new_value)
        except:
            raise ValueError("Equipment current status need be a boolean.")
    