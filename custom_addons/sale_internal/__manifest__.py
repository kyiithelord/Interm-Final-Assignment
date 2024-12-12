# __manifest__.py
{
    'name': 'Sale Internal',
    'version': '16.0.1.0.0',
    'category': 'Custom',
    'summary': 'Sale order line Discount amount and Portal',
    'description': """
        Detailed description of the module
    """,
    'author': 'Bhone Myint Thu, Pyae Sone Hein, Thura Htun, ',
    'depends': ['base', 'sale','website','account'],  # Add any module dependencies here
    'data': [
        'views/discount_amm.xml',
        'views/discount_amm_invoice.xml',
        'views/portal_sale_order_views.xml',
        'views/portal_invoice_views.xml'
    ],
    'installable': True,
    'application': True,
}
