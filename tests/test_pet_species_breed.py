# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('-standard', 'test_species_breed')
class PetSpeciesBreedTesting(TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.species_demo = self.env["pet.species"].create({"name": "Cat"})

    def test_pet_species_breed_creation(self):
        pet_species_breed = self.env["pet.species.breed"].create(
            {"name": "Bengali", "species_id": self.species_demo.id})
        self.assertEqual(pet_species_breed.name, second="Bengali", msg="Name does not exist!!")
        self.assertEqual(pet_species_breed._name, second="pet.species.breed", msg="Name does not exist!!")
        self.assertIn(pet_species_breed.id, self.species_demo.breed_ids.ids, msg="Breed is not related to species")
