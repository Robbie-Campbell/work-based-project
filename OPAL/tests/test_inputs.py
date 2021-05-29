from django.test import TestCase
from django.urls import reverse

from ..models import IndirectInput, DirectInput, Team, Therapist
from .create_objects import *


class TestInputs(TestCase):

    def test_direct_input_get(self):
        direct_input = DirectInput.objects.create(id=1, title="test")
        therapist = create_therapist(1, create_team(1))
        self.client = create_user()
        response = self.client.get(reverse("OPAL:direct_input_create", args=[therapist.id,]))

        self.assertEqual(response.status_code, 200)
        self.assertIn(direct_input.title, response.content)