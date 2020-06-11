from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json


class TestViews(TestCase):


    def setUp(self):
        # creating instance of a client.
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project1'])
        self.project1 = Project.objects.create(
            name = 'project1',
            budget = 1000
        )


    def test_project_list_GET(self):

        #test code
        response = self.client.get(self.list_url)

        #assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_GET(self):

        #test code
        response = self.client.get(self.detail_url)

        #assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')
