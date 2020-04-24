# -*- coding: utf-8 -*-
#
# Swiss Open Access Repository
# Copyright (C) 2019 RERO
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

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from functools import partial

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import GenFunction, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields

from sonar.modules.serializers import schema_from_context
from sonar.modules.users.api import UserRecord

schema_from_user = partial(schema_from_context, schema=UserRecord.schema)


class UserMetadataSchemaV1(StrictKeysMixin):
    """Schema for the user metadata."""

    pid = PersistentIdentifier()
    user_id = fields.Integer()
    full_name = SanitizedUnicode(required=True)
    birth_date = fields.DateTime()
    email = SanitizedUnicode(required=True)
    street = SanitizedUnicode()
    postal_code = SanitizedUnicode()
    city = SanitizedUnicode()
    phone = SanitizedUnicode()
    organisation = fields.Dict(dump_only=True)
    roles = fields.List(SanitizedUnicode, required=True)
    # When loading, if $schema is not provided, it's retrieved by
    # Record.schema property.
    schema = GenFunction(load_only=True,
                         attribute="$schema",
                         data_key="$schema",
                         deserialize=schema_from_user)


class UserSchemaV1(StrictKeysMixin):
    """User schema."""

    metadata = fields.Nested(UserMetadataSchemaV1)
    created = fields.Str(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
