from odoo import api, models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    #override _update_purchase_order_line and add unit_qty and unit_price_cj to the values
    def _update_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, line):
        values = super()._update_purchase_order_line(product_id, product_qty, product_uom, company_id, values, line)
        values.update({
            'unit_qty_cj': line.unit_qty_cj + product_qty * product_id.case_pack,
            'unit_price_cj': values['price_unit'],
        })
        return values

    #override _prepare_purchase_order_line and add unit_qty and unit_price_cj to the values
    @api.model
    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, po):
        values = super()._prepare_purchase_order_line(product_id, product_qty, product_uom, company_id, values, po)
        values.update({
            'unit_qty_cj': product_qty * product_id.case_pack,
            'unit_price_cj': values['price_unit'],
        })
        return values
        