from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_category = fields.Selection([
        ('consultant', 'Consultant'),
        ('education', 'Education-Based')
    ], string="Employee Category", default='consultant')
    provident_fund = fields.Char(string='Provident Fund')
    employee_esic = fields.Char(string='ESIC')
    professional_tax  = fields.Char(string='Professional Tax ')
    employee_doj  = fields.Char(string='Date of Joining')
    aadhar_no  = fields.Char(string='Aadhar No')
    pf_no  = fields.Char(string='PF No')
    uan_no  = fields.Char(string='UAN No')
    eisc_no  = fields.Char(string='EISC No')
