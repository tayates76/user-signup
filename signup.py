from flask import Flask, redirect, request, render_template



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def login_display():
    return render_template('form_temp.html')


@app.route('/validate', methods=['POST', 'GET'])
def validate_form():
    

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if request.method == "POST":
        username = request.form['username']
        password= request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']
    

    

    if username == "":
        username_error = "A username is required to continue."
    elif " " in username:
        username_error = "The username cannot contain any spaces."
    elif len(username)<3 or len (username)>20:
        username_error = "The username should be between 3 and 20 characters."

    if password == "":
        password_error = "A password is required to continue."
    elif " " in password:
        password_error = "The password cannot contain any spaces."
    elif len(password)<3 or len (password)>20:
        password_error = "The password should be between 3 and 20 characters."
    
    if password != verify_password:
        verify_password_error = "The passwords do not match."

    if email !="":

        if " " in email:
            email_error = "The email cannot contain any spaces."
        elif "@" not in email or "." not in email:
            email_error = "The email is not valid."
        elif len(email)>20 or len(email)<3:
            email_error = "The email should be between 3 and 20 characters."

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('form_temp.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, email=email)

if __name__=="__main__":
    app.run()

    




    



