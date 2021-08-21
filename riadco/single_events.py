# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def allow_negative():
    negative_stock = frappe.db.sql(""" update `tabSingles` set value = '0' where doctype = 'Stock Settings' and field = 'allow_negative_stock' """)
    over_delivery = frappe.db.sql(""" update `tabSingles` set value = '10' where doctype = 'Stock Settings' and field = 'over_delivery_receipt_allowance' """)
    over_bill = frappe.db.sql(""" update `tabSingles` set value = '10' where doctype = 'Accounts Settings' and field = 'over_billing_allowance' """)
    return negative_stock , over_bill, over_delivery

