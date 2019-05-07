# -*- coding: utf-8 -*-
from flectra import api, fields, models


class buyerinfo(models.Model):
    _name="entity.information"

    name = fields.Char(string = "Name  ",required=True)
    type = fields.Selection([('electronic', 'electronics'),
                                   ('furniture', 'furniture'),('twowheeler','twowheeler')], string="Types  ")

    entity= fields.Integer(string="ID")
    manufacture_date= fields.Integer(string="Manufacture date")

    seller_ids = fields.Many2many("seller.info", "seller_entity_rel",
                                  "entity_id","seller_id" , string="Sellers")