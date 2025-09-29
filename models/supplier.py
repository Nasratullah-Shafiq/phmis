from odoo import models, fields

class Supplier(models.Model):
    _name = 'pharmacy.supplier'
    _description = 'Supplier'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    name = fields.Char(string='Name', required=True)
    contact = fields.Char(string='Contact')
    address = fields.Text(string='Address')
