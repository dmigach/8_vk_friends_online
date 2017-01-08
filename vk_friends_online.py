import vk
import getpass

APP_ID = 5799847


def get_user_login():
    return(input('Enter your login (e-mail or '
                 'telephone number in +7xxxxxxxxxx form)\n'))


def get_user_password():
    return getpass.getpass('Enter your password\n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids)


def output_friends_online(friends_online_list):
    print('Online friends are:\n')
    for friend in friends_online_list:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    user_login = get_user_login()
    user_password = get_user_password()
    try:
        friends_online = get_online_friends(user_login, user_password)
        output_friends_online(friends_online)
    except vk.exceptions.VkAuthError:
        pass
        # vk library is printing pretty self-explaining and clear error
        # to console, so there is no need to print something custom
