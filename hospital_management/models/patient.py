from odoo import models, fields


class HospitalPatient(models.Model):

    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender"
    )
    doctor_id = fields.Many2one("hospital.doctor", string="Assigned Doctor")
    medical_history = fields.Text(string="Previous Medical History")
    phone = fields.Char(string="Phone number")
    date_of_birth = fields.Date(string="Date Of Birth")
    appointment_ids = fields.One2many(
        "hospital.appointment", "patient_id", string="Appointments"
    )
