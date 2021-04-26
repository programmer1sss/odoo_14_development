# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import ValidationError


class HospitalTechnicalStaff(models.Model):
    _name = 'hospital.staff'
    _inherit =['hospital.contact']
    _description = 'Technical Staff'

    technical_worker = fields.Boolean(
        string='Technical Worker',
    )

    
    
    

    
    
    
    
    


    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

