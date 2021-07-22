from odoo import exceptions
import random
import string
import logging

_logger = logging.getLogger(__name__)

class GeneratePassword(object):
    def generate_password(self):
        letters = string.ascii_letters+string.digits
        password = ''.join(random.sample(letters,8))
        _logger.info("Ramdom Password: [%s]" % password)

        return password