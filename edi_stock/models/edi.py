# -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class EdiIntegration(models.Model):
    _inherit = 'edi.integration'

    type = fields.Selection(
        selection_add=[('send_stock_quant', 'Send Stock Quant')])

    def _get_content(self, records):
        if self.type != 'send_stock_quant':
            return super()._get_content(records)

        file = []
        for quant in records.sudo():
            file.append('%s;%s;%s' % (quant.location_id,
                                        quant.product_id.default_code,
                                        quant.available_to_sell))
        return '\n'.join(file)
