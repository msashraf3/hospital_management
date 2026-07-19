{
    "name": "Hospital Management",
    "version": "19.0.1.0.0",
    "summary": "Manage Patients, Doctors and  Appointments",
    "depends": ["base"],
    "author": "Shamim, Betopia Group.",
    "category": "Services/Hospital",
    "description": """
    A custom Hospital Management System built for learning Odoo.
    """,
    # data files always loaded at installation
    "data": [
        "security/ir.model.access.csv",
        "views/doctor_views.xml",
        "views/patient_views.xml",
    ],
    "installable": True,
    "application": True,
}
