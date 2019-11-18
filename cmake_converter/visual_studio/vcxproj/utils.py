#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2019:
#   Matthieu Estrada, ttamalfor@gmail.com
#   Pavel Liavonau, liavonlida@gmail.com
#
# This file is part of (CMakeConverter).
#
# (CMakeConverter) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# (CMakeConverter) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with (CMakeConverter).  If not, see <http://www.gnu.org/licenses/>.

from cmake_converter.utils import Utils


class VCXUtils(Utils):

    def lists_of_settings_to_merge(self):
        lists = super(VCXUtils, self).lists_of_settings_to_merge()
        lists.extend(
            [
                'cl_flags',
                'ln_flags'
            ]
        )
        return lists

    def init_context_current_setting(self, context):
        """
        Define settings of converter.

        :param context: converter context
        :type context: Context
        """

        super(VCXUtils, self).init_context_current_setting(context)
        for l in self.lists_of_settings_to_merge():
            context.settings[context.current_setting][l] = []
        context.settings[context.current_setting]['inc_dirs_list'] = []
        context.settings[context.current_setting]['PrecompiledHeader'] = []
        context.settings[context.current_setting]['property_sheets'] = []
