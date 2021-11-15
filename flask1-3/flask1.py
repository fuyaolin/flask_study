from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def jsonpath1():
    return jsonify({'code': 1000, 'data': [1, 2, 3]})


@app.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        if user == 'fyl' and passwd == 'fyl':
            return redirect('/index')
        else:
            return render_template('login.html', error='用户名或密码错误')


@app.route('/index')
def index():
    return "首页"


if __name__ == '__main__':
    app.run()
