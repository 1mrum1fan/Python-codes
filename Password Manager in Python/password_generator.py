import string
import random
import passsword_manager_app as app
password_txt=''
length=0

## characters to generate password from
#only alphabets and numbers
alpha_and_num=list(string.ascii_letters+string.digits)
#containes all alphabets,numbers and special characters
all_characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password(length):

	## shuffling the characters
	random.shuffle(all_characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(all_characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	password="".join(password)

	return password




#invoking the function
generate_password(length)