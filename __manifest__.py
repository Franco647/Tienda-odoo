{
    'name': 'Tienda',
    'version': '1.0',
    'author': 'Franco',
    'sequence': 1,
    'description': 'Este es un módulo para dar de alta productos, categorias y pedidos',
    'category': 'Sales',
    'data': [
        'views/tienda_views.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml'
        ],
    'installable': True,
    'application': True,
    'depends': ['base'],
    'license': 'LGPL-3',
    'icon': '/tienda/static/img/shop.png',
}