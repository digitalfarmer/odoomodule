# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class academy(models.Model):
#     _name = 'academy.academy'
class Teachers(models.Model):
    _name = 'academy.teachers'
    _inherit = 'mail.thread'

    name = fields.Char()
    biography = fields.Html()

    courses_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")
    #course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'academy.courses'
    _inherit = 'mail.thread'
    #_inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string='Teacher')
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100