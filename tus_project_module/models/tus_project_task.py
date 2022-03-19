# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def search_read(self, args=None, fields=None, offset=0, limit=None, order=None):
        if args is None:
            args = []
        if self.env.user.has_group('project.group_project_user') and not self.env.user.has_group('tus_project_module.group_project_project_manager') and not self.env.user.has_group('project.group_project_manager') :
            args += [('user_ids', 'in', self.env.user.id)]
        return super(ProjectTask, self).search_read(args, fields, offset, limit, order)