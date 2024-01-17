import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase
from .models import *
from .serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            user=User.objects.create(
                email="mail@dmail.com",
                fam="Петров",
                name="Николай",
                otc="Иванович",
                phone="89956785633"
            ),
            beauty_title="основное",
            title="перевал",
            other_titles="другое",
            connect="связано",
            coordinates=Coordinates.objects.create(
                latitude=344.56,
                longitude=76.8,
                height=234
            ),
            level=Level.objects.create(
                winter="1d",
                summer="2a",
                autumn="2d",
                spring="3a"
            ),
        )
        self.images_1 = Image.objects.create(
            data="photos/image-66",
            title="hjkff",
            pereval=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            user=User.objects.create(
                email="mai2l@dmail.com",
                fam="Петров2",
                name="Николай2",
                otc="Иванович2",
                phone="899567856332"
            ),
            beauty_title="основное2",
            title="перевал2",
            other_titles="другое2",
            connect="связано2",
            coordinates=Coordinates.objects.create(
                latitude=344.562,
                longitude=76.82,
                height=2342
            ),
            level=Level.objects.create(
                winter="1d",
                summer="2a",
                autumn="2d",
                spring="3a"
            ),
        )
        self.images_2 = Image.objects.create(
            data="photos/image-662",
            title="hjkff",
            pereval=self.pereval_2
        )

    def test_get_list(self):
        url = reverse('pereval-list')  # from shell
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))  # from shell
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_get_by_email(self):
        url = reverse('email-pereval', args=(self.pereval_1.user.email,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            user=User.objects.create(
                email="mail@dmail.com",
                fam="Петров",
                name="Николай",
                otc="Иванович",
                phone="89956785633"
            ),
            beauty_title="основное",
            title="перевал",
            other_titles="другое",
            connect="связано",
            coordinates=Coordinates.objects.create(
                latitude=344.56,
                longitude=76.8,
                height=234
            ),
            level=Level.objects.create(
                winter="1d",
                summer="2a",
                autumn="2d",
                spring="3a"
            ),
        )
        self.images_1 = Image.objects.create(
            data="photos/image-66",
            title="hjkff",
            pereval=self.pereval_1
        )

        self.pereval_2 = Pereval.objects.create(
            user=User.objects.create(
                email="mai2l@dmail.com",
                fam="Петров2",
                name="Николай2",
                otc="Иванович2",
                phone="899567856332"
            ),
            beauty_title="основное2",
            title="перевал2",
            other_titles="другое2",
            connect="связано2",
            coordinates=Coordinates.objects.create(
                latitude=344.562,
                longitude=76.82,
                height=2342
            ),
            level=Level.objects.create(
                winter="1d",
                summer="2a",
                autumn="2d",
                spring="3a"
            ),
        )
        self.images_2 = Image.objects.create(
            data="photos/image-662",
            title="hjkff",
            pereval=self.pereval_2
        )

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                "id": 1,
                "beauty_title": "основное",
                "title": "перевал",
                "other_titles": "другое",
                "connect": "связано",
                "add_time": str(self.pereval_1.add_time),
                "user": {
                    "email": "mail@dmail.com",
                    "fam": "Петров",
                    "name": "Николай",
                    "otc": "Иванович",
                    "phone": "89956785633"
                },
                "coordinates": {
                    "latitude": 344.56,
                    "longitude": 76.8,
                    "height": 234
                },
                "level": {
                    "winter": "1d",
                    "summer": "2a",
                    "autumn": "2d",
                    "spring": "3a"
                },
                "images": [
                    {
                        "data": "photos/image-66",
                        "title": "hjkff"
                    },
                ],
                "status": "New"
            },
            {
                "id": 2,
                "beauty_title": "основное2",
                "title": "перевал2",
                "other_titles": "другое2",
                "connect": "связано2",
                "add_time": str(self.pereval_2.add_time),
                "user": {
                    "email": "mai2l@dmail.com",
                    "fam": "Петров2",
                    "name": "Николай2",
                    "otc": "Иванович2",
                    "phone": "899567856332"
                },
                "coordinates": {
                    "latitude": 344.562,
                    "longitude": 76.82,
                    "height": 2342
                },
                "level": {
                    "winter": "1d",
                    "summer": "2a",
                    "autumn": "2d",
                    "spring": "3a"
                },
                "images": [
                    {
                        "data": "photos/image-662",
                        "title": "hjkff"
                    },
                ],
                "status": "New"
            }
        ]
        dString = json.loads(json.dumps(serializer_data))
        self.assertEqual(expected_data, dString)

# python manage.py test .
# python manage.py test mainapp.tests.PerevalApiTestCase.test_get_list
# coverage run --source='.' manage.py test .
# coverage report
# coverage html
