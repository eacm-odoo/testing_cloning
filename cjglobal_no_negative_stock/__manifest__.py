{
    'name': "cjglobal_no_negative_stock",

    'summary': """
        this module prevents stock transfers with negative quantities""",

    'description': """
        This module extends stock.quant to raise an error when stock move let negative quantities
    """,

    'author': "Odoo PS",
    'website': "https://www.odoo.com",
    'category': 'Customizations/Product',
    'version': '1.1.0',
    'license': 'OPL-1',
    'depends': ['sale_stock'],
}
