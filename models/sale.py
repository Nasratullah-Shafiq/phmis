from odoo import models, fields, api

class PharmacySale(models.Model):
    _name = 'pharmacy.sale'
    _description = 'Pharmacy Sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    medicine_id = fields.Many2one('pharmacy.medicine', string="Medicine", required=True)
    customer_id = fields.Many2one('pharmacy.customer', string="Customer", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    price = fields.Float(string="Unit Price", required=True)
    total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=True)
    date = fields.Date(string="Sale Date", default=fields.Date.today, required=True)

    @api.depends('quantity', 'price')
    def _compute_total_price(self):
        """Compute total price for each sale."""
        for record in self:
            record.total_price = record.quantity * record.price
