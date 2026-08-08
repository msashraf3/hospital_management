{
    "name": "Hospital Management",
    "version": "19.0.1.0.0",
    "summary": "Manage Patients, Doctors and  Appointments",
    "depends": ["base", "website"],
    "author": "Shamim, Betopia Group.",
    "category": "Services/Hospital",
    "description": """
    A custom Hospital Management System built for learning Odoo.
    """,
    # data files always loaded at installation
    "data": [
        "security/hospital_security.xml",
        "security/ir.model.access.csv",
        "security/hospital_record_rules.xml",
        "views/doctor_views.xml",
        "views/patient_views.xml",
        "views/appointment_views.xml",
        "views/website_templates.xml",
        "views/patient_website_templates.xml",
    ],
    "installable": True,
    "application": True,
}
