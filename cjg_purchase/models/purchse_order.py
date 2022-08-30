# -*- coding: utf-8 -*-

from odoo import fields, models, api

import math


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    case_pack = fields.Integer(string='Case Pack', compute='_compute_case_pack')
    box_qty = fields.Float(string='Box Count', compute='_compute_box_qty')
    price_box = fields.Float(string='Box Price', compute='_compute_box_price')

    @api.depends('product_id')
    def _compute_case_pack(self):
        for line in self:
            line.case_pack = line.product_id.product_tmpl_id.case_pack
    
    @api.depends('box_qty', 'case_pack')
    def _compute_box_qty(self):
        for line in self:
            line.box_qty = math.ceil(line.product_qty / line.case_pack) if line.case_pack > 0 else line.product_qty
    
    @api.depends('price_unit', 'case_pack')
    def _compute_box_price(self):
        for line in self:
            line.price_box = line.price_unit * line.case_pack
    
    def _prepare_stock_moves(self, picking):
        res = super()._prepare_stock_moves(picking)
        for val in res:
            val['product_uom_qty'] = self.box_qty
            val['price_unit'] = self.price_box
        return res
