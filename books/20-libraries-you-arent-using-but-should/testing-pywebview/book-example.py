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

with doc:
    with div(cls='container'):
        with h1():
            span(cls='glyphicon glyphicon-map-marker') span('My Heading')
        with div(cls='row'):
            with div(cls='col-sm-6'):
                p('{{body}}')
            with div(cls='col-sm-6'):
                p('Evaluate an expression:')
                input_(id='expression', type='text')
                button('Evaluate', cls='btn btn-primary')
                div(style='margin-top: 10px;')
                with div(cls='dropdown'):
                    with button(cls="btn btn-default dropdown-toggle",
                                type="button", data_toggle='dropdown'):
    span('Dropdown') span(cls='caret')
    items = ('Action', 'Another action',
    'Yet another action')
    ul((li(a(x, href='#')) for x in items), cls='dropdown-menu')