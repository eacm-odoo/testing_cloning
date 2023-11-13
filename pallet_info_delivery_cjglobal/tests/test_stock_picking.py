from odoo.fields import Command
import odoo.tests
import logging

_logger = logging.getLogger(__name__)


class TestStockPicking(odoo.tests.common.TransactionCase):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()

        cls.partner = cls.env['res.partner'].create({'name': 'test'})

        cls.product1 = cls.env['product.product'].create({
            'sale_ok': True,
            'name': "Test Product 1",
        })

        cls.product2 = cls.env['product.product'].create({
            'sale_ok': True,
            'name': "Test Product 2",
        })

        cls.product3 = cls.env['product.product'].create({
            'sale_ok': True,
            'name': "Test Product 3",
        })

        cls.product4 = cls.env['product.product'].create({
            'sale_ok': True,
            'name': "Test Product 4",
        })

        cls.product0 = cls.env['product.product'].create({
            'sale_ok': True,
            'name': "Test Product 0",
        })

        cls.sale_order = cls.env['sale.order'].create({
            'partner_id': cls.partner.id,
            'order_line': [
                Command.create({
                    'product_id': cls.product0.id,
                    'product_uom_qty': 1,
                    'price_unit': 5,
                }),
                Command.create({
                    'product_id': cls.product1.id,
                    'product_uom_qty': 1,
                    'price_unit': 1,
                }),
                Command.create({
                    'product_id': cls.product2.id,
                    'product_uom_qty': 1,
                    'price_unit': 2,
                }),
                Command.create({
                    'product_id': cls.product3.id,
                    'product_uom_qty': 1,
                    'price_unit': 3,
                }),
                Command.create({
                    'product_id': cls.product4.id,
                    'product_uom_qty': 1,
                    'price_unit': 4,
                })
            ],
        })

    def test_pallet_info(self):
        _logger.warning('Test pallet info')

        self.env['res.config.settings'].create({'group_stock_production_lot': True}).execute()
        self.sale_order.action_confirm()
        pickings = self.sale_order.picking_ids

        for i, lines in enumerate(pickings.move_line_ids):
            lines.state = 'done'
            lines.qty_done = 1.0
            if i % 2 == 0:
                pickings.action_put_in_pack()

        self.assertEqual(pickings.pallet_count, 3, 'The number of packages packed is incorrect.')
        self.assertEqual(pickings.carton_count, 5, 'The number of "done" quantities is incorrect.')

        measures = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        total_volume = 0
        for i, package in enumerate(pickings.package_ids):
            package.length = measures[0][i]
            package.width = measures[1][i]
            package.height = measures[2][i]
            total_volume += measures[0][i] * measures[1][i] * measures[2][i]

        self.assertEqual(pickings.max_height, 9, 'The highest height is incorrect.')
        self.assertEqual(pickings.total_cuf, total_volume, 'The total cubic feet is incorrect.')
