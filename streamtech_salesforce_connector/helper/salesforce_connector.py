from odoo import models, fields, api, exceptions, _
from simple_salesforce import Salesforce
from openerp.exceptions import Warning

class SalesForceConnect(models.Model):
    def connect_to_salesforce(self):
        try:
            IrConfigParameter = self.env['ir.config_parameter'].sudo()
            username = IrConfigParameter.get_param('odoo_salesforce.sf_username')
            password = IrConfigParameter.get_param('odoo_salesforce.sf_password')
            security = IrConfigParameter.get_param('odoo_salesforce.sf_security_token')
            domain = IrConfigParameter.get_param('odoo_salesforce.sf_domain')
            self.sales_force = Salesforce(username=username, password=password, security_token=security, domain=domain)
        except Exception as e:
            Warning(_(str(e)))


