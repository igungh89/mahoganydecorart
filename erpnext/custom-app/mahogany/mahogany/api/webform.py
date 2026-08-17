import frappe


@frappe.whitelist()
def cancel_booking(lead):
    if not lead:
        frappe.throw("Lead tidak ditemukan")

    doc = frappe.get_doc("Mahogany Lead", lead)

    doc.db_set("booking_status", "Canceled")
    doc.db_set("sales_status", "Lost")

    frappe.db.commit()

    return {"success": True}


@frappe.whitelist()
def get_lead_success(lead):
    if not lead:
        frappe.throw("Lead tidak ditemukan")

    doc = frappe.get_doc("Mahogany Lead", lead)

    # Ambil URL Web Form yang sudah dibuat untuk Lead ini.
    # URL ini harus berupa /edit, bukan /new.
    web_form_url = doc.web_form_url

    if not web_form_url and doc.sales_status not in ("Meeting", "Lost"):
        frappe.throw("Web Form URL belum tersedia untuk Lead ini")

    return {
        "name": doc.name,
        "client_name": doc.client_name,
        "phone": doc.phone,
        "instagram": doc.instagram,
        "address": doc.address,

        "service": doc.service,
        "service_package": doc.service_package,
        "price": doc.price,
        "event_date": doc.event_date,

        "venue": doc.venue,
        "venue_address": doc.venue_address,

        "booking_status": doc.booking_status,
        "sales_status": doc.sales_status,

        "channel_order": doc.channel_order,
        "channel_partner": doc.channel_partner,
        "channel_partner_pic": doc.channel_partner_pic,
        "phone_pic": doc.phone_pic,

        "web_form_url": web_form_url
    }



@frappe.whitelist()
def get_services():
    return frappe.get_all(
        "Service",
        filters={"status": "Active"},
        fields=["name", "service_name"],
        order_by="name asc"
    )


@frappe.whitelist()
def get_venues():
    return frappe.get_all(
        "Venue",
        filters={"status": "Active"},
        fields=["name", "venue_name", "address"],
        order_by="venue_name asc"
    )


@frappe.whitelist()
def get_packages(service=None):
    filters = {"status": "Active"}

    if service:
        filters["service"] = service

    return frappe.get_all(
        "Service Package",
        filters=filters,
        fields=["name", "package_name", "display_name", "price", "service"],
        order_by="sort_order asc, name asc"
    )


@frappe.whitelist()
def get_last_lead(phone=None):
    if not phone:
        return None

    return frappe.db.get_value(
        "Mahogany Lead",
        {"phone": phone},
        "name",
        order_by="modified desc"
    )



@frappe.whitelist()
def get_channel_partners():
    return frappe.get_all(
        "Channel Partner",
        filters={"status": "Active"},
        fields=[
            "name",
            "partner_name",
            "channel_type",
            "address"
        ],
        order_by="partner_name asc",
        limit_page_length=100
    )
