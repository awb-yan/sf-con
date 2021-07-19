from odoo import models, fields, api, exceptions, _
from simple_salesforce import Salesforce
from openerp.exceptions import Warning

_logger = logging.getLogger(__name__)

class SalesForceConnect(object):
    def connect_salesforce(self, model):
        IrConfigParameter = model.env['ir.config_parameter'].sudo()
        username = IrConfigParameter.get_param('odoo_salesforce.sf_username')
        password = IrConfigParameter.get_param('odoo_salesforce.sf_password')
        security = IrConfigParameter.get_param('odoo_salesforce.sf_security_token')
        domain = IrConfigParameter.get_param('odoo_salesforce.sf_domain')

        sales_force = Salesforce(username=username, password=password, security_token=security, domain=domain)

        return sales_force


