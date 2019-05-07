# -*- coding: utf-8 -*-
from flectra import api, fields, models


class sellerinfo(models.Model):
    _name="seller.info"

    name = fields.Char(string = "Name  ",required=True)
    selling_type = fields.Selection([('electronic', 'electronics'),
                                   ('furniture', 'furniture'),('twowheeler','twowheeler')], string="Types")

    mobile_no= fields.Integer(string="Mobile no")
    expected_amount = fields.Integer(string="Expected amount")

    buyer_id = fields.Many2one("buyer.information", string="Buyers")

    entity_ids = fields.Many2many("entity.information", "seller_entity_rel",
                                  "seller_id", "entity_id", string= "Entities")