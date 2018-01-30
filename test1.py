import orm
from models import User, Blog, Comment

def test():
	yield from orm.create_pooi(user = 'www-data',password = 'www-data',database= 'awesome')

	u =User(name = 'test', email = 'test@example.com',password ='1234567890',image = 'about:blank')

	yield from u.save()

for x in test():
	pass