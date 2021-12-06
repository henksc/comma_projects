# -*- coding: utf-8 -*-
{
    'name': 'SA Comma Project Integration',
    'version': '14.0.1.0.1',
    'summary': 'Integration between Odoo Project module and Comma core module',
    'price': 99,
    'currency': 'EUR',
    'support':'support@securityadvice.be',
    'sequence': -120,
    'description': """Link your projects to the GRC concepts""",
    'category': 'Productivity',
    'author': 'info@securityadvice.be',
    'website': 'https://www.securityadvice.be',
    'images': [''],
    'depends': ['base', 'mail', 'sa_grc_core', 'project'],
    'data': [
        'views/project_project_views.xml',
    ],
    'demo': [
        'demo/risk_demo.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'Other proprietary'
}
