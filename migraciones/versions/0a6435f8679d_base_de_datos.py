"""BASE DE DATOS

Revision ID: 0a6435f8679d
Revises: a586e02bbbde
Create Date: 2025-05-26 11:13:04.515989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0a6435f8679d'
down_revision: Union[str, None] = 'a586e02bbbde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipoAsesoria',
    sa.Column('idTipoAsesoria', sa.Integer(), nullable=False),
    sa.Column('nombreTipoAsesoria', sa.String(length=50), nullable=True),
    sa.Column('descripcionTipoAsesoria', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('idTipoAsesoria')
    )
    op.create_table('galeriaVehiculoModificado',
    sa.Column('idGaleriaVehiculoModificado', sa.Integer(), nullable=False),
    sa.Column('nombreVehiculoGaleriaVehiculoModificado', sa.String(length=100), nullable=True),
    sa.Column('descripcionGaleriaVehiculoModificado', sa.String(length=100), nullable=True),
    sa.Column('usuarioIdGaleriaVehiculoModificado', sa.Integer(), nullable=True),
    sa.Column('vehiculoIdGaleriaVehiculoModificado', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuarioIdGaleriaVehiculoModificado'], ['usuario.idUsuario'], ),
    sa.ForeignKeyConstraint(['vehiculoIdGaleriaVehiculoModificado'], ['vehiculo.idVehiculo'], ),
    sa.PrimaryKeyConstraint('idGaleriaVehiculoModificado')
    )
    op.create_table('historialAsesoria',
    sa.Column('idHistorialAsesoria', sa.Integer(), nullable=False),
    sa.Column('comentariosHistorialAsesoria', sa.String(length=500), nullable=True),
    sa.Column('fechaRegistroHistorialAsesoria', sa.Date(), nullable=True),
    sa.Column('asesoriaIdHistorialAsesoria', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asesoriaIdHistorialAsesoria'], ['asesoria.idAsesoria'], ),
    sa.PrimaryKeyConstraint('idHistorialAsesoria')
    )
    op.drop_table('tipoasesoria')
    op.drop_table('historialasesoria')
    op.drop_table('galeriavehiculomodificado')
    op.drop_constraint('asesoria_ibfk_2', 'asesoria', type_='foreignkey')
    op.create_foreign_key(None, 'asesoria', 'tipoAsesoria', ['tipoAsesoriaIdAsesoria'], ['idTipoAsesoria'])
    op.add_column('diagnosticos', sa.Column('diagnosticomecanico', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'diagnosticos', 'mecanico', ['diagnosticomecanico'], ['idMecanico'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'diagnosticos', type_='foreignkey')
    op.drop_column('diagnosticos', 'diagnosticomecanico')
    op.drop_constraint(None, 'asesoria', type_='foreignkey')
    op.create_foreign_key('asesoria_ibfk_2', 'asesoria', 'tipoasesoria', ['tipoAsesoriaIdAsesoria'], ['idTipoAsesoria'])
    op.create_table('galeriavehiculomodificado',
    sa.Column('idGaleriaVehiculoModificado', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombreVehiculoGaleriaVehiculoModificado', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('descripcionGaleriaVehiculoModificado', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('usuarioIdGaleriaVehiculoModificado', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('vehiculoIdGaleriaVehiculoModificado', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['usuarioIdGaleriaVehiculoModificado'], ['usuario.idUsuario'], name='galeriavehiculomodificado_ibfk_1'),
    sa.ForeignKeyConstraint(['vehiculoIdGaleriaVehiculoModificado'], ['vehiculo.idVehiculo'], name='galeriavehiculomodificado_ibfk_2'),
    sa.PrimaryKeyConstraint('idGaleriaVehiculoModificado'),
    mysql_collate='utf8mb4_uca1400_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('historialasesoria',
    sa.Column('idHistorialAsesoria', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('comentariosHistorialAsesoria', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('fechaRegistroHistorialAsesoria', sa.DATE(), nullable=True),
    sa.Column('asesoriaIdHistorialAsesoria', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['asesoriaIdHistorialAsesoria'], ['asesoria.idAsesoria'], name='historialasesoria_ibfk_1'),
    sa.PrimaryKeyConstraint('idHistorialAsesoria'),
    mysql_collate='utf8mb4_uca1400_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tipoasesoria',
    sa.Column('idTipoAsesoria', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombreTipoAsesoria', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('descripcionTipoAsesoria', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('idTipoAsesoria'),
    mysql_collate='utf8mb4_uca1400_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('historialAsesoria')
    op.drop_table('galeriaVehiculoModificado')
    op.drop_table('tipoAsesoria')
    # ### end Alembic commands ###
