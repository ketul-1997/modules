# -*- coding: utf-8 -*-
from flectra import api, fields, models
from flectra.exceptions import ValidationError


class studentinfo(models.Model):
    _name="student.information"

    name = fields.Char(string = "Enter Name",required=True)
    age = fields.Integer(string="Enter your age")
    gender = fields.Selection([('male', 'male'),
                                   ('female', 'female')], string="Gender  :")

    mobile_no = fields.Char(string="Enter mobile no   :")
    graduation = fields.Selection([('ssc', 'ssc'),
                                   ('hsc', 'hsc')], string="Enter your graduation  :")
    address = fields.Text(string="address  :",required=True)
    email = fields.Text(string="E-mail  :", required=True,unique=True)
    course_id = fields.Many2one("course.information", string="course")

    state = fields.Selection([('success', 'Success'),('pending', 'Pending'),('cancel','Cancel')], string="status")

   # start_date = fields.Date(string='data')
    _sql_constraints = [('name_uniq', 'unique(name)', "please enter proper number.")]
    _sql_constraints = [('name_uniq', 'unique(email)', "please enter unique email.")]


    @api.constrains('mobile_no')
    def check_room_area(self):
        if len(self.mobile_no) > 10:
            raise ValidationError("mobile number should be less than 10.")


    @api.onchange('course_id')
    def _onchange_code(self):
        print("this is onchange", self.name)
        self.name = self.course_id.name

    def s_success(self):
        self.state = "success"

    def s_pending(self):
        self.state = "pending"

    def s_cancel(self):
        self.state = "cancel"
