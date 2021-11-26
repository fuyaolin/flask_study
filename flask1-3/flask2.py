from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DATA_DICT = {
    '1': {'name': 'baby', 'age': 12},
    '2': {'name': 'linda', 'age': 18}
}


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get('user')
        passwd = request.form.get('passwd')
        if user == 'fyl' and passwd == 'fyl':
            return redirect('/index')
        else:
            return render_template('register.html', error='用户名或密码错误')


@app.route('/index', endpoint='idx')
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)


# 通过get请求接收参数
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    nid = request.args.get('nid')
    if request.method == 'GET':
        info = DATA_DICT[nid]
        return render_template('edit.html', info=info)
    else:
        user = request.form.get("user")
        age = request.form.get("age")
        DATA_DICT[nid]['name'] = user
        DATA_DICT[nid]['age'] = age
        return redirect(url_for("idx"))


# 通过url后参数接收值，默认字符串，int转换类型
@app.route('/del/<int:nid>')
def delect(nid):
    del DATA_DICT[str(nid)]
    # return redirect('/index')
    return redirect(url_for("idx"))


if __name__ == '__main__':
    app.run()
