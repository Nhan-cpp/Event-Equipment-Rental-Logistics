from utils.utils import validate_ID

class Equipment():
    MIN_ID_LEN = 4
    MAX_ID_LEN = 20

    def __init__(self,Id = "",powerRating = 0.0,hourlyRentalRate = 0.0,currentStatus = True):
        self._Id = ""
        self._powerRating = 0.0
        self._hourlyRentalRate = 0.0
        self._currentStatus = True

        if Id != "":
            self.Id = Id
        if powerRating != 0.0:
            self.powerRating = powerRating
        if hourlyRentalRate != 0.0:
            self.hourlyRentalRate = hourlyRentalRate
        self.currentStatus = currentStatus

    def __str__(self):
        return f"ID: {self._Id} | Power: {self._powerRating} | Rate: {self._hourlyRentalRate} | Status: {self.currentStatus}"

    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value : str):
        if(len(new_value) < self.MIN_ID_LEN or self.MAX_ID_LEN < len(new_value)):
            raise ValueError(f"Equipment id need length from {self.MIN_ID_LEN} to {self.MAX_ID_LEN}")
        if(validate_ID(new_value) == False):
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
        return "Available" if self._currentStatus else "Rented"
    @currentStatus.setter
    def currentStatus(self,new_value):
        if isinstance(new_value, str):
            val = new_value.strip().lower()
            if val in ["available", "true"]:
                new_value = True
            elif val in ["rented", "false"]:
                new_value = False
                
        if not isinstance(new_value, bool):
            raise ValueError("Equipment current status must be 'Available'/'Rented' or True/False.")
        self._currentStatus = new_value
