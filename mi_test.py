# -*- coding: utf-8 -*-
from openerp import models, fields
class mi_testeo_mi_test(models.Model):
	_name="mi_testeo.mi_test"

	nombre = fields.Char('Nombre', required=True)
	edad = fields.Integer('Edad')
	profesion = fields.Boolean('Profesión ?')
	nombreProfesion = fields.Char('Profesión')
	rut = fields.Char('Rut', required=True)
	email = fields.Char('Email')
	categoria = fields.Selection([('agricultura',('Agricultura')),
		('urbano', ('Urbano')),
		('educacion', ('Educación'))])
	idea = fields.Text('Exponer idea')

	