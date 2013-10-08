# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time

class designer_paper(osv.osv):
    """ 竟稿申请"""
    _name = 'designer.paper'
    _columns = {
        'project_id': fields.many2one('designer.project', string='项目简报', readonly=True, states={'draft': [('readonly', False)]}),
        'paper_no': fields.char('编号', size=64, required=True),
        'reason': fields.text('原因', help='原因'),
        'comment': fields.text('意见', help='意见'),
        'state': fields.selection([('draft', '草稿中'),
            ('open', '已批准'),
            ('cancel', '已拒绝'),
            ('close', '已完成')],
            '状态', readonly=True, track_visibility='onchange',
        ),
    }
    _sql_constraints = [
        ('paper_no', 'unique(paper_no)', 'The name of the idea must be unique')
    ]

    _order = 'paper_no asc'

    _defaults = {
        'state': lambda *a: 'draft',
    }

    def designer_project_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_project_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def designer_project_close(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)

    def designer_project_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)