import odoo.tests
import logging

_logger = logging.getLogger(__name__)


class TestStockQuantPackages(odoo.tests.common.TransactionCase):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()

        cls.package = cls.env['stock.quant.package'].create({
            'length': 15,
            'width': 12,
            'height': 10,
        })

    def test_package_volume(self):
        _logger.warning('Test package volume')
        # 12 * 12 * 12 = 1728
        self.assertEqual(self.package.volume, 1800 / 1728, 'length * width * height is different to the volume.')
