from odoo import models, api, fields, _ 


class DoctorCategoryMAster(models.Model):

    _name = "doctor.category.master"
    _description = "Doctor category master"
    _rec_name ="category_name"

    category_name = fields.Char(string="Category Name")
    ref_code = fields.Char('Ref. Code')
    description = fields.Char(string="Description")
