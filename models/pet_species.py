# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PetSpecies(models.Model):
    _name = 'pet.species'
    _description = 'Pet Species'

    name = fields.Char(string="Name", required=True)
    breed_ids = fields.One2many(string="Breeds", comodel_name="pet.species.breed", inverse_name="species_id")

