from odoo import fields, models, api
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor", required=True)
    appointment_date = fields.Datetime(string="Appointment Date and Time", required=True)
    reason = fields.Char(string="Possible reason of your illness, according to you.")
    severity = fields.Selection(
        [
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        string="Severity",
    )
    is_contagious = fields.Boolean(string="Contagious")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
    )

    # confirmed button for the appointment
    def action_confirm(self):
        self.status = "confirmed"

    # done button for the appointment after they are released
    def action_done(self):
        self.status = "done"

    # cancel button, whenever they want to cancel
    def action_cancel(self):
        self.status = "cancelled"

    def action_view_doctors(self):
        return {
            "name": "Assigned Doctor",
            "type": "ir.actions.act_window",
            "res_model": "hospital.doctor",
            "view_mode": "form",
            "res_id": self.doctor_id.id,
        }

    def action_view_patients(self):
        return {
            "name": "Assigned Patient",
            "type": "ir.actions.act_window",
            "res_model": "hospital.patient",
            "view_mode": "form",
            "res_id": self.patient_id.id,
        }

    @api.constrains("doctor_id", "appointment_date")
    def _check_double_booking(self):
        for record in self:
            if record.doctor_id and record.appointment_date:
                conflicting = self.search(
                    [
                        ("id", "!=", record.id),
                        ("doctor_id", "=", record.doctor_id.id),
                        ("appointment_date", "=", record.appointment_date),
                        ("status", "!=", "cancelled"),
                    ]
                )
                if conflicting:
                    raise ValidationError(
                        f"Dr. {record.doctor_id.name} already has an appointment at this exact Date/Time."
                    )

    @api.constrains("appointment_date")
    def _check_past_dates(self):
        for record in self:
            DateNow = fields.Datetime.now()
            if record.appointment_date < fields.Datetime.now():
                raise ValidationError(
                    f"Appointment Date can't be in the past. Please select {DateNow} or in the future."
                )
