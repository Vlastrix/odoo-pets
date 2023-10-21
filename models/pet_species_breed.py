# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PetSpeciesBreed(models.Model):
    _name = 'pet.species.breed'
    _description = 'Pet Species Breed'

    name = fields.Char(string="Name", required=True)
    species_id = fields.Many2one(string="Species", comodel_name="pet.species", required=True)
