from odoo import http
from odoo.http import request

class HospitalController(http.Controller):
    
    @http.route('/hospital/doctors', type='http', auth='public', website=True)
    def list_doctors(self, **kwargs):
        doctors=request.env['hospital.doctor'].sudo().search([])
        return request.render('hospital_management.doctor_list_template', {'doctors': doctors,})

    @http.route('/hospital/patients', type='http', auth='user', website=True)
    def list_patients(self, **kwargs):
        patients=request.env['hospital.patient'].sudo().search([])
        return request.render('hospital_management.patient_list_template', {'patients': patients,})