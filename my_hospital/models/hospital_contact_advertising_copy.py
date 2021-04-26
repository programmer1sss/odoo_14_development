# -*- coding: utf-8 -*-

from odoo import api,fields,models
from odoo.exceptions import ValidationError


class HospitalContactAdvertising(models.Model):
    _name = 'hospital.advertising'
    _inherit ='hospital.contact'
    _description = 'Contacts of advertising companies'
    
    website = fields.Char(
        string="Name"
    )
    facebook = fields.Char(
        string='Facebook',
    )
    recommendation = fields.Char(
        string='Recommendation',
    )
    sending_sms = fields.Char(
        string='Sending SMS',
    )
    

    
    


    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

