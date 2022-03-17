# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    email_id = fields.Char(string="Email Id")
    website = fields.Char(string="Website")

    @api.model
    def search_read(self, args=None, fields=None, offset=0, limit=None, order=None):
        if args is None:
            args = []
        if self.env.user.has_group('tus_project_module.group_project_project_manager') and not self.env.user.has_group('project.group_project_manager'):
            args += [('user_id', '=', self.env.user.id)]
        return super(Project, self).search_read(args, fields, offset, limit, order)

