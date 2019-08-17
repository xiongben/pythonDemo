#coding=utf-8

from flask import Flask

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

@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(debug=True)