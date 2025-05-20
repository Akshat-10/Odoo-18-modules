{
    'name': 'Many2Many Quick Preview',
    'author': 'Odoo Hub',
    'category': 'Tools',
    'summary': 'Provides quick preview of records in many2many tags, many2many preview, many2many clickable, Odoo record preview, many2many field preview, many2many field clickable, many2many tags clickable, many2many_tags clickable, many2many_tags preview, tags preview, tags clickable, clickable tag',
    'description': """
        Many2Many Quick Preview is an Odoo app that allows users to instantly preview related records in many2many fields directly from the many2many_tags. 
        This app improves navigation and productivity by providing quick access to record details without having to open them individually.
    """,
    'maintainer': 'Odoo Hub',
    'version': '1.0',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'many2many_quick_preview/static/src/js/many2many_tags_field.js',
        ],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
