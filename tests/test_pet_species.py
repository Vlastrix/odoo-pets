# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('-standard', 'test_species')
class PetSpeciesTesting(TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()

    def test_pet_species_creation(self):
        bird = self.env["pet.species"].create({"name": "Bird"})
        self.assertEqual(bird.name, second="Bird", msg="Name does not exist!!")
        self.assertEqual(bird._name, second="pet.species", msg="Name does not exist!!")
