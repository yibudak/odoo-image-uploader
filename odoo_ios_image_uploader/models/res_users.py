# Copyright 2023 Yiğit Budak (https://github.com/yibudak)
# Copyright 2023 krokan (https://github.com/krokan-us)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = "res.users"

    def get_user_image_endpoint(self):
        """
        API endpoint for getting image of user
        :param vals: {product_barcode: barcode}
        :return: json response
        """
        # Start with a dictionary with an error status
        response = {"status": "error"}
        if self:
            response["status"] = "success"
            response["message"] = _("User found")
            response["user_id"] = self.id
            response["user_name"] = self.name
            response["image_data"] = self.image.decode("utf-8").replace("\n", "")
        return response
