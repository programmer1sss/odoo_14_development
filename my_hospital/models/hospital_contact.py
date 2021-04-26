# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import ValidationError


class HospitalContact(models.Model):
    _name = 'hospital.contact'
    _description = 'Contacts of Hospital'
    
    first_name = fields.Char(
        string="Name",
    )
    last_name = fields.Char(
        string='Last name',
    )
    patronymic = fields.Char(
        string='Mid­dle Name',
    )
    # mid­dle_name = fields.Char(
    #     string='Mid­dle Name',
    # )
    phone = fields.Char(
        string='Phone',
    )
    
    

    

    

    
    


    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

