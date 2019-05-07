# -*- coding: utf-8 -*-
from flectra import api, fields, models


class jobseekerinfo(models.Model):
    _name="jobseeker.info"

    name= fields.Char(string = "name  ",required=True)
    mobile_no= fields.Integer(string = "mobile no")
    graduation=fields.Text(string="graduation")
    salary=fields.Integer(string="salary")
    job_type = fields.Selection([('trainie', 'trainie'),
                                   ('onroll', 'onroll')], string="job Type")
    state = fields.Selection([('applied', 'applied'), ('selected', 'selected'), ('onroll', 'onroll'),('cancle','cancle')], string="status")

    #job_id = fields.One2many("job.info", 'seeker_id', string="posts ")
    company_idss = fields.Many2many("job.info", "job_company_rel", "jobseeker_ids", "company_ids",string="posts")

    def s_applied(self):
        self.state = "applied"

    def s_selected(self):
        self.state = "selected"

    def s_onroll(self):
        self.state = "onroll"

    def s_cancle(self):
        self.state = "cancle"