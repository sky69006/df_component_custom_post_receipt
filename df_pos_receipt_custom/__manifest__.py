{
    'name': 'POS Receipt Customization',
    'version': '19.0.1.0.0',
    'summary': 'Customizable POS receipts with multi-language templates and editable email templates',
    'description': """
        Allows creating and managing custom POS receipt templates with:
        - Multi-language support for header and footer text
        - Toggle visibility of receipt sections (config name, cashier, tax details, etc.)
        - Custom email templates for receipt emails
        - Fix for duplicate receipt attachment in emails
        - Accessible from POS settings
    """,
    'category': 'Sales/Point of Sale',
    'author': 'Surekha Technologies Pvt. Ltd.',
    'website': 'https://www.surekhatech.com',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'views/pos_receipt_template_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'df_pos_receipt_custom/static/src/overrides/order_receipt.js',
            'df_pos_receipt_custom/static/src/overrides/order_receipt.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
