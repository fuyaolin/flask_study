from flask import Blueprint, render_template, request, redirect
from flask5.app import db
from flask5.app.models import User


STUDENT = Blueprint('xSTUDENT', __name__)


@STUDENT.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('user')
        passwd = request.form.get('passwd')
        if username == 'fyl' and passwd == 'fyl':
            return redirect('/show')
        else:
            return render_template('login.html', error='用户名或密码错误')


# 查询
@STUDENT.route('/show', methods=['GET', 'POST'])
def show():
    ulist = User.query.all()
    if request.method == 'GET':
        return render_template('show.html', data=ulist)
    else:
        value_list = []
        value = request.form.get('search')
        if value == '':
            value_list = User.query.all()
        else:
            for i in ulist:
                if str(i.id) == value or str(i.age) == value or i.name == value:
                    value_list.append(i)
        return render_template('show.html', data=value_list)


# 增
@STUDENT.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        if id == '' or name == '' or age == '':
            return render_template('add.html', error='id,name,age不能为空')
        else:
            # 声明对象
            user1 = User(id=id, name=name, age=age)
            # 调用添加方法
            db.session.add(user1)
            # 提交入库
            db.session.commit()
            return redirect('/show')


# 数据库的修改操作（改）
@STUDENT.route("/edit", methods=['GET', 'POST'])
def edit_user():
    nid = request.args.get('nid')
    if request.method == 'GET':
        data = User.query.filter_by(id=nid).all()
        return render_template('edit.html', name=data[0].name, age=data[0].age)
    else:
        # 根据某个字段做修改操作
        # 翻译为 update user set name = '张三' where id = 2
        name = request.form.get("user")
        age = request.form.get("age")
        User.query.filter_by(id=nid).update({'name': name, 'age': age})
        return redirect('/show')


# 数据库的删除操作（删）
@STUDENT.route("/del/<int:nid>")
def del_user(nid):
    # 根据某个字段做删除,filter_by可以理解为where条件限定
    # 翻译为 delete from user where id = 1
    User.query.filter_by(id=nid).delete()
    return redirect('/show')
