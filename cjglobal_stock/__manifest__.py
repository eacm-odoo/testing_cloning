{
    'name': 'CJ Global: Available to sell field',
    'summary': '''
        Adds 'Available to Sell' field to Inventory Report List
    ''',
    'description': '''
        MPV - TASK ID: 2470112
        Adds a new field to Inventory Report List called 'Available to sell'
        that shows the difference between on hand quantity and the reserved
        quantity
    ''',
    'license': 'OPL-1',
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Development Services/Custom Development',
    'version': '1.1.0',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_quant_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
