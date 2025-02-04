from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training_course'
    _description = 'Training Course'
    
    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible')
    session_line =  fields.One2many(comodel_name='training_session', inverse_name='course_id', string='Sessions')
    tempat = fields.Char(string='Tempat Kursus', required=True)
    

class TrainingSession(models.Model):
    _name = 'training_session'
    _description = 'Training Session'
    
    name = fields.Char(string='Session Name', required=True)
    course_id = fields.Many2one(comodel_name='training_course', string='Course', required=True, onDelete='cascade')
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Float(string='Duration', required=True)
    seats = fields.Integer(string='Seats', required=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta')
    
