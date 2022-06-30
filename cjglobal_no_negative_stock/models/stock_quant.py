# -*- coding:utf-8 -*-

from odoo import _, api, models
from odoo.exceptions import ValidationError
from odoo.tools import config, float_compare


class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.constrains("product_id", "quantity")
    def check_negative_qty(self):
        p = self.env["decimal.precision"].precision_get("Product Unit of Measure")

        for quant in self:
            if (
                float_compare(quant.quantity, 0, precision_digits=p) == -1
                and quant.product_id.type == "product"
                and quant.location_id.usage in ["internal", "transit"]
            ):
                raise ValidationError(
                    _(
                        "There is not enough inventory to complete this transaction. Please check the following :"
                        "product: '%s' lot/serial number location: %s "
                        "(%s available at location %s)"
                    )
                    % (
                        quant.product_id.display_name,
                        quant.lot_id.name or quant.location_id.complete_name,
                        quant.quantity,
                        quant.location_id.complete_name,
                    )
                )

