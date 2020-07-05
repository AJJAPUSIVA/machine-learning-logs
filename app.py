from flask import Flask, render_template, redirect, url_for, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='/var/log/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
                    
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            logging.error("Invalid Credentials!", exc_info=True)
        else:
            logging.info("success!", exc_info=True)
            return redirect('https://i.pinimg.com/originals/78/ac/aa/78acaad3c2890c0d47f94ec7b3cce9fb.jpg')
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

