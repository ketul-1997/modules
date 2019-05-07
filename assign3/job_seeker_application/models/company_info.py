# -*- coding: utf-8 -*-
from flectra import api, fields, models


class companyinfo(models.Model):
    _name="company.information"

    name = fields.Char(string = "company name")

    post_id = fields.Many2one("job.info", string="posts ")
   # jobseeker_id=fields.Many2many("jobseeker.info","jobseeker_company_rel","company_ids","jobseeker_ids",string="Employees")