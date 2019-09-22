#coding=utf-8

from flask import Flask
from person.xb import XB
from person.pic import getpictest

from bs4 import BeautifulSoup



app = Flask(__name__)


def sum(*numbers,multiple=1):
    total = 0
    for number in numbers:
        total += number
    return total

# print(sum(100,200,300,100));

def show_info(sep=':',**info):
    print("--------show-------")
    for key,value in info.items():
        print('{0} {2} {1}'.format(key,value,sep))

# show_info(name='xiongben',age=26,love="copy")
# myinfo_dict = {'name':'xiongben','age':26,'love':'coding'}
# show_info(**myinfo_dict,sport='football',sep='=>')

def testClassMethod():
    xiongben = Person("football","media")
    xiongben.eat()
    print('the weight of xiongben is {0}'.format(xiongben.weight))
    xiongben.weight = 140
    print('the weight of xiongben is {0}'.format(xiongben.weight))
    Person.occupation("web engineer")
 

# testClassMethod()

# school1 = School()
# print(XB)
# xb1 = XB(27)
getpictest()



@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(debug=True)