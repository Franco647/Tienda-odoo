from odoo import api, fields, models 

class TiendaCliente(models.Model):
    _name = 'tienda.cliente'

    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    email = fields.Char(string='Correo Electrónico')
    foto = fields.Binary('Foto')
   
    def _compute_display_name(self):
        for obj in self:
            obj.display_name = obj.nombre