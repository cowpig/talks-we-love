import json

def set_password(username, password):
	try:
		salted = password + open('salt.txt', 'rb').read()
		pw_hash = hash(salted)
		with open("user_info.json", 'rb') as f:
			users = json.load(f)
		if username in users:
			return (False, "Username already taken")
		users[username] = password
		with open("user_info.json", 'wb') as f:
			json.dump(users, f)
		return (True, "Cows eat grass!")
	except Exception as e:
		print e
		return (False, e.msg())

def check_password(username, password):
	salted = password + open('salt.txt', 'rb').read()
	pw_hash = hash(salted)
	with open("user_info.json", 'rb') as f:
		users = json.load(f)

	return username in users and pw_hash == users[username]

class Talk(object):
	def __init__(self, name, url, img):
		self.name = name
		self.url = url
		self.img = img

	def serialize(self):
		return json.dumps({
				'name':name,
				'url':url,
				'img':img
			})

	def deserialize(str):
		return Talk(**json.loads(str))