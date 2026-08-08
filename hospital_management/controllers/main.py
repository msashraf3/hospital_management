from odoo import http
from odoo.http import request

class HospitalController(http.Controller):
    
    @http.route('/hospital/doctors', type='http', auth='public', website=True)
    def list_doctors(self, **kwargs):
        doctors=request.env['hospital.doctor'].sudo().search([])
        return request.render('hospital_management.doctor_list_template', {'doctors': doctors,})