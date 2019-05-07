# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name': 'job seeker application',
    'author': 'ketul',
    'version': '1.1',
    'sequence': 30,
    'description': """
selling app
    """,
    'data': ['view/company_info.xml','view/job_info.xml','view/jobseeker_info.xml'],
    'depends': ['base'],
    'installable': True,
    'application': True,
    'auto_install': False,
}