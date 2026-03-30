from odoo import fields, models


class PosReceiptTemplate(models.Model):
    _name = 'pos.receipt.template'
    _description = 'POS Receipt Template'

    name = fields.Char(string='Template Name', required=True, translate=True)
    active = fields.Boolean(default=True)
    header_text = fields.Text(string='Header Text', translate=True,
                              help='Custom header text displayed on the receipt.')
    footer_text = fields.Text(string='Footer Text', translate=True,
                              help='Custom footer text displayed on the receipt.')
    show_config_name = fields.Boolean(string='Show POS Name', default=False,
                                      help='Show the POS configuration name on the receipt (e.g. "Wandl 1").')
    show_cashier = fields.Boolean(string='Show Cashier', default=True,
                                  help='Show the cashier name on the receipt.')
    show_company_address = fields.Boolean(string='Show Company Address', default=True)
    show_company_vat = fields.Boolean(string='Show VAT Number', default=True)
    show_company_contact = fields.Boolean(string='Show Contact Info', default=True,
                                          help='Show phone, email, and website on the receipt.')
    show_tax_details = fields.Boolean(string='Show Tax Details', default=True,
                                      help='Show tax breakdown on the receipt.')
    show_qr_code = fields.Boolean(string='Show QR Code', default=True,
                                  help='Show QR code for invoice portal access.')

