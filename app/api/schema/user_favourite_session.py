from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship

from app.api.helpers.utilities import dasherize
from app.api.schema.base import SoftDeletionSchema


class UserFavouriteSessionSchema(SoftDeletionSchema):
    """
    Api schema for User Favourite Session Model
    """

    class Meta:
        type_ = 'user-favourite-session'
        self_view = 'v1.user_favourite_session_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)

    session = Relationship(
        attribute='session',
        self_view='v1.user_favourite_session_session',
        self_view_kwargs={'id': '<id>'},
        related_view='v1.session_list',
        related_view_kwargs={'user_favourite_session_id': '<id>'},
        schema='SessionSchema',
        type_='session',
    )

    user = Relationship(
        attribute='user',
        self_view='v1.user_favourite_session_user',
        self_view_kwargs={'id': '<id>'},
        related_view='v1.user_detail',
        related_view_kwargs={'user_favourite_session_id': '<id>'},
        schema='UserSchema',
        type_='user',
    )
