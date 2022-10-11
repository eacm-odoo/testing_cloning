# -*- coding: utf-8 -*-

from odoo import fields, models, api

import math


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    case_pack = fields.Integer(string='Case Pack', related='product_id.product_tmpl_id.case_pack')
    unit_qty_cj = fields.Float(string='Unit Quantity')
    unit_price_cj = fields.Float(string="Unit Price")
    product_qty = fields.Float(string='Box Quantity', digits='Product Unit of Measure', compute="_compute_product_qty")
    price_unit = fields.Float(string='Box Price', required=True, digits='Product Price', compute='_compute_price_unit')

    @api.depends('unit_qty_cj', 'case_pack')
    def _compute_product_qty(self):
        for line in self:
            line.product_qty = math.ceil(line.unit_qty_cj / line.case_pack) if line.case_pack > 0 else line.unit_qty_cj
    
    @api.depends('unit_price_cj', 'case_pack')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.unit_price_cj * line.case_pack
    
