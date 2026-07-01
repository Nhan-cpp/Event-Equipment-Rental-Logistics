from utils.utils import validate_ID

class Rental():
    _Id = None
    _clientName = None
    _startTime = None
    _expectedReturnTime = None

    def __init__(self,Id,clientName,startTime,expectedReturnTime):
        self._Id = Id
        self._clientName = clientName
        self._startTime = startTime
        self._expectedReturnTime = expectedReturnTime
    
    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value):
        if(validate_ID(new_value) == True):
            self._Id = new_value
    
    @property
    def clientName(self):
        return self._clientName
    @clientName.setter
    def clientName(self,new_value):
        try:
            self._clientName = str(new_value)
        except:
            raise ValueError("client name have some error.")
    @property
    def startTime(self):
        return self._startTime
    @startTime.setter
    def startTime(self,new_value):
        try:
            self._startTime = new_value
        except:
            raise ValueError("Need be a time format.")
    @property
    def expectedReturnTime(self):
        return self._expectedReturnTime
    @expectedReturnTime.setter
    def expectedReturnTime(self,new_value):
        try:
            if(self._startTime >= new_value):
                self._expectedReturnTime = new_value
        except:
            raise ValueError("expected return time have some error.")        