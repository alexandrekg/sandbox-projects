import webview
import dominate
from string import ascii_letters
from random import choice, randint
from dominate.tags import *
from bottle import route, run, template

bootstrap = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/'
bootswatch = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/'

doc = dominate.document()

def root():
    print('Hi')


if __name__ == "__main__":
    root()