from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_receipt_template_id = fields.Many2one(
        related='pos_config_id.receipt_template_id',
        readonly=False,
    )
    pos_receipt_email_template_id = fields.Many2one(
        related='pos_config_id.receipt_email_template_id',
        readonly=False,
    )
