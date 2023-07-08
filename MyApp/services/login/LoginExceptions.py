
class InstanceAlreadyCreatedException(Exception) :
    ''' Exception when someone directly calls the initialiser'''

class UnableToCreateNewUserException(Exception) :
    ''' Exception raised when file not found and unable to create user'''

class IncorrectPasswordException(Exception) :
    ''' Exception when Password dosen't match with the password corrosponding with the Username'''
    
class UsernameNotFoundException(Exception) :
    ''' Exception when Username dosen't exist in logindata.csv file'''

class UnableToLoginException(Exception) :
    ''' Exception raised when file not found or unable to login'''

class UnableToDeleteException(Exception) :
    ''' Exception raised when unable to Delete'''
