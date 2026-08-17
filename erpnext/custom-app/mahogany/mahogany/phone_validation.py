import frappe
from frappe.model.base_document import BaseDocument
from frappe.utils import (
    split_emails,
    validate_email_address,
    validate_iban,
    validate_name,
    validate_url,
)

_original_validate_data_fields = BaseDocument._validate_data_fields


def validate_data_fields(self):
    if self.doctype != "Channel Partner PIC":
        return _original_validate_data_fields(self)

    # Untuk Channel Partner PIC:
    # tetap pertahankan Phone field + country picker,
    # tetapi jangan validasi panjang/format nomor.
    for data_field in self.meta.get_data_fields():
        data = self.get(data_field.fieldname)

        if not data:
            continue

        options = data_field.get("options")
        old_fieldtype = data_field.get("oldfieldtype")

        if old_fieldtype and old_fieldtype != "Data":
            continue

        if options == "Email":
            if self.owner in frappe.STANDARD_USERS and data in frappe.STANDARD_USERS:
                continue
            for email in split_emails(data):
                validate_email_address(email, throw=True)

        elif options == "Name":
            validate_name(data, throw=True)

        elif options == "URL":
            validate_url(data, throw=True)

        elif options == "IBAN":
            validate_iban(data, throw=True)


BaseDocument._validate_data_fields = validate_data_fields
