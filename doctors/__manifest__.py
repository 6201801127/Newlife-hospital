{
    'name' : "Doctors",
    'summary' : "This is the module where manage all doctor details",
    'version': '16.0',
    'category' : "Web Application",
    'author' : "Ajay Kumar Ravidas",
    'license': 'LGPL-3',
    'depends': ['hospital_master'],
    'data' : [
        'security/ir.model.access.csv',
        'views/doctor_details.xml',
        'views/menuitem.xml',
    ],
    'application': True,
    'installable': True,
    'auto_installation': False,
    'sequence' : 1,
    'price': 49.99,
    'currency': 'USD',
    'images': ['static/description/doctor.jpg'],
}