# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalUnit(models.Model):
    _name = 'hospital.unit'
    _description = 'Hospital Unit'

    name = fields.Char(
        string='Hospital Unit',
        required=True,
    )
    quantity_doctor = fields.Integer(
        string='Number of doctors in the department',
        compute='_compute_count_doctors',
    )
    doctor_ids = fields.One2many(
        'hospital.doctor',
        'unit_id',
        string='doctor',
    )
        
    @api.depends('doctor_ids')
    def _compute_count_doctors(self):
        for unit in self:
            unit.quantity_doctor = len(unit.doctor_ids)
    
    


    
 

