from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"

    name = fields.Char(string="Doctor Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender"
    )
    specialization = fields.Char(string="Specialization")
    department = fields.Char(string="Department")
    date_of_birth = fields.Date(string="Date of Birth")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="E-mail Address")
    appointment_ids = fields.One2many(
        "hospital.appointment", "doctor_id", string="Appointments"
    )

    appointment_count=fields.Integer(string="Total Appointment" ,compute='_compute_appointment_count')

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count=len(record.appointment_ids)