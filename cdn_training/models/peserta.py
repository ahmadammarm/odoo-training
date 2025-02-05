from odoo import models, fields, api

class Peserta(models.Model):
    _name = 'peserta'
    _description = 'Peserta'
    _inherit = {"res.partner" : "partner_id"}
    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', required=True, ondelete='cascade')
    pendidikan = fields.Selection(string='Jenjang Pendidikan', selection=[('sd', 'SD'), ('smp', 'SMP'), ('sma', 'SMA'), ('s1', 'Sarjana S1')])
    pekerjaan = fields.Char(string='Pekerjaan')
    is_menikah = fields.Boolean(string='Sudah Menikah')
    nama_pasangan = fields.Char(string='Nama Pasangan')
    hp_pasangan = fields.Char(string='HP Pasangan')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_peserta = fields.Char(string='No Peserta', readonly=True)
    
    @api.model
    def create(self, vals):
        vals['no_peserta'] = self.env['ir.sequence'].next_by_code('peserta')
        return super(Peserta, self).create(vals)