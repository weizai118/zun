#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""add mem used to compute node

Revision ID: 648c25faa0be
Revises: 174cafda0857
Create Date: 2017-05-24 09:39:42.021441

"""

# revision identifiers, used by Alembic.
revision = '648c25faa0be'
down_revision = '174cafda0857'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('compute_node',
                  sa.Column('mem_used', sa.Integer(), nullable=False))
