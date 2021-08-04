from datetime import datetime
from odoo import http, fields, models
from odoo.http import request
from .authentication import OdooAPI

import importlib
import json

Serializer = importlib.import_module(
    "odoo.addons.odoo-rest-api"
).controllers.serializers.Serializer

class OdooAPI(OdooAPI):
    _inherit = 'sale.subscription'

    is_active = fields.Datetime(string="Is Subscription Active", default=False)

    @http.route('/awb/active_users/', type='json', auth='user', methods=["PUT"], csrf=False)
    # data = {"params": {"user_ids": [<id1>, <id2>, <id3>], "subs_status": "expired/exceed_usage"}}
    def _active_users(self, user_ids=None):
        if not user_ids:
            res = {
              "errors": [
                {
                  "status": 400,
                  "message": "Bad Request",
                  "code": 352,
                  "description": "required parameters: <user_ids>, <subs_status: expired/ exceed_usage>",
                  "links": {
                    "about": "http://www.domain.com/rest/errorcode/352"
                  },
                  "data": {},
                  "data_count": {},
                }
              ]
            }

            return json.dumps(res)

        records = request.env['sale.subscription'].search([('code', 'in', user_ids)])

        print(records, flush=True)
        for record in records:
            record.write(
                {
                  "is_active": True
                }
            )
        records.env.cr.commit()

        # method for disconnecting users
        # return must be the processed records
        # if 2 out of 3 successful records
        # records must be set to 2 only
        # records = records.set_users_discon()

        serializer = Serializer(records, "{id, name, partner_id}", many=True)
        data = serializer.data
        res = {
            "success": [{
                "status": 200,
                "message": "User found!",
                "code": 200,
                "description": "",
                "links": {
                  "about": "",
                },
                "data": records,
                "data_count": len(records),
            }]
        }

        return res
