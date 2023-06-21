from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from resume.models import Resume
from resume.serializers import ResumeSerializer


class ResumeTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('resume')

        self.user_1: User = User.objects.create_user(username="test_user_1")
        self.user_1.set_password("password_1")
        self.user_1.save()

        self.user_2: User = User.objects.create_user(username="test_user_2")
        self.user_2.set_password("password_2")
        self.user_2.save()

    def tearDown(self):
        self.user_1.delete()
        self.user_2.delete()

    def test_api_access_anon(self):
        self.client.logout()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'].code, 'not_authenticated')

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'].code, 'not_authenticated')

    def test_api_get(self):
        self.client.force_login(self.user_1)

        response = self.client.get(self.url)
        orig_resume_data = ResumeSerializer(Resume.objects.get(owner=self.user_1.id)).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, orig_resume_data)

    def test_api_patch(self):
        self.client.force_login(self.user_1)
        new_resume = {
            "status": "active",
            "grade": "middle",
            "specialty": "backend",
            "salary": 123456,
            "education": None,
            "experience": "Yandex, SkyPro",
            "portfolio": "https://example-site.com/resume/1234",
            "title": "Backend Developer",
            "phone": "+71112223344",
            "email": "user_1@email.com"
        }

        old_response = self.client.get(self.url)
        old_resume_data = ResumeSerializer(Resume.objects.get(owner=self.user_1.id)).data

        self.assertEqual(old_response.status_code, 200)
        self.assertEqual(old_response.data, old_resume_data)

        self.client.patch(self.url, new_resume, format='json')

        new_response = self.client.get(self.url)
        new_resume_data = ResumeSerializer(Resume.objects.get(owner=self.user_1.id)).data

        self.assertEqual(new_response.status_code, 200)
        self.assertEqual(new_response.data, new_resume_data)
        self.assertEqual(new_response.data, new_resume)

        self.client.force_login(self.user_1)
        user_1_response = self.client.get(self.url)
        self.client.force_login(self.user_2)
        user_2_response = self.client.get(self.url)
        user_2_default_resume_data = ResumeSerializer(Resume(owner=self.user_2)).data
        self.assertNotEqual(user_1_response.data, user_2_response.data)
        self.assertEqual(user_2_response.data, user_2_default_resume_data)
