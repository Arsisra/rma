# -*- coding: utf-8 -*-
#########################################################################
#                                                                       #
#                                                                       #
#########################################################################
#                                                                       #
# Copyright (C) 2009-2011  Akretion, Emmanuel Samyn						#
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################

from osv import fields, osv

class product_supplierinfo(osv.osv):
    _inherit = "product.supplierinfo"

    def get_warranty_return_partner(self, cr, uid, context=None):
        if self.pool.get('ir.module.module').search(cr, uid, [('name','like','product_brand'),('state','like','installed')]):
            return [
                ('company','Company'),
                ('supplier','Supplier'),
                ('brand','Brand manufacturer'),
                ('other','Other'),]
        else:
            return [
                ('company','Company'),
                ('brand','Brand manufacturer'),
                ('other','Other'),]
            
    _columns = {
        "warranty_duration" : fields.float('Warranty', help="Warranty in month for this product/supplier relation. Only for company/supplier relation (purchase order) ; the customer/company relation (sale order) always use the product main warranty field"),
        "warranty_return_partner" :  fields.selection(get_warranty_return_partner, 'Warrantee return', size=128, help="Who is in charge of the warranty return treatment toward the end customer. Company will use the current compagny delivery or default address and so on for supplier and brand manufacturer. Doesn't necessarly mean that the warranty to be applied is the one of the return partner (ie: can be returned to the company and be under the brand warranty"),
        }
    _defaults = {
        'warranty_return_partner': lambda *a: 'company',
    }
    
product_supplierinfo()   

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: