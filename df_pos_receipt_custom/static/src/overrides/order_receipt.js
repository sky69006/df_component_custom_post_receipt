/** @odoo-module */

import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";
import { patch } from "@web/core/utils/patch";

patch(OrderReceipt.prototype, {
    get receiptTemplate() {
        return this.order.config._receipt_template || null;
    },

    get showConfigName() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_config_name : true;
    },

    get showCashier() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_cashier : true;
    },

    get showCompanyAddress() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_company_address : true;
    },

    get showCompanyVat() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_company_vat : true;
    },

    get showCompanyContact() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_company_contact : true;
    },

    get showTaxDetails() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_tax_details : true;
    },

    get showQrCode() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.show_qr_code : true;
    },

    get customHeaderText() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.header_text : '';
    },

    get customFooterText() {
        const tpl = this.receiptTemplate;
        return tpl ? tpl.footer_text : '';
    },
});

function _getReceiptTemplate(order) {
    return order.config._receipt_template || null;
}

patch(ReceiptHeader.prototype, {
    get showCashier() {
        const tpl = _getReceiptTemplate(this.props.order);
        return tpl ? tpl.show_cashier : true;
    },
});
