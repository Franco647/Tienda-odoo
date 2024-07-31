from odoo import api, fields, models

class TiendaCategoria(models.Model):
    _name = 'tienda.categoria'
    
    nombre = fields.Char('Nombre', required = True)

    def _compute_display_name(self):
        for obj in self:
            obj.display_name = obj.nombre