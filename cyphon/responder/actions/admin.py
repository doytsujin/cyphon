# -*- coding: utf-8 -*-
# Copyright 2017-2018 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines a |ModelAdmin| subclass for |Actions| and registers it with
the `Django admin site`_.
"""

# third party
from django.contrib import admin

# local
from .models import Action, AutoAction


class ActionAdmin(admin.ModelAdmin):
    """
    Customizes admin pages for Actions.
    """
    fields = [
        'title',
        'description',
        'platform',
        'api_module',
        'api_class',
        'visa_required',
    ]


class AutoActionAdmin(admin.ModelAdmin):
    """
    Customizes admin pages for AutoActions.
    """
    fields = [
        'action',
        'sieve',
        'enabled',
    ]

admin.site.register(Action, ActionAdmin)
admin.site.register(AutoAction, AutoActionAdmin)
