# -*- coding: utf-8 -*-
from flectra import api, fields, models


class jobinfo(models.Model):
    _name="job.info"

    name= fields.Char(string = "job post  ",required=True)
    job_type = fields.Selection([('trainie', 'trainie'),
                                   ('onroll', 'onroll')], string="job Type")

    company_id = fields.One2many("company.information", 'post_id', string="compamnies")
    #seeker_id = fields.Many2one("jobseeker.info", string="seekers")
    jobseeker = fields.Many2many("jobseeker.info", "job_company_rel", "company_ids","jobseeker_ids" , string="seekers")


