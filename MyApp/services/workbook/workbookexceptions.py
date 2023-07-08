
class InstanceAlreadyCreatedException(Exception) :
    ''' Exception when someone directly calls the initialiser'''
class CreateNewWorksheetException(Exception) :
    ''' Exception raised when there is only one worksheet of current worksheet is full'''
class UnableToGetWorksheetException(Exception):
    ''' Exception raised when unable to find sheetdata.csv file or some exception in getting sheet'''
class UnableToCreateWorksheetException(Exception):
    ''' Exception raised when unable to find sheetdata.csv file or some exception in creating sheet'''