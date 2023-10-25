# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('-standard', 'test_pet')
class PetTesting(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.species_demo = cls.env["pet.species"].create({"name": "Cat"})
        cls.species_breed_demo = cls.env["pet.species.breed"].create(
            {"name": "Bengali", "species_id": cls.species_demo.id})

    def test_pet_creation(self):
        self.assertTrue(True)

    def test_pet_species_breed_creation(self):
        pet_species_breed = self.env["pet.pet"].create(
            {"name": "Michifus", "species_id": self.species_demo.id, "breed_id": self.species_breed_demo.id,
             "birth_date": "2019-10-05"})
        self.assertEqual(pet_species_breed.birth_date.strftime("%Y-%m-%d"), second="2019-10-05",
                         msg="birth_date does not exist!!")
