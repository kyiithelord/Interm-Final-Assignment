# __manifest__.py
{
    'name': 'Custom Module Name',
    'version': '16.0.1.0.0',
    'category': 'Custom',
    'summary': 'A short summary of your module',
    'description': """
        Detailed description of the module
    """,
    'author': 'Your Name or Company',
    'depends': ['base', 'sale'],  # Add any module dependencies here
    'data': [
        'views/custom_module_views.xml',
        'security/ir.model.access.csv',
        # Add other XML/CSV files for views, security, etc.
    ],
    'installable': True,
    'application': True,
}
