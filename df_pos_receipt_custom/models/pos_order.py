from odoo import _, models
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _get_mail_attachments(self, name, ticket, basic_ticket):
        """Skip the basic ticket attachment to prevent duplicate receipts in email."""
        return super()._get_mail_attachments(name, ticket, False)

    def action_send_receipt(self, email, ticket_image, basic_image):
        """Use custom email template if configured on the POS config."""
        self.ensure_one()
        custom_template = self.config_id.receipt_email_template_id
        if custom_template:
            self.email = email
            custom_template.send_mail(
                self.id,
                force_send=True,
                email_values={
                    'email_to': email,
                    'attachment_ids': self._get_mail_attachments(
                        self.name, ticket_image, basic_image
                    ),
                },
            )
        else:
            return super().action_send_receipt(email, ticket_image, basic_image)
