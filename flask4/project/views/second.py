from flask import Blueprint

SECOND = Blueprint('xSECOND', __name__)


@SECOND.route('/SECOND1')
def f1():
    return 'SECOND1'


@SECOND.route('/SECOND2')
def f2():
    return 'SECOND2'