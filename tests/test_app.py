from app import app

def test_home():
    ''' Test for home page.'''
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
