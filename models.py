from openerp import api, models, exceptions, fields,  _
import openerp.addons.decimal_precision as dp
from openerp.osv import osv
import logging
import datetime

_logger = logging.getLogger(__name__)


class multi_package_shipment_wizard(models.TransientModel):
        _inherit= 'multi.package.shipment.wizard'

        def default_get(self,cr,uid,fields,context):
                res = super(multi_package_shipment_wizard,self).default_get(cr,uid,fields,context)
                picking_ids=self.pool['stock.picking'].browse(cr,uid,context['active_ids'])
		dhl_declared_value = 0
		for picking_id in picking_ids:
			if picking_id.dhl_declared_value > 0:
				dhl_declared_value = dhl_declared_value + picking_id.dhl_declared_value
		if dhl_declared_value > 0:
			res['declared_value'] = dhl_declared_value
		return res
