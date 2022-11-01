{
    'name': "cjg_sale_stock",

    'summary': """
        Use Box Count field as demand on deliveries """,
    'description': """
        Use box count field as the initial demand so warehouse 
        can take that many boxes from inventory and deliver them.
        Take amount out of inventory.
    """,

    'author': "Odoo INC",
    'website': "https://www.odoo.com",
    'license': 'OEEL-1',
    'version': '0.1',
    'depends': ['sale_stock'],
}
