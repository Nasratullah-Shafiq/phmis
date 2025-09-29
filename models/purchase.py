from odoo import models, fields, api

class PharmacyPurchase(models.Model):
    _name = 'pharmacy.purchase'
    _description = 'Pharmacy Purchase'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- Add chatter support

    medicine_id = fields.Many2one('pharmacy.medicine', string="Medicine", required=True)
    supplier_id = fields.Many2one('pharmacy.supplier', string="Supplier", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    unit_price = fields.Float(string="Unit Price", required=True)
    total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=True)
    date = fields.Date(string="Purchase Date", default=fields.Date.today, required=True)

    @api.depends('quantity', 'unit_price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.quantity * record.unit_price
