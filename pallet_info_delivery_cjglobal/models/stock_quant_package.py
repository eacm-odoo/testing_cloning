from odoo import api, fields, models


class QuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    length = fields.Float(string="Pallet Length")
    width = fields.Float(string="Pallet Width")
    height = fields.Float(string="Pallet Height")
    volume = fields.Float(string="Cubic feet", compute='_compute_volume')

    length_uom_name = fields.Char(string="", compute='_compute_length_uom_name')
    volume_uom_name = fields.Char(string="", compute='_compute_volume_uom_name')

    def _compute_volume(self):
        for package in self:
            package.volume = package.length * package.width * package.height / 1728

    def _compute_length_uom_name(self):
        length_uom_name = self.env.ref('uom.product_uom_inch').name
        for package in self:
            package.length_uom_name = length_uom_name

    @api.depends('length', 'width', 'height')
    def _compute_volume_uom_name(self):
        volume_uom_name = self.env.ref('uom.product_uom_cubic_foot').name
        for package in self:
            package.volume_uom_name = volume_uom_name
