{
    'name': 'Freja eID Integration',
    'version': '14.0.1.0.1',
    'author': 'Verified Email Europe AB',
    'maintainer': 'Verified Email Europe AB',
    'contributors': 'Hemangi Rupareliya, Verified Email Europe AB, Fredrik Arvas',
    'website': 'https://verified-email.com/',
    'license': 'AGPL-3',
    'category': 'Tools',
    'depends': [
        'auth_oauth',
        'partner_ssn', # https://github.com/VerifiedEmailEurope/ve-odoo-base/tree/14.0
        'portal',
        'partner_extenstion_verifiedemail' # https://github.com/VerifiedEmailEurope/ve-odoo-base/tree/14.0
    ],
    'data': {
        'views/provider_views.xml',
        'views/portal_templates.xml'
    },
    'application': False,
    'installable': True,
}
