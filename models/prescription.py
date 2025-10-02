from odoo import models, fields

class Prescription(models.Model):
    _name = 'pharmacy.prescription'
    _description = 'Prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    file = fields.Binary(string='Prescription File')
    customer_id = fields.Many2one('pharmacy.customer', string='Customer')
    date = fields.Date(string='Date', default=fields.Date.today)
