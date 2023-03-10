from urllib import request

from pip._internal.network import session


class User:
    pass


if request.method == 'POST':
    Name = request.form['Name']
    Username = request.form['Username']
    Password = request.form['Password']
    Email = request.form['Email']
    Confirm = request.form['Confirm']
    user = User.query.filter_by(Username=Username).first()
    if user:
        username_failure = "Username already taken."
    else:
        if Password == Confirm:

        else:
            password_match = "Passwords are not same!"


def login_user(user):
    pass


def login(password_failure=None, name_failure=None):
	if request.method == 'GET':

	else:
		Username = request.form['Username']
		Password = request.form['Password']

		if user:
			if user.Password == Password:
				login_user(user)
				session['Name'] = user.Name
				session['Username'] = user.Username

			else:
                password_failure = "Password failure!"

		else:
			name_failure = "Username not found!"


def logout_user():
    pass


def log_out():
	logout_user()
	print(session.get('Name') + " has logged out.")
	return 'Logged out.'

def open(name):
    print(f'Python Bootcamp Ödev01, {name}')


def render_template(param):
    pass


def home():
    return render_template('index.html')


if __name__ == '__main__':
    open('Kullanıcı')
