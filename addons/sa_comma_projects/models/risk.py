from odoo import api, fields, models, _

# GRC Risk model
#
class Risk(models.Model):
    _name = "grc.risk"
    _inherit="grc.risk"
    _description = "GRC Risk - project integration"

    project_ids = fields.Many2many('project.project', String="Projects")