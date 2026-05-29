from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from .models import Format, ConvertFormat


class ConvertFormatViewSetTest(TestCase):

    def setUp(self):
        self.format_input = Format.objects.create(
            extension="pdf", category="document", is_active=True
        )
        self.format_output = Format.objects.create(
            extension="docx", category="document", is_active=True
        )
        self.convertformat = ConvertFormat.objects.create(
            original_extension=self.format_input,
            output_extension=self.format_output,
            is_active=True,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse("format-detail", kwargs={"id": self.format_input.id})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_and_retrieve_convertformat(self):
        # ORM retrieval: comprobar que el ConvertFormat creado en setUp existe
        cf = ConvertFormat.objects.get(
            original_extension=self.format_input, output_extension=self.format_output
        )
        self.assertIsNotNone(cf)
        self.assertEqual(cf.original_extension, self.format_input)
        self.assertEqual(cf.output_extension, self.format_output)
