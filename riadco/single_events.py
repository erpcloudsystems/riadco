# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def allow_negative():
    return frappe.sdb.sql(""" update `tabSingles` set value = 0 where doctype = 'Stock Settings' and field = 'allow_negative_stock' """)