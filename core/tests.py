from django.test import TestCase

from .models import *


class HomepageTestCase(TestCase):
    def test_open_homepage_should_success(self):
        response = self.client.get("/")
        assert response.status_code == 200

        response_1 = self.client.get("/workers")
        assert response_1.status_code == 301

    def test_post_request_homepage_should_405(self):
        response = self.client.post('/')
        assert response.status_code == 405


class VacancyTestCase(TestCase):
    def test_create_vacancy_should_success(self):
        my_data = {
            'title': 'Test 1',
            'salary': '100',
            'description': 'test description',
            'email': 'test@mail.com',
            'is_relevant': True,
            'contacts': 'test contacts'
        }
        response = self.client.post('/add-vacancy/', data=my_data)
        self.assertEqual(response.status_code, 302)

        new_vacancy = Vacancy.objects.first()
        self.assertEqual(new_vacancy.title, my_data['title'])
        self.assertEqual(new_vacancy.salary, int(my_data['salary']))
        self.assertEqual(new_vacancy.description, my_data['description'])
        self.assertEqual(new_vacancy.email, my_data['email'])
        self.assertEqual(new_vacancy.is_relevant, my_data['is_relevant'])
        self.assertTrue(new_vacancy.contacts, my_data['contacts'])

        vacancy_title = my_data["title"]
        response_homepage = self.client.get("/")
        self.assertContains(response_homepage, vacancy_title)



