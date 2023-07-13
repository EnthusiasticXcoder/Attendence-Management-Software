from MyApp.services.login.LoginService import LoginService


print('''
============================================================================================
    ----------------------------------------------------------------------------------
============================================================================================\n\n''')
service = LoginService.getInstance()
Username =input('Username : ')
Password = input('Password : ')
if service.CheackUserName(Username):
    service.CreateLogin(Username, Password,isadmin=True)
    print('\n\nLogin created successfully\n\n')
    print(f'Username : {Username} and Password : {Password}')