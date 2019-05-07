# -*- coding: utf-8 -*-
from flectra import api, fields, models


class courseinfo(models.Model):
    _name="course.information"

    name = fields.Char(string = "Enter course Name")
    course_ids= fields.Char(tring="course id ")
    course_type = fields.Selection([('ce', 'ce'),
                                   ('me', 'me'),('accounts','accounts')], string="courses  :")

    duration= fields.Integer(string="duration of course   :")
    certificate = fields.Boolean(string="certificate   ?")
    total_student=fields.Integer(string="total number of student")



  #  start_date = fields.Date(string='data')

    student = fields.One2many("student.information", 'course_id',string="student list")

    faculty_ids = fields.Many2many("faculty.information", "faculty_course_rel",
                                   "faculty_id", "course_id", string="faculty")