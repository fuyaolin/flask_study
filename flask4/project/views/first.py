from flask import Blueprint

FIRST = Blueprint('xFIRST', __name__)


@FIRST.route('/FIRST1')
def f1():
    return 'FIRST1'


@FIRST.route('/FIRST2')
def f2():
    return 'FIRST2'