{
    'name' : "Hospital Master",
    'Summary' : "All master data of hospital managed by this module",
    'data' : [
        'security/ir.model.access.csv',
        'views/bed_details.xml',
        'views/floor_details.xml',
        'views/room_details.xml',
        'views/menuitem.xml',
    ],
    'application' : True,
    'installable': True,
    'auto_install' : False,
    'sequence' : 2,
}