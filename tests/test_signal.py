from flask import template_rendered

import min_app

from blinker import Namespace

def say_hello(sender):
    print("Hello")

def test_my_signal():
    my_signals = Namespace()
    model_saved = my_signals.signal('model-saved')
    model_saved.connect(say_hello)
    model_saved.send(min_app.app)
    assert 0 == 1