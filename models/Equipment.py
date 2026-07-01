from utils.utils import validate_ID

class Equipment():
    _Id = None
    _powerRating = None
    _hourlyRentalRate = None
    _currentStatus = None
    
    def __init__(self,Id,powerRating,hourlyRentalRate,currentStatus):
        self._Id = Id
        self._powerRating = powerRating
        self._hourlyRentalRate = hourlyRentalRate
        self._currentStatus = currentStatus
    
    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value):
        if(validate_ID(new_value) == True):
            self._Id = new_value
    @property
    def powerRating(self):
        return self._powerRating
    @powerRating.setter
    def powerRating(self,new_value):
        try:
            new_value = float(new_value)
            if(new_value < 0.0):
                return
            self._powerRating = new_value
        except:
            raise ValueError("Need be a number and greater than 0")
    @property
    def hourlyRentalRate(self):
        return self._hourlyRentalRate
    @hourlyRentalRate.setter
    def hourlyRentalRate(self,new_value):
        try:
            new_value = float(new_value)
            if(new_value < 0.0):
                return
            self._hourlyRentalRate = new_value
        except:
            raise ValueError("Need be a number and greater than 0")
    @property
    def currentStatus(self):
        return self._currentStatus
    @currentStatus.setter
    def currentStatus(self,new_value):
        try:
            self._currentStatus = bool(new_value)
        except:
            raise ValueError("Need be a boolean.")
    