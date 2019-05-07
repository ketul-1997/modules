# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name': 'student info',
    'author': 'ketul',
    'version': '1.1',
    'sequence': 30,
    'description': """
society info app
    """,
    'category': 'accounting',
    'data': ['view/student_info.xml','view/course_detail.xml','view/faculty_info.xml'],
    'depends': ['base'],
    'installable': True,
    'application': False,
    'auto_install': False,
}