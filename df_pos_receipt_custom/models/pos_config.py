from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    receipt_template_id = fields.Many2one(
        'pos.receipt.template',
        string='Receipt Template',
        help='Select a custom receipt template for this POS.',
    )
    receipt_email_template_id = fields.Many2one(
        'mail.template',
        string='Receipt Email Template',
        domain="[('model', '=', 'pos.order')]",
        help='Select a custom email template for sending receipts. '
             'Leave empty to use the default.',
    )

    @api.model
    def _load_pos_data_read(self, records, config):
        result = super()._load_pos_data_read(records, config)
        if config.receipt_template_id:
            tpl = config.receipt_template_id
            result[0]['_receipt_template'] = {
                'id': tpl.id,
                'name': tpl.name,
                'header_text': tpl.header_text or '',
                'footer_text': tpl.footer_text or '',
                'show_config_name': tpl.show_config_name,
                'show_cashier': tpl.show_cashier,
                'show_company_address': tpl.show_company_address,
                'show_company_vat': tpl.show_company_vat,
                'show_company_contact': tpl.show_company_contact,
                'show_tax_details': tpl.show_tax_details,
                'show_qr_code': tpl.show_qr_code,
            }
        else:
            result[0]['_receipt_template'] = None
        return result
