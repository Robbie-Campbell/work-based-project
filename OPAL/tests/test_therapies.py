from django.test import TestCase
from django.urls import reverse

from .create_objects import create_user, create_patient, create_team, create_therapist
from ..models import Therapy


class TestTherapies(TestCase):

    def setUp(self):
        self.client = create_user()
        self.patient = create_patient(1)
        team = create_team(1)
        self.therapist = create_therapist(1, team)
        self.therapy = self.create_therapy()

    def test_therapy_list_patient(self):
        self.client.post(reverse('OPAL:patient_create'), data=self.patient.__dict__)
        response = self.client.get(reverse('OPAL:therapy_list_patient', args=[self.patient.id]))
        self.assertEqual(response.status_code, 200)

    def test_therapy_list_therapist(self):
        self.client.post(reverse('OPAL:therapist_create'), data=self.therapist.__dict__)
        response = self.client.get(reverse('OPAL:therapy_list_therapist', args=[self.therapist.id]))
        self.assertEqual(response.status_code, 200)

    def test_therapy_create_get(self):
        response = self.client.get(reverse('OPAL:therapy_create', args=[self.patient.id]))
        self.assertEqual(response.status_code, 200)

    def test_therapy_create_post(self):
        response = self.client.post(reverse('OPAL:therapy_create', args=[self.therapy.patient.id]), data=self.therapy.__dict__)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Therapy.objects.first().id, 1)

    def test_therapy_edit_get(self):
        self.client.post(reverse('OPAL:therapy_create', args=[self.therapy.patient.id]), data=self.therapy.__dict__)
        response = self.client.get(reverse('OPAL:therapy_edit', args=[self.therapy.id]))
        self.assertEqual(response.status_code, 200)

    def test_therapy_edit_post(self):
        self.client.post(reverse('OPAL:therapy_create', args=[self.therapy.patient.id]), data=self.therapy.__dict__)
        response = self.client.post(reverse('OPAL:therapy_edit', args=[self.therapy.id]), data=self.therapy.__dict__)
        self.assertEqual(response.status_code, 200)

    def test_therapy_delete(self):
        self.client.post(reverse('OPAL:therapy_create', args=[self.therapy.patient.id]), data=self.therapy.__dict__)
        response = self.client.post(reverse('OPAL:therapy_delete', args=[self.therapy.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Therapy.objects.count(), 0)
