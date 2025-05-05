# -*- coding: utf-8 -*-
{
    'name': "ylhc_theme_base",

    'summary': """
        Base for themes, it support free login for odoo
    """,

    'description': """
        Odoo Login, 
        Odoo login page, 
        Odoo login theme
        Login, 
        ylhc Theme Base,
        ylhc Theme,
        Ylhc Theme,
        Multi tab theme,
        Pop form theme
    """,

    'author': "ylhctec",

    'website': "https://www.ylhctec.com",
    'live_test_url': 'https://www.ylhctec.com',

    'license': 'OPL-1',
    'images': ['static/description/screen_shot.png', 'static/description/banner.png'],
    'maintainer': 'ylhctec',
    'category': 'Theme/Backend',
    'version': '18.0.0.3',

    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 0.0,
    'currency': 'EUR',

    'depends': ['base', 'web'],
    
    'data': [],

    'assets': {
        'web.assets_backend': [
            'ylhc_theme_base/static/css/ylhc_scroll.scss',
            'ylhc_theme_base/static/css/ylhc_misc.scss',
        ]
    }
}
