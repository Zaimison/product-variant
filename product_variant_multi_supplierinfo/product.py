# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2014  KMEE  - www.kmee.com.br - Daniel Sadamo Hirayama        #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU General Public License for more details.                                 #
#                                                                             #
#You should have received a copy of the GNU General Public License            #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

from openerp.osv import fields, orm


class product_product(orm.Model):
    _inherit = 'product.product'

    _columns = {

        'seller_ids': fields.one2many('product.supplierinfo',
                                      'product_id', 'Supplier'),
    }


class product_supplierinfo(orm.Model):
    _inherit = 'product.supplierinfo'

    _columns = {

        'product_id': fields.many2one('product.product',
                                      'Product',
                                      required=True,
                                      ondelete='cascade',
                                      select=True),
    }
