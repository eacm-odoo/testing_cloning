from odoo import fields, models, api
from odoo.tools.float_utils import float_round


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    case_pack = fields.Integer(string='Case Pack', related='product_id.product_tmpl_id.case_pack')
    unit_qty_cj = fields.Float(string='Unit Quantity')
    unit_price_cj = fields.Float(string="Unit Price")
    product_qty = fields.Float(string='Box Quantity', digits='Product Unit of Measure', compute="_compute_product_qty", store=True)
    price_unit = fields.Float(string='Box Price', digits='Product Price', compute='_compute_price_unit')

    @api.depends('unit_qty_cj', 'case_pack')
    def _compute_product_qty(self):
        for line in self:
            line.product_qty = float_round(line.unit_qty_cj / line.case_pack, precision_rounding=1, rounding_method='UP') if line.case_pack > 0 else line.unit_qty_cj
    
    @api.depends('unit_price_cj', 'case_pack')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.unit_price_cj * line.case_pack
    
    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, company_id, values, po):
        """override _prepare_purchase_order_line_from_procurement and add unit_qty and unit_price_cj to the values"""
        values = super()._prepare_purchase_order_line_from_procurement(product_id, product_qty, product_uom, company_id, values, po)
        values.update({
            'unit_qty_cj': product_qty * product_id.case_pack,
            'unit_price_cj': values['price_unit'],
        })
        return values
