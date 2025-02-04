from odoo import models, fields, api

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'instruktur'
    _inherit = {'res.partner': 'partner_id'}
    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, onDelete='cascade')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', relation='instruktur_keahlian_rel', string='Keahlian')
    
  
class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'Keahlian'
    
    name = fields.Char(string='Keahlian', required=True)
    # instruktur_ids = fields.Many2many(comodel_name='instruktur', relation='instruktur_keahlian_rel', string='Instruktur')
    