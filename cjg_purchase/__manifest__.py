{
    "name": "cjg_purchase",
    "summary": """CjGlobal : Computed fields in PO""",
    "description": """
        CjGlobal module:
        Computed fields in PO 

        Developer: ELCE
        Ticket ID: 2948278
    """,
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "category": "Custom Development",
    "version": "1.1.0",
    "depends": [
        'cjg_sale_stock', 'purchase'],
    "data": [
        'views/purchase_order_views.xml',
    ],
    "license": "OPL-1",
    'installable' : True, 
    'application' : False,
    'auto_install' : False,
}
