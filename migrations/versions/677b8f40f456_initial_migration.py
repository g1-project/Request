"""Initial migration.

Revision ID: 677b8f40f456
Revises: 
Create Date: 2021-03-12 14:07:26.118453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "677b8f40f456"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("request")
    op.drop_table("product_category")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "product_category",
        sa.Column(
            "productcategoryid",
            sa.SMALLINT(),
            server_default=sa.text(
                "nextval('product_category_productcategoryid_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("productcategoryid", name="product_category_pk"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "request",
        sa.Column("requestid", postgresql.UUID(), autoincrement=False, nullable=False),
        sa.Column("productname", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("startdate", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("enddate", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("requester", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("lender", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "productcategoryid",
            sa.SMALLINT(),
            server_default=sa.text(
                "nextval('request_productcategoryid_seq'::regclass)"
            ),
            autoincrement=True,
            nullable=False,
        ),
        sa.CheckConstraint(
            "lender ~* '^[\\w\\-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$'::text",
            name="valid_lender_email",
        ),
        sa.CheckConstraint(
            "requester ~* '^[\\w\\-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$'::text",
            name="valid_requester_email",
        ),
        sa.CheckConstraint("requester <> lender", name="valid_lender_user"),
        sa.ForeignKeyConstraint(
            ["productcategoryid"],
            ["product_category.productcategoryid"],
            name="request_product_category_fk",
            onupdate="RESTRICT",
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("requestid", name="request_pk"),
    )
    # ### end Alembic commands ###
