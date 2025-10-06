{
    'name': 'Pharmacy Management System',
    'version': '17.0.1.0.0',
    'category': 'Healthcare',
    # 'sequence': -200,
    'summary': 'Manage medicines, sales, purchases, customers, and prescriptions',
    'author': 'Nasratullah Shafiq',
    'depends': ['base', 'mail'],  # <-- Add 'mail' here
    'data': [
        'security/ir.model.access.csv',

        'views/medicine_views.xml',
        'views/supplier_views.xml',
        'views/purchase_views.xml',
        'views/sale_views.xml',
        'views/customer_views.xml',
        'views/prescription_views.xml',
        'views/menu.xml',
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
