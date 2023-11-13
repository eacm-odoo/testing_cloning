from odoo import fields, models


class Picking(models.Model):
    _inherit = 'stock.picking'

    pallet_count = fields.Integer(compute='_compute_pallet_count')
    carton_count = fields.Integer(compute='_compute_carton_count')
    max_height = fields.Float(compute='_compute_max_height')
    total_cuf = fields.Float(compute='_compute_total_cuf')

    max_height_uom_name = fields.Char(compute='_compute_max_height_uom_name')
    volume_uom_name = fields.Char(string="", compute='_compute_volume_uom_name')

    def _compute_pallet_count(self):
        self.pallet_count = 0
        for picking in self:
            picking.pallet_count = len(picking.package_ids)

    def _compute_carton_count(self):
        carton_counts = {picking.id: sum(picking.move_line_ids.mapped("qty_done")) if picking.move_line_ids else 0 for picking in self}
        for picking in self:
            picking.carton_count = carton_counts[picking.id]

    def _compute_max_height(self):
        max_heights = {picking.id: max(picking.package_ids.mapped("height")) if picking.package_ids else 0 for picking in self}
        for picking in self:
            picking.max_height = max_heights[picking.id]

    def _compute_total_cuf(self):
        total_cufs = {picking.id: sum(picking.package_ids.mapped('volume')) if picking.package_ids else 0 for picking in self}
        for picking in self:
            picking.total_cuf = total_cufs[picking.id]

    def _compute_max_height_uom_name(self):
        length_uom_name = self.env.ref('uom.product_uom_inch').name
        for picking in self:
            picking.max_height_uom_name = length_uom_name

    def _compute_volume_uom_name(self):
        volume_uom_name = self.env.ref('uom.product_uom_cubic_foot').name
        for picking in self:
            picking.volume_uom_name = volume_uom_name
