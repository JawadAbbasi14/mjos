from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PortfolioAccessTests(TestCase):
    def test_public_pages_are_available_without_login(self):
        page_names = (
            "home",
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
