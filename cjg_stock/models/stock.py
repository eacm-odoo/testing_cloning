# -*- coding: utf-8 -*-

from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # move_lines = fields.One2many('stock.move', 'picking_id', string="Stock Moves", copy=True)

    @api.model
    def get_initial_demand(self):
        print('hi')
        for move in self:
            print(move)

class StockMove(models.Model):
    _inherit = 'stock.move'

    # product_uom_qty = fields.Float('Initial Demand',
    #     digits='Product Unit of Measure',
    #     default=0.0, required=True, states={'done': [('readonly', True)]},
    #     help="This is the quantity of products from an inventory "
    #          "point of view. For moves in the state 'done', this is the "
    #          "quantity of products that were actually moved. For other "
    #          "moves, this is the quantity of product that is planned to "
    #          "be moved. Lowering this quantity does not generate a "
    #          "backorder. Changing this quantity on assigned moves affects "
    #          "the product reservation, and should be done with care.",
    #     compute='_get_initial_demand')

    
    # def _get_initial_demand(self):
    #     print('hi')
    #     for line in self:
    #         line.product_uom_qty = line.box_count

    # @api.onchange('box_count')
    # def set_demand(self):
    #     print('onchange firing.....................')
    #     for line in self:
    #         line.product_uom_qty = line.box_count