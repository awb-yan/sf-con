from datetime import datetime
from odoo import http, fields, models

class AWBOdooAPI(models.Model):
  _inherit = 'sale_subscription'

  is_active = fields.Boolean(string="Is Subscription Active")
