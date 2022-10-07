# -*- coding: utf-8 -*-

from odoo import fields, models, api

import math


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    case_pack = fields.Integer(string='Case Pack', related='product_id.product_tmpl_id.case_pack')
    unit_qty = fields.Float(string='Unit Quantity')
    unit_price = fields.Float(string="Unit Price")
    product_qty = fields.Float(string='Box Quantity', digits='Product Unit of Measure', required=True, compute="_compute_product_qty")
    price_unit = fields.Float(string='Box Price', required=True, digits='Product Price', compute='_compute_price_unit')

    @api.depends('unit_qty', 'case_pack')
    def _compute_product_qty(self):
        for line in self:
            line.product_qty = math.ceil(line.unit_qty / line.case_pack) if line.case_pack > 0 else line.unit_qty
    
    @api.depends('price_unit', 'case_pack')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.unit_price * line.case_pack
    
