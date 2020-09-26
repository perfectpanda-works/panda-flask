import min_app

def test_first():
    min_app.app.testing = True
    assert min_app.app.test_client().get('/').status_code == 200