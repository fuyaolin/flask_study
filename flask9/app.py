"""
查询关键字
import keyword
print(keyword.kwlist)
"""


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

# 配置参数SECRET_KEY
app.config["SECRET_KEY"] = "asdf"


# 定义表单的模型类
class RegisterFrom(FlaskForm):
    """自定义的注册表单模型类"""
    # StringField,PasswordField的参数分别是 模块名字，对应验证器
    # DataRequired 保证数据必须填写，并且不能为空
    user_name = StringField(label=u"用户名", validators=[DataRequired(u"用户名不能为空")])
    user_password = PasswordField(label=u"密码", validators=[DataRequired(u"密码不能为空")])
    same_password = PasswordField(label=u"确认密码",
                                  validators=[DataRequired(u"密码不能为空"), EqualTo("user_password", u"两次密码不一致")])

    submit = SubmitField(label="提交")


@app.route("/")
def index():
    form = RegisterFrom()
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
