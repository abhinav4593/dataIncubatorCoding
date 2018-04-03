from flask_testing import TestCase
from flask import url_for
import unittest
from app import app
from StringIO import *
class FlaskTestCase(TestCase):

    def create_app(self):
        app.config['TESTING']=True
        return app

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_index_loads(self):
        """Ensure index page loads correctly."""
        response = self.client.get('/', follow_redirects=True)
        print(response)
        self.assert200(response)
        self.assertTemplateUsed('index.html')

    def test_post(self):
        data={}
        """Ensure index page loads correctly."""
        with open("D:\PycharmProjectFiles\dataIncubator\imgTest\houston-cougars.jpg",'r') as img1:
            imgStringIO1 = StringIO(img1.read())
        data['file'] = (imgStringIO1, 'houston-cougars.jpg')
        response = self.client.post(url_for('upload_file'), data=data, follow_redirects=True, content_type='multipart/form-data')
        self.assertTemplateUsed('template.html')
        self.assert200(response)

if __name__ == '__main__':
    unittest.main()