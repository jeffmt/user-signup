from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def signup():
    return render_template('signup.html')

@app.route("/verify", methods=['POST'])
def verify():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    if not username:
        return render_template('signup.html', username_error = "Username cannot be left blank")

    if email:
        if len(email) < 3 or len(email) > 20:
            return render_template('signup.html', username = username, email = email, email_error = "Email should be between 3 and 20 characters long")

        if email.count('@') != 1:
            return render_template('signup.html', username = username, email = email, email_error = "Email should have one @ symbol")

        if email.count('.') != 1:
            return render_template('signup.html', username = username, email = email, email_error = "Email should have one . symbol")

        if email.count(' ') > 0:
            return render_template('signup.html', username = username, email = email, email_error = "Email should not have spaces")

    if not password: 
        return render_template('signup.html', username = username, email = email,password_error = "Password cannot be left blank")
    if not verify_password: 
        return render_template('signup.html', username = username, email = email,verify_password_error = "Verify password cannot be left blank")

    if len(username) < 3 or len(username) > 20:
        return render_template('signup.html', username = username, email = email,username_error = "Username should be between 3 and 20 characters long")

    if username.count(' ') > 0:
        return render_template('signup.html', username = username, email = email,username_error = "Username cannot contain a space")

    if len(password) < 3 or len(password) > 20:
        return render_template('signup.html', username = username, email = email,password_error = "Password should be between 3 and 20 characters long")

    if password.count(' ') > 0:
        return render_template('signup.html', username = username, email = email,password_error = "Password cannot contain a space")

    if password != verify_password:
        return render_template(
                'signup.html', 
                username = username, 
                email = email,
                password_error = "Password does not match verify password", 
                verify_password_error = "Verify password does not match password"
                )

    return render_template('welcome.html', username = username)

app.run()
