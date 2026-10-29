from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductCrudViewTests(TestCase):
	def setUp(self):
		self.product = Product.objects.create(
			name="Sample product",
			price=Decimal("4.50"),
			quantity=3,
			description="Current description",
		)

	def test_create_product_uses_existing_form_fields(self):
		response = self.client.post(
			reverse("create"),
			{
				"pname": "New product",
				"pprice": "12.75",
				"pquantity": "6",
				"pdescription": "New description",
			},
		)

		self.assertRedirects(response, reverse("db_home"))
		product = Product.objects.get(name="New product")
		self.assertEqual(product.price, Decimal("12.75"))
		self.assertEqual(product.quantity, 6)
		self.assertEqual(product.description, "New description")

	def test_update_product_preserves_record_id_and_updates_fields(self):
		response = self.client.post(
			reverse("update", kwargs={"product_id": self.product.id}),
			{
				"pname": "Updated product",
				"pprice": "8.25",
				"pquantity": "9",
				"pdescription": "Updated description",
			},
		)

		self.assertRedirects(response, reverse("db_home"))
		self.product.refresh_from_db()
		self.assertEqual(self.product.name, "Updated product")
		self.assertEqual(self.product.price, Decimal("8.25"))
		self.assertEqual(self.product.quantity, 9)
		self.assertEqual(self.product.description, "Updated description")

	def test_delete_product_returns_to_list(self):
		response = self.client.get(
			reverse("delete", kwargs={"product_id": self.product.id})
		)

		self.assertRedirects(response, reverse("db_home"))
		self.assertFalse(Product.objects.filter(id=self.product.id).exists())
