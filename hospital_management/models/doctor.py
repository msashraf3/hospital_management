from odoo import models, fields

class HospitalDoctor(models.Model):
    _name="hospital.doctor"
    _description="Hospital Doctor"

    name=fields.Char(string="Doctor Name",  required=True)
    age=fields.Integer(string="Age")
    gender=fields.Selection([('male','Male'), ('female', 'Female'),('others','Others')], string="Gender")
    specialization=fields.Char(string="Specialization")
    department=fields.Char(string="Department")
    date_of_birth=fields.Date(string="Date of Birth")
    phone=fields.Char(string="Phone Number")
    email=fields.Char(string="E-mail Address")
