# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    case_pack = fields.Integer(related='product_id.case_pack')
    box_count = fields.Float(compute='_compute_box', string='Box Count', default=0, store=True)
    box_price = fields.Integer(compute='_compute_box', string='Box Price')
    package_count = fields.Integer(compute='_compute_package_count', string='Package Count', default=0, store=True)

    @api.depends('product_uom_qty', 'product_id.case_pack')
    def _compute_box(self):
        for record in self:
            if record.product_id.case_pack:
                record.box_count = record.product_uom_qty / record.product_id.case_pack
            record.box_price = record.price_unit * record.product_id.case_pack

    @api.depends('product_uom_qty', 'product_packaging.qty')
    def _compute_package_count(self):
        for record in self.filtered(lambda sol: sol.product_packaging.qty):
                record.package_count = record.product_uom_qty / record.product_packaging.qty

class Sale(models.Model):
    _inherit = 'sale.order'

    total_box_count = fields.Integer(compute='_compute_packaging_total', string='Total Box Count')
    total_package_count = fields.Integer(compute='_compute_packaging_total', string='Total Package Count')

    @api.depends('order_line', 'order_line.box_count', 'order_line.package_count')
    def _compute_packaging_total(self):
        for order in self:
            order.total_box_count = sum(order.order_line.mapped('box_count'))
            order.total_package_count = sum(order.order_line.mapped('package_count'))