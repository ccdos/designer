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

class designer_idea(osv.osv):
    """ 创意简报"""
    _name = 'designer.idea'
    _inherit = ['mail.thread']
    _columns = {
        #'create_uid': fields.many2one('res.users','撰写人', required=True, readonly=True,states={'draft': [('readonly', False)]}),
        'name': fields.char('创意简报', size=64, required=True, readonly=True, states={'draft': [('readonly', False)]}),
        'brand_id': fields.many2one('designer.brand', '品牌', readonly=True, states={'draft': [('readonly', False)]}, required=True, change_default=True, select=True, track_visibility='always'),
        'partner_id': fields.many2one('res.partner', '客户', readonly=True, states={'draft': [('readonly', False)]}, required=True, change_default=True, select=True, track_visibility='always'),
        #'product_id': fields.many2one('product.product', '产品', readonly=True, required=True, change_default=True, select=True,states={'draft': [('readonly', False)]}),
        'date':fields.datetime('日期',required=True),
        'brand_definition': fields.text('品牌定义', help='品牌定义', readonly=True, states={'draft': [('readonly', False)]}),
        'marketing_problem_definition': fields.text('行销问题', help='行销问题', readonly=True, states={'draft': [('readonly', False)]}),
        'role_and_aim_of_advertising': fields.text('广告的角色和意图', help='广告的角色和意图', readonly=True, states={'draft': [('readonly', False)]}),
        'competition_scope': fields.text('竞争范畴', help='竞争范畴', readonly=True, states={'draft': [('readonly', False)]}),
        'target_segment_and_its_current_situation': fields.text('目标对象及其现状', help='目标对象及其现状', readonly=True, states={'draft': [('readonly', False)]}),
        'impact_of_advertising_you_want': fields.text('期望广告对消费者有何影响', help='期望广告对消费者有何影响', readonly=True, states={'draft': [('readonly', False)]}),
        'adverting_information_and_brand_proposition': fields.text('广告信息或品牌主张', help='广告信息或品牌主张', readonly=True, states={'draft': [('readonly', False)]}),
        'critical_support': fields.text('重要支持', help='重要支持', readonly=True, states={'draft': [('readonly', False)]}),
        'necessary_information': fields.text('必要事项', help='必要事项', readonly=True, states={'draft': [('readonly', False)]}),
        'advertising_tone': fields.text('广告格调', help='广告格调', readonly=True, states={'draft': [('readonly', False)]}),
        'background_information_concerned': fields.text('相关背景资料', help='相关背景资料', readonly=True, states={'draft': [('readonly', False)]}),
        #'receiver_uid':fields.many2one('res.users','我方对接人', required=True, readonly=True ,states={'draft': [('readonly', False)]}),
        'project_ids': fields.many2one('project.project', string='项目', readonly=True, states={'draft': [('readonly', False)]}),
        'state': fields.selection([('draft', '草稿中'),
            ('open', '已批准'),
            ('cancel', '已拒绝'),
            ('close', '已完成')],
            '状态', readonly=True, track_visibility='onchange',
        )
    }
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the idea must be unique')
    ]
    _defaults = {
        'state': lambda *a: 'draft',
    }
    _order = 'name asc'

    def designer_idea_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_idea_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def designer_idea_close(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)

    def designer_idea_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)
