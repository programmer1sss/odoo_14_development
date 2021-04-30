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
    telephone = fields.Char(
        string='Telephone',
    )
    state = fields.Selection(
        string='state',
        selection=[('in_hospital', 'In hospital'), 
                   ('on_sick_leave', 'On sick leave'),
                   ('discharged', 'Discharged')]
    )
    def change_state(self, new_state):
        for patient in self:
            if patient.state == new_state :
                raise models.ValidationError('The patient is already on sick leave')
            else:
                patient.state = new_state         

    def issue_sick_leave(self):
        self.change_state('in_hospital')
    
    def create_visit(self):
       
        record = self.env['hospital.visit'].create({'data': fields.Date.today(),'patient_id': self.id })
        return {
      
        'res_model': 'hospital.visit',
        'res_id': record.id,
        'type': 'ir.actions.act_window',
        'context': {},
        'view_mode': 'form',       
        'target':  'current',

    }
    
    def q_visit(self):
        visitObj=self.env['hospital.visit']
       
        raise models.ValidationError(visitObj.search_count([('patient_id','=', self.id )]))
                
                

    @api.constrains('telephone')
    def check_telephone(self):
        for patient in self:
            recs=self.search_count([('telephone','=',patient.telephone)])
            if recs >1:
                raise models.ValidationError('The phone error')
           
  



    
 




    
    


    
 

