# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pet(models.Model):
    _name = 'pet.pet'
    _description = 'Pet'

    def _compute_age(self):
        for pet in self:
            pet_age = pet.birth_date
            pet.age = 0

    profile_pic = fields.Image(string="Profile Pic")
    name = fields.Char(string="Name", required=True)
    species_id = fields.Many2one(string="Species", comodel_name="pet.species", required=True)
    breed_id = fields.Many2one(string="Breed", comodel_name="pet.species.breed")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Float(string="Age", compute='_compute_age')




