
# -*- coding: utf-8 -*-
{
    'name': "SSI customerPOs",


    'author': "Kristenn",
    'website': "http://kristennquem.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
