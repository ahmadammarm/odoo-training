from odoo import models, fields, api

class Mahasiswa(models.Model):
    _name = 'mahasiswa'
    _description = 'Mahasiswa'
    _sql_constraints = [
        ('nim_uniq', 'unique(nim)', 'NIM sudah ada!')
    ]
    
    nama = fields.Char(string='Nama', required=True)
    nim = fields.Char(string='NIM', required=True)
    prodi = fields.Char(string='Prodi', required=True)
    angkatan = fields.Integer(string='Angkatan', required=True)
    
    