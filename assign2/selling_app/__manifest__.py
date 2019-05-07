# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name': 'selling info',
    'author': 'ketul',
    'version': '1.1',
    'sequence': 30,
    'description': """
selling app
    """,
    'data': ['view/seller_info.xml','view/buying_info.xml','view/entity_info.xml'],
    'depends': ['base'],
    'installable': True,
    'application': True,
    'auto_install': False,
}