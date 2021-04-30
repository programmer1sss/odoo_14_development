# -*- coding: utf-8 -*-
from odoo import api,fields,models
from odoo.exceptions import ValidationError
from datetime import date, datetime



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

    def create_patient(self):
        t_date= datetime.strptime('1958-04-11', "%Y-%m-%d").date()
        record = self.env['hospital.patient'].create({
            'name': 'Шевченко Тарас Николаевич',
            'gender':'men',
            'birthday':  t_date,
            'comment':'pay attention to high pressure '
        })
        return True
            
            
    
            
    
    
    
    
    

    
 




    
    


    
 

