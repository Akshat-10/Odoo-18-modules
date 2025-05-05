# -*- coding: utf-8 -*-
{
    'name': 'Odoo Chatter',
    'summary': """The Odoo Chatter module is designed to enhance Odoo
                  activity management system, enabling users to efficiently handle activities, 
                  logs, and messages related to specific records. By introducing model and record 
                  selection tools, the module provides a streamlined approach to viewing and managing 
                  record-specific activities.
                  With features like detailed activity logs, centralized tracking, and full control over 
                  adding, editing, and deleting activities, this module ensures improved productivity and traceability.
                  Whether for communication, updates, or audit purposes, it empowers users to maintain organized and 
                  detailed records effortlessly.
               """,

    'description': """
            The Odoo Chatter Module provides a comprehensive 
            solution for managing record-specific activities, logs, and 
            messages within Odoo 18.
            Key Features:
            Dropdown Selections for Models and Records
            Adds two dropdown menus:
            One for selecting a model.
            Another for selecting a specific record within the chosen model.
            Detailed Activity Log View
            Displays all logs, messages, and activities related to the selected record in a centralized activity log.
            Ensures users can easily track actions performed on specific records.
            Complete Activity Management           
            Enables users to add, update, edit, or delete activities, logs, and messages associated with the selected record.
            Supports seamless communication and tracking of record-specific actions.
            This module improves the traceability and organization of record-specific activities, empowering users to efficiently manage their workflow and maintain a clear activity history.
    """,

    'author': "Ksolves India Ltd.",
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 0,
    'website': "https://store.ksolves.com/",
    'maintainer': 'Ksolves India Ltd.',
    'version': '18.0.1.0.0',
    'support': 'sales@ksolves.com',
    'images': ['static/description/Odoo_Chatter_Banner.png'],
    'live_test_url': 'https://odoochatter18.kappso.com/web/demo_login',
    'depends': ['base', 'mail'],

    'data': [
    ],
    'assets': {

        'web.assets_backend': [
            'ks_chatter/static/src/core/web/ks_chatter.xml',
            'ks_chatter/static/src/core/web/ks_chatter.js',
            'ks_chatter/static/src/css/style.css',
        ],
        'web.assets_frontend': [
            'ks_chatter/static/src/css/style.css',
        ],
    },

    'installable': True,

    'application': True,

}
