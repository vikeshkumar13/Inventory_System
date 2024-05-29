from First_Code import main_function, normal_user
def select_user():
    try:

        user_name = input('ENTER USER NAME->')

        if user_name == 'vikesh':
            print('**************WELCOME***********\n', user_name)
            print('you are admin: '+user_name)
            main_function()
        else: 
            print('**************WELCOME***********\n', user_name)
            print('you are normal user: '+user_name)
            normal_user()
    except Exception as e:
        print('Invalid input', e)
        
select_user()