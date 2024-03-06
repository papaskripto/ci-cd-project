from app import app

def test_home():
    ''' Test for home page.'''
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_about():
    ''' Test for about us page.'''
    client = app.test_client()
    response = client.get('/about-us')
    assert response.status_code == 200

def test_contact():
    ''' Test for contact us page.'''
    client = app.test_client()
    response = client.get('/contact-us')
    assert response.status_code == 200

def test_signup():
    ''' Test for the signup page.'''
    pass
