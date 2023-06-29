import webview
import dominate
from string import ascii_letters
from random import choice, randint
from dominate.tags import *
from bottle import route, run, template

bootstrap = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/'
bootswatch = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/'

doc = dominate.document()


@route('/')
def root():
    print('Hi')


if __name__ == "__main__":
    webview.create_window("Not a browser, honest!", "http://localhost:8080",
                          width=800, height=600, resizable=False)
