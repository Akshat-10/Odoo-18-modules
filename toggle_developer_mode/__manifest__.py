{
    'name': "Toggle Debug Mode",
    'version': '18.0',
    'category': 'Tools',
    'author': "cube48 AG",
    'website': "https://www.cube48.de",
    'license': "AGPL-3",
    'summary': """
        Toggle to debug mode in the top right user menu, just one click!""",
    'description': """
        Toggle to debug mode in the top right user menu, just one click!

    """,
    'depends': [
        'base', 
        'web',
    ],
    'assets': {
        'web.assets_backend': [
            'toggle_developer_mode/static/src/css/app.css',
            'toggle_developer_mode/static/src/js/debug_mode_js.js',
        ],
    },
    'images': ["static/description/banner.png"],
    'installable': True,
    'application': True,
}
