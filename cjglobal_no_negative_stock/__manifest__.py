
# -*- coding: utf-8 -*-
{
    'name': "cjglobal_no_negative_stock",

    'summary': """
        this module prevents stock transfers with negative quantities""",

    'description': """
        This module extends stock.quant to raise an error when stock move let negative quantities
    """,

    'author': "Odoo Inc",
    'website': "https://www.odoo.com",
    # task number 2871191
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations/Product',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['sale_stock'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
