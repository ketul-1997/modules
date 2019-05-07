# -*- coding: utf-8 -*-
from flectra import fields, models


class buyerinfo(models.Model):
    _name = "buyer.information"

    state = fields.Selection([('success', 'Success'), ('pending', 'Pending'), ('cancel', 'Cancel')], string="status")
    name = fields.Char(string="Name", required=True)
    buying_type = fields.Selection([('electronic', 'electronics'),
                                    ('furniture', 'furniture'), ('twowheeler', 'twowheeler')], string="Types")

    mobile_nos = fields.Integer(string="Mobile")
    range = fields.Integer(string="Range")
    seller_id = fields.One2many("seller.info", 'buyer_id', string="Seller")
    

    def s_success(self):
        self.state = "success"

    def s_pending(self):
        self.state = "pending"

    def s_cancel(self):
        self.state = "cancel"