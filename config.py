# Activates the cross-site request forgery prevention
WTF_CSRF_ENABLED = True

# Used to create a cryptographic token that is used to validate a form; only needed when CSRF is enabled
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '666484943458211',
        'secret': '8bbdfb41da1283d8f2d696580e271267'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
