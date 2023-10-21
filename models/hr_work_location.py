# -*- coding: utf-8 -*-

from odoo import models, fields


class HrWorkLocation(models.Model):
    _inherit = 'hr.work.location'

    pets_ids = fields.One2many(string="Pets", comodel_name="pet.pet", inverse_name="work_location_id")

