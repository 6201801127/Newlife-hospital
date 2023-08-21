from odoo import models, fields, api,_ 

class DoctorDetails(models.Model):

    _name="doctor.details"
    _description ="Doctor Details"


    name = fields.Char(string="Name of Doctor")
    registration_no = fields.Char(string="Doctor registration no.")
    specialized = fields.Many2one(comodel_name="doctor.category.master", string="Specialized on")
    doctor_timing_mrng = fields.Datetime(string="Doctor timing in morning")
    doctor_timing_evng = fields.Datetime(string="Doctor timing in evening")