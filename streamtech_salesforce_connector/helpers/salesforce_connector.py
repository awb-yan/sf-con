from odoo import models, fields, api, exceptions, _
from simple_salesforce import Salesforce
from openerp.exceptions import Warning

class SalesForceConnect(object):
    def connect_salesforce(self, model):
        IrConfigParameter = model.env['ir.config_parameter'].sudo()

        _logger.info("Connect to salesforce")
        _logger.info("username: [%s]" % username)
        _logger.info("password: [%s]" % password)
        _logger.info("security: [%s]" % security)
        _logger.info("domain: [%s]" % domain)
        sales_force = Salesforce(username=username, password=password, security_token=security, domain=domain)

        return sales_force


