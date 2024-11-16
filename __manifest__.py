{
    'name': 'Custom Report Header/Footer',
    'version': '17.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Custom Header and Footer for Reports',
    'description': 'Allows configuration of JPEG header and footer images for reports.',
    'author': 'Oleksii Panpukha',
    'website': 'https://github.com/3xecut0r',
    'depends': ['base', 'web'],
    'data': [
        'views/report_templates.xml',
        'views/base_document_layout_views.xml',
        'data/report_layout.xml',
    ],
    'installable': True,
    'application': False,
}