# -*- coding: utf-8 -*-
from odoo import api,fields,models
from odoo.exceptions import ValidationError

class HospitalContactAdvertisingCompanies(models.Model):
    
    _name = 'hospital.contact.advertising.company'
    _inherits ={'res.partner':'partner_id'}
    _description = 'Contacts of advertising companies'
    
    first_name = fields.Char(string="Name")
    
    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='cascade',
    )
    

    
    


    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

