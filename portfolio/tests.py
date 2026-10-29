from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PortfolioAccessTests(TestCase):
    def test_public_pages_are_available_without_login(self):
        page_names = (
            "portfolio_home",
            "about",
            "education",
            "certifications",
            "experience",
            "services",
            "cv",
        )
        for name in page_names:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_navigation_reflects_real_authentication_state(self):
        home = self.client.get(reverse("home"))
        self.assertContains(home, reverse("login"))
        self.assertContains(home, reverse("signup"))
        dashboard_href = f'href="{reverse("dashboard")}"'
        self.assertNotContains(home, dashboard_href)

        user = get_user_model().objects.create_user(
            username="portfolio_member",
            password="Portfolio-Member-Password-482!",
        )
        self.client.force_login(user)
        authenticated_home = self.client.get(reverse("home"))
        self.assertContains(authenticated_home, reverse("dashboard"))
        self.assertContains(authenticated_home, reverse("logout"))
        self.assertNotContains(authenticated_home, reverse("signup"))

    def test_global_home_lists_only_registered_application_landing_pages(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("portfolio_home"))
        self.assertContains(response, reverse("project_form"))
        self.assertContains(response, reverse("db_home"))
        self.assertNotContains(response, reverse("education"))
        self.assertNotContains(response, reverse("cv"))

    def test_portfolio_navigation_owns_its_internal_pages(self):
        response = self.client.get(reverse("portfolio_home"))
        navigation = response.content.decode().split('<nav class="site-nav"', 1)[1].split("</nav>", 1)[0]

        for name in ("about", "education", "experience", "certifications", "services", "cv"):
            with self.subTest(page=name):
                self.assertIn(reverse(name), navigation)

        self.assertNotIn(reverse("project_form"), navigation)
        self.assertNotIn(reverse("db_home"), navigation)

    def test_legacy_portfolio_path_redirects_to_portfolio_application(self):
        response = self.client.get("/about/")

        self.assertRedirects(response, reverse("about"))
