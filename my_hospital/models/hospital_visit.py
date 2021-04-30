# -*- coding: utf-8 -*-
from odoo import api,fields,models
from odoo.exceptions import ValidationError

class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Visits'
    

    name = fields.Char(
        string='Name',
    )
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
    )
    data = fields.Date(
        string='Data Visit',
        default=fields.Date.context_today,
    )
    diagnosis = fields.Html(
        string='Diagnosis',
    )
    patient_gender = fields.Selection(
        
        string='Gender',
        related='patient_id.gender',
        readonly=True,
        store=True   
    )
    temperature = fields.Float(
        string='Body Temperature',
        digits=(4, 4),
    )
    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency',
    )
    cost = fields.Monetary(
        string='Cost of Services',
        currency_field='currency_id',
    )
    
    @api.constrains('temperature')
    def check_temperature(self):
        for visit in self:
            if visit.temperature < 35 or visit.temperature > 45:
                raise models.ValidationError('Wrong value')
             
    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

