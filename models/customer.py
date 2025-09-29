from odoo import models, fields

class Customer(models.Model):
    _name = 'pharmacy.customer'
    _description = 'Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    name = fields.Char(string='Name', required=True)
    contact = fields.Char(string='Contact')
    prescription_history = fields.Text(string='Prescription History')
