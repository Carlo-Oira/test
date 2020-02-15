# -*- coding: utf-8 -*-

from odoo import fields, models


class PartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    address1 = fields.Text(string='Address 1')
    level = fields.Char(string='Level')
    municipality = fields.Char(string='Municipality')