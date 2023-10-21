# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime, date

class Pet(models.Model):
    _name = 'pet.pet'
    _description = 'Pet'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _compute_age(self):
        for pet in self:
            if pet.birth_date:
                birth_date_str = str(pet.birth_date)
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
                current_date = fields.Date.today()
                age_in_days = (current_date - birth_date).days
                age_in_years = age_in_days / 365
                pet.age = age_in_years
            else:
                pet.age = 0.0

    profile_pic = fields.Image(string="Profile Pic")
    name = fields.Char(string="Name", required=True)
    species_id = fields.Many2one(string="Species", comodel_name="pet.species", required=True)
    breed_id = fields.Many2one(string="Breed", comodel_name="pet.species.breed")
    birth_date = fields.Date(string="Birth Date", tracking=True)
    age = fields.Float(string="Age", compute='_compute_age')
    work_location_id = fields.Many2one(string="Work Location", comodel_name="hr.work.location", tracking=True)
