# -*- coding: utf-8 -*-
{
    'name': "My Hospital", 
    'summary': "Manage hospital easily",  
    'description': """
Manage Hospital
==============
Description related to hospital..
    """,  
    'author': "Arthur",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': [ 'base','mail'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hospital_menu_views.xml',        
        'views/hospital_doctor_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_visit_views.xml',
        'views/hospital_unit_views.xml',
        'views/hospital_technical_staff_views.xml',
        'views/hospital_contact_advertising_views.xml',
        

    ],
}



