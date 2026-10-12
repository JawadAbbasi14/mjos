from django.test import TestCase
from django.urls import reverse

from .models import Category, Project


class ProjectListViewTests(TestCase):
	def setUp(self):
		self.tools = Category.objects.create(name="Tools", slug="tools")
		self.web = Category.objects.create(name="Web", slug="web")

	def test_search_and_category_filters_are_combined(self):
		matching_project = Project.objects.create(
			title="Terminal scanner",
			slug="terminal-scanner",
			category=self.tools,
			description="Scans repository output.",
		)
		Project.objects.create(
			title="Web console",
			slug="web-console",
			category=self.web,
			description="A terminal-inspired interface.",
		)

		response = self.client.get(
			reverse("project_form"),
			{"q": "terminal", "project_category": "tools"},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(list(response.context["projects"]), [matching_project])
		self.assertContains(response, 'value="terminal"')
		self.assertContains(response, 'value="tools" selected')
		self.assertEqual(list(response.context["categories"]), [self.tools, self.web])

	def test_pagination_keeps_search_and_category_filters(self):
		for index in range(6):
			Project.objects.create(
				title=f"Terminal project {index}",
				slug=f"terminal-project-{index}",
				category=self.tools,
				description="Searchable project.",
			)

		response = self.client.get(
			reverse("project_form"),
			{"page": 2, "q": "Terminal", "project_category": "tools"},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["projects"].number, 2)
		self.assertEqual(
			response.context["pagination_query"],
			"q=Terminal&project_category=tools",
		)
		self.assertContains(
			response,
			'?page=1&amp;q=Terminal&amp;project_category=tools',
		)
