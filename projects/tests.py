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

	def test_show_all_clears_filters_and_keeps_pagination(self):
		for index in range(6):
			Project.objects.create(
				title=f"Project {index}",
				slug=f"project-{index}",
				category=self.tools,
				description="Project description.",
			)

		response = self.client.get(
			reverse("project_form"),
			{"q": "missing", "project_category": "tools"},
		)

		self.assertContains(response, f'href="{reverse("project_form")}">Show All</a>')
		all_projects_response = self.client.get(reverse("project_form"))
		self.assertEqual(all_projects_response.context["projects"].paginator.count, 6)
		self.assertEqual(all_projects_response.context["projects"].paginator.num_pages, 2)

	def test_project_live_demo_url_is_clickable(self):
		project = Project.objects.create(
			title="Hosted project",
			slug="hosted-project",
			category=self.web,
			description="A project with a live demo.",
			live_demo_url="https://example.com/demo",
		)

		response = self.client.get(reverse("project_form"))

		self.assertContains(
			response,
			f'<a class="projects-live-url" href="{project.live_demo_url}" target="_blank" rel="noopener noreferrer">',
		)

	def test_project_title_links_to_slug_detail_page(self):
		project = Project.objects.create(
			title="Slug linked project",
			slug="slug-linked-project",
			category=self.tools,
			description="Project introduction.",
		)

		response = self.client.get(reverse("project_form"))

		self.assertContains(
			response,
			f'href="{reverse("project_detail", kwargs={"slug": project.slug})}"',
		)


class ProjectDetailViewTests(TestCase):
	def setUp(self):
		self.category = Category.objects.create(name="Tools", slug="tools")
		self.project = Project.objects.create(
			title="Detailed project",
			slug="detailed-project",
			category=self.category,
			description="A short introduction.",
			detail_content="Full project explanation.",
		)

	def test_detail_page_renders_requested_project(self):
		response = self.client.get(
			reverse("project_detail", kwargs={"slug": self.project.slug})
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["project"], self.project)
		self.assertContains(response, "A short introduction.")
		self.assertContains(response, "Full project explanation.")
		self.assertContains(response, "Tools")

	def test_missing_project_links_are_not_rendered(self):
		response = self.client.get(
			reverse("project_detail", kwargs={"slug": self.project.slug})
		)

		self.assertNotContains(response, "GitHub</a>")
		self.assertNotContains(response, "Live Demo</a>")

	def test_unknown_slug_returns_404(self):
		response = self.client.get(
			reverse("project_detail", kwargs={"slug": "unknown-project"})
		)

		self.assertEqual(response.status_code, 404)
