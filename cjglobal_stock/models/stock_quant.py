# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    available_to_sell = fields.Float(string='Available to Sell',
        compute='_compute_available_to_sell')

    def _compute_available_to_sell(self):
        for record in self:
            record.available_to_sell = record.inventory_quantity - record.reserved_quantity
        
    ''' 
        Override read_group to add available_to_sell field, similar to how is 
        done for inventory_quantity in stock_quant.py 
    '''
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        result = super(StockQuant, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        if self._is_inventory_mode():
            for record in result:
                record['available_to_sell'] = record.get('inventory_quantity', 0) - record.get('reserved_quantity', 0)
        return result