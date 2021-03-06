# -*- coding: utf-8 -*-
#
# Swiss Open Access Repository
# Copyright (C) 2021 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Projects resource."""

from flask_resources.serializers import JSONSerializer
from invenio_records_resources.resources import \
    RecordResourceConfig as BaseRecordResourceConfig
from invenio_records_resources.resources.records.response import RecordResponse

from sonar.resources.projects.serializers.csv import CSVSerializer
from sonar.resources.resource import RecordResource as BaseRecordResource
from sonar.resources.resources.responses import StreamResponse


class RecordResourceConfig(BaseRecordResourceConfig):
    """Projects resource configuration."""

    resource_name = 'projects'
    list_route = '/projects/'
    item_route = f'{list_route}/<pid_value>'

    response_handlers = {
        'application/json':
        RecordResponse(JSONSerializer()),
        'text/csv':
        StreamResponse(CSVSerializer(csv_included_fields=[
            'pid', 'name', 'description', 'startDate', 'endDate'
        ]),
                       filename='projects.csv')
    }


class RecordResource(BaseRecordResource):
    """Projects resource"."""

    default_config = RecordResourceConfig
