from odoo import models, fields, api
from datetime import date

class Medicine(models.Model):
    _name = 'pharmacy.medicine'
    _description = 'Medicine'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    name = fields.Char(string='Name', required=True)
    brand = fields.Char(string='Brand')
    generic_name = fields.Char(string='Generic Name')
    category = fields.Selection([
        ('otc', 'OTC'),
        ('prescription', 'Prescription'),
        ('supplement', 'Supplement'),
    ], string='Category')
    batch_no = fields.Char(string='Batch Number')
    expiry_date = fields.Date(string='Expiry Date')
    quantity = fields.Integer(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    selling_price = fields.Float(string='Selling Price')

    @api.depends('quantity')
    def check_low_stock(self):
        for record in self:
            record.low_stock = record.quantity < 10

    low_stock = fields.Boolean(string='Low Stock', compute='check_low_stock', store=True)
