# -*- coding: utf-8 -*-

from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class Pet(models.Model):
    _name = 'pet.pet'
    _description = 'Pet'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _compute_age(self):
        for record in self:
            relativedelta_age = relativedelta(datetime.now(), record.birth_date)
            years_age = relativedelta_age.years
            months_age = relativedelta_age.months
            days_age = relativedelta_age.days
            record.age = years_age + months_age / 12 + days_age / 365

    profile_pic = fields.Image(string="Profile Pic")
    name = fields.Char(string="Name", required=True)
    species_id = fields.Many2one(string="Species", comodel_name="pet.species", required=True)
    breed_id = fields.Many2one(string="Breed", comodel_name="pet.species.breed")
    birth_date = fields.Date(string="Birth Date", tracking=True)
    age = fields.Float(string="Age", compute='_compute_age')
    work_location_id = fields.Many2one(string="Work Location", comodel_name="hr.work.location", tracking=True)
