from string import ascii_letters
from random import choice, randint
import webview
import dominate
from dominate.tags import *
from bottle import route, run, template

bootstrap = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/'
bootswatch = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/'

doc = dominate.document()
with doc.head:
    link(rel='stylesheet',
         href=bootstrap + 'css/bootstrap.min.css')
    link(rel='stylesheet',
         href=bootswatch + 'paper/bootstrap.min.css')
    script(src='https://code.jquery.com/jquery-2.1.1.min.js')
    [script(src=bootstrap + 'js/' + x)
     for x in ['bootstrap.min.js', 'bootstrap-dropdown.js']]
