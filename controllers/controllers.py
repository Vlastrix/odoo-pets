# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-pets(http.Controller):
#     @http.route('/odoo-pets/odoo-pets', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-pets/odoo-pets/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-pets.listing', {
#             'root': '/odoo-pets/odoo-pets',
#             'objects': http.request.env['odoo-pets.odoo-pets'].search([]),
#         })

#     @http.route('/odoo-pets/odoo-pets/objects/<model("odoo-pets.odoo-pets"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-pets.object', {
#             'object': obj
#         })
