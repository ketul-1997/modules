# -*- coding: utf-8 -*-
from flectra import api, fields, models


class facultyinfo(models.Model):
    _name="faculty.information"

    name = fields.Char(string = "Enter Name")
    mobile_no = fields.Integer(string="Enter mobile no   :")
    graduation = fields.Text(string="Enter graduation")
    teaching_experience = fields.Integer(string="teaching experience")
    #start_date = fields.Date(string='data')

    course_ids = fields.Many2many("course.information", "faculty_course_rel",
                                    "faculty_id","course_id", string="courses")