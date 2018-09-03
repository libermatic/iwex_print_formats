# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__

app_name = "iwex_print_formats"
app_version = __version__
app_title = "iWEX Print Formats"
app_publisher = "Libermatic"
app_description = "Print Formats for iWEX"
app_icon = "fa fa-print"
app_color = "#0000FF"
app_email = "info@libermatic.com"
app_license = "MIT"

error_report_email = 'support@libermatic.com'

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iwex_print_formats/css/iwex_print_formats.css"
# app_include_js = "/assets/iwex_print_formats/js/iwex_print_formats.js"

# include js, css files in header of web template
# web_include_css = "/assets/iwex_print_formats/css/iwex_print_formats.css"
# web_include_js = "/assets/iwex_print_formats/js/iwex_print_formats.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#    "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "iwex_print_formats.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "iwex_print_formats.install.before_install"
# after_install = "iwex_print_formats.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = \
#   "iwex_print_formats.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"iwex_print_formats.tasks.all"
# 	],
# 	"daily": [
# 		"iwex_print_formats.tasks.daily"
# 	],
# 	"hourly": [
# 		"iwex_print_formats.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iwex_print_formats.tasks.weekly"
# 	]
# 	"monthly": [
# 		"iwex_print_formats.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "iwex_print_formats.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": \
# 	 "iwex_print_formats.event.get_events"
# }
