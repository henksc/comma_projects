from odoo import api, fields, models, _


# GRC Project model
#
class Task(models.Model):
    _name = "project.task"
    _inherit="project.task"
    _description = "GRC Project Task"
#    type = fields.Char("review")
    #default_asset_id = context.get('default_asset_id')
    asset_id = fields.Many2one("grc.asset", String = "Asset" )
    control_id = fields.Many2one("grc.control", String='Control')
    risk_id = fields.Many2one('grc.risk', string='Risk')
    policy_id=fields.Many2one('grc.policy',string='Policy')

# GRC Project model
#
class Project(models.Model):
    _name = "project.project"
    _inherit="project.project"
    _description = "GRC Project"

    risk_ids = fields.Many2many("grc.risk", String = "Risks", )