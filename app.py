from flask import Flask, request, render_template, url_for

app = Flask(__name__)


user_auth = {'Saichandar':'123456'}

@app.route('/')
def index():
    return "welcome to flask log in page"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    print('login page')
    print('request', request.method)
    if request.method == 'POST':
        print('request.form', request.form['name'])
        name = request.form['name']
        password = request.form['password']
        # print(name=='Saichandar', password)
        if name in user_auth:
            print('user exits')
            if user_auth[name] == password:
                return url_for('login_success')

            #return
            # return render_template()
    return render_template('login.html')
    # return """<form method='post'><input type='text' id='name'>
    # <input type='text' id='password'>
    # <input type='submit' value='SUBMIT'>
    # </form>"""


@app.route('/login_success', methods=['GET','POST'])
def login_success():
    return 'welcome {0}, you are logged in successfully'.format(request.form['name'])

app.run(port=5012)

