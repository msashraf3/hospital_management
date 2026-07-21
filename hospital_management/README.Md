# Hospital Management (Odoo 19)

A custom Odoo module built from scratch to learn Odoo development — managing patients, doctors, and appointments.

## 🎯 Purpose
Learning project: building a real Odoo module step-by-step while learning core Odoo concepts (models, views, security, workflows).

## ✅ Progress
- [x] Module scaffold created
- [x] Doctor model
- [x] Patient model
- [x] Appointment model (linked to Patient + Doctor)
- [x] Many2one relationships (Patient/Appointment → Doctor)
- [x] One2many reverse relationships (Doctor/Patient → Appointments)
- [x] Views (list/form) for all models
- [x] Security & access rights
- [x] Menus
- [x] Business logic (status workflow buttons, computed fields, constraints)
- [ ] Related fields
- [ ] Appointment scheduling rules (doctor availability, slot limits)

## 🧩 Models
- **hospital.doctor** — name, specialization, department, contact info
- **hospital.patient** — name, age, gender, medical history, assigned doctor
- **hospital.appointment** — links a patient + doctor, tracks date, severity, status

## 🛠 Tech
- Odoo 19 (source install)
- PostgreSQL

## 📸 Screenshots

**Kanban View**
![Doctor List View](screenshots/kanban_view.png)

**Search, Filter & Group By**
![Doctor List View](screenshots/search_by_specific_fields.png)
![Doctor List View](screenshots/group_by_search_feature.png)

**Doctor List and Form View**
![Doctor List View](screenshots/doctors_list.png)
![Doctor form View](screenshots/doctor_form_view.png)

**Patient Form with Linked Appointments and list view**
![Patient Form](screenshots/patient_form.png)
![Patient Form](screenshots/patient_list.png)

**Appointment Form and List**
![Appointment Form](screenshots/appointment_form.png)
![Appointment Confirmed Button](screenshots/appointment_confirmed_button.png)
![Appointment Done Button](screenshots/appointment_done_button.png)
![Appointment Cancel Button](screenshots/appointment_cancel_buttons.png)
![Appointment Form](screenshots/appointment_list.png)