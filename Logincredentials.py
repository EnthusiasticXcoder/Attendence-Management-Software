from MyApp.services.login.LoginService import LoginService


print('''
============================================================================================
    ----------------------------------------------------------------------------------
============================================================================================\n\n''')
service = LoginService.getInstance()
Username =input('Username : ')
Password = input('Password : ')
if service.CheackUserName(Username):
    logindata = service.CreateLogin(Username, Password)
    print('\n\nLogin created successfully\n\n')
    print(logindata)