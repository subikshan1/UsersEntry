from django.test import TestCase
from .models import Users


class TestModels(TestCase):
    def setUp(self):
        Users.objects.create(
            City="Covai",
            DOB="2000-02-03",
            FirstName="TestCase", LastName="T",
            Gender="Male", National="India", State="Assam", Pin="641004",
            Qualification="B.TECH", PanNum="BR400", Salary="40000")
        Users.objects.create(
            City="Covai",
            DOB="2000-02-03",
            FirstName="TestCase", LastName="T",
            Gender="Male", National="India", State="Assam", Pin="641004",
            Qualification="B.TECH", PanNum="BR400", Salary="40000")

    def test_model(self):
        self.assertEqual(len(Users.objects.all()), 2)

    def test_form_request(self):
        form = Users(
            data={
                'FirstName': "TestCase",
                'LastName': "T",
                'DOB': "2000-02-03",
                'Gender': "Male",
                'National': "India",
                'City': "Covai",
                'Pin': "641004",
                'State': "Assam",
                'Qualification': "B.TECH",
                'Salary': "40000",
                'PanNum': "TEST50PAN",
            }
        )
        self.assertTrue(form.isvalid())
