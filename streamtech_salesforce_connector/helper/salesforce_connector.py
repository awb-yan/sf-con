from odoo import models, fields, api, exceptions, _
from simple_salesforce import Salesforce
from openerp.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)

class SalesForceConnect(models.Model):
    def connect_to_salesforce(self):
        try:
            IrConfigParameter = self.env['ir.config_parameter'].sudo()
            username = IrConfigParameter.get_param('odoo_salesforce.sf_username')
            password = IrConfigParameter.get_param('odoo_salesforce.sf_password')
            security = IrConfigParameter.get_param('odoo_salesforce.sf_security_token')
            domain = IrConfigParameter.get_param('odoo_salesforce.sf_domain')

            _logger.info("Connect to salesforce")
            _logger.info("username: [%s]" % username)
            _logger.info("password: [%s]" % password)
            _logger.info("security: [%s]" % security)
            _logger.info("domain: [%s]" % domain)
            sales_force = Salesforce(username=username, password=password, security_token=security, domain=domain)
            _logger.info("SF: [%s]" % sales_force)

            return sales_force
        except Exception as e:
            Warning(_(str(e)))


