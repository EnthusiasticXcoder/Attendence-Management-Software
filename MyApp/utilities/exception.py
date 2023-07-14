class UnableToFindFolderException(Exception) :
    ''' Exception when someone directly calls the initialiser'''

# Login Exceptions
class IncorrectPasswordException(Exception) :
    ''' Exception when Password dosen't match with the password corrosponding with the Username'''
    
class UsernameNotFoundException(Exception) :
    ''' Exception when Username dosen't exist in logindata.csv file'''

class UnableToDeleteException(Exception) :
    ''' Exception raised when unable to Delete'''

class CannotDeleteCurrentLoginUserException(Exception) :
    ''' Exception raised when Given Username Is Cuttent Login Username '''

# Workbook Exceptions
class CreateNewWorksheetException(Exception) :
    ''' Exception raised when there is only one worksheet of current worksheet is full'''
class UnableToGetWorksheetException(Exception):
    ''' Exception raised when unable to find sheetdata.csv file or some exception in getting sheet'''
class UnableToCreateWorksheetException(Exception):
    ''' Exception raised when unable to find sheetdata.csv file or some exception in creating sheet'''