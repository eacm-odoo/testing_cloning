{
    'name': "CJ Global: add pallet information to the delivery transfer",
    'summary':
        """
        Module to add pallet information to the delivery transfer. 
        """,
    'description':
        """
        Module to add pallet information to the delivery transfer, 
        NEW REALLY IMPORTANT CHANGE!!!
        On the package reference (stock.quant.package):
        - Pallet Height
        - Pallet Width
        - Pallet Length
        - Cubic feet
        On the delivery transfer (stock.picking):
        - Pallet count: total packages packed 
        - Carton count: total of 'done' quantities in that delivery.
        - Max Height: the highest number entered under Pallet Height of the packages in the line
        - Total Cuf: total cubic feet calculated by adding the cubic feet per pallet (package)
        Developer: ralb
        Task ID: 3478728
        Link to task: https://www.odoo.com/web#id=3478728&cids=17&model=project.task&view_type=form
        """,
    'author': "Odoo Inc.",
    'license': 'OPL-1',
    'website': "https://www.odoo.com",
    'category': 'Custom Modules',
    'version': '1.0.0',
    'depends': ['stock', 'delivery'],
    'data': [
        'views/stock_picking_views_cjglobal.xml',
        'views/stock_quant_views_cjglobal.xml',
    ]
}
