# -*- coding: utf-8 -*-
from odoo import api,fields,models
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    
    name=fields.Char(
        'Name patient',
        required=True)
    gender = fields.Selection([('women', 'Women'),('men', 'Men')],
    string='Gender',
    )
    birthday= fields.Date(
        'Birthday'
    )
    comment = fields.Text(
        'comment'
    )  
    telephone = fields.Integer(
        string='Telephone',
    )

    @api.constrains('telephone')
    def check_telephone(self):
        for patient in self:
            recs=self.search_count([('telephone','=',patient.telephone)])
            if recs >1:
                raise models.ValidationError('The phone error')
           
  

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    
    name = fields.Char(
        'Name doctor',
        required=True,
    )  
    title = fields.Selection(
        selection=[('nurse', 'Nurse'),('doctor', 'Doctor'),('head_physician', 'Head physician')],
        string='Rank', 
    )
    date_of_hiring = fields.Date(
        'Enrollment Date',
    )
    education  = fields.Boolean(
        "Education"
    )
    patient_ids = fields.Many2many(
        'hospital.patient',
        string='Patient',
    )
    unit_id = fields.Many2one(
        'hospital.unit',
        string='unit',
    )
    

class HospitalVisit(models.Model):
    _name = 'hospital.visit'
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
             
    
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

