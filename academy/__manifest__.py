# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        Belajar Building Website Odoo""",

    'description': """
        Building Website Module Odoo 11
    """,

    'author': "adesdev",
    'website': "https://digitalfarmer.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Learning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}