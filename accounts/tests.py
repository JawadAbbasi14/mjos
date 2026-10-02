from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


User = get_user_model()


class AuthenticationFlowTests(TestCase):
    def signup_data(self, **overrides):
        data = {
            "username": "mjos_member",
            "email": "member@example.com",
            "age": "24",
            "remember": "on",
            "bio": "Account test profile",
            "password1": "Secure-Flow-Passphrase-482!",
            "password2": "Secure-Flow-Passphrase-482!",
        }
        data.update(overrides)
        return data

    def test_signup_creates_user_and_authenticated_session(self):
        response = self.client.post(reverse("signup"), self.signup_data())

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(User.objects.filter(username="mjos_member").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_invalid_signup_does_not_create_or_authenticate_user(self):
        response = self.client.post(
            reverse("signup"),
            self.signup_data(password2="Not-the-same-password-491!"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="mjos_member").exists())
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertContains(response, "password")

    def test_signup_enforces_minimum_age_on_server(self):
        response = self.client.post(
            reverse("signup"),
            self.signup_data(age="17"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="mjos_member").exists())
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_login_validates_and_establishes_session(self):
        User.objects.create_user(
            username="existing_member",
            password="Existing-Member-Password-481!",
        )

        invalid = self.client.post(
            reverse("login"),
            {"username": "existing_member", "password": "wrong-password"},
        )
        self.assertEqual(invalid.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)

        response = self.client.post(
            reverse("login"),
            {
                "username": "existing_member",
                "password": "Existing-Member-Password-481!",
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_rejects_external_next_url(self):
        User.objects.create_user(
            username="existing_member",
            password="Existing-Member-Password-481!",
        )

        response = self.client.post(
            f"{reverse('login')}?next=https://example.invalid/",
            {
                "username": "existing_member",
                "password": "Existing-Member-Password-481!",
                "next": "https://example.invalid/",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))

    def test_dashboard_protected_and_logout_is_post_only(self):
        dashboard = reverse("dashboard")
        response = self.client.get(dashboard)
        self.assertRedirects(response, f"{reverse('login')}?next={dashboard}")

        user = User.objects.create_user(
            username="signed_in_member",
            password="Signed-In-Member-Password-492!",
        )
        self.client.force_login(user)
        self.assertEqual(self.client.get(dashboard).status_code, 200)
        self.assertEqual(self.client.get(reverse("logout")).status_code, 405)

        response = self.client.post(reverse("logout"))
        self.assertRedirects(response, reverse("home"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_logout_requires_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        user = User.objects.create_user(
            username="csrf_member",
            password="CSRF-Member-Password-493!",
        )
        csrf_client.force_login(user)
        csrf_client.get(reverse("dashboard"))

        rejected = csrf_client.post(reverse("logout"))
        self.assertEqual(rejected.status_code, 403)

        token = csrf_client.cookies["csrftoken"].value
        accepted = csrf_client.post(
            reverse("logout"),
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertRedirects(accepted, reverse("home"))
        self.assertNotIn("_auth_user_id", csrf_client.session)
