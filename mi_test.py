# -*- coding: utf-8 -*-
from openerp import models, fields, api

class mi_testeo_mi_test(models.Model):
	_name="mi_testeo.mi_test"

	nombre = fields.Char('Nombre', required=True)
	edad = fields.Integer('Edad')
	profesion = fields.Boolean('Tiene profesión?')
	nombreProfesion = fields.Char('Profesión')
	categoriaProfesion = fields.Selection([
		('informatica',('Informatica')),
		('mecanica',('Mecanica')),
		('recursos humanos',('Recursos Humanos')),
		('finanzas',('Finanzas')),
		('educacion',('Educación')),
		('otros',('Otros'))])
	rut = fields.Char('Rut', required=True)
	email = fields.Char('Email')
	categoria = fields.Selection([('agricultura',('Agricultura')),
		('urbano', ('Urbano')),
		('educacion', ('Educación'))])
	idea = fields.Text('Exponer idea')

	


