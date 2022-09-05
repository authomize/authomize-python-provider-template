from typing import List, Tuple

from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema,
    UserStatus,
)
from onelogin.api.models.otp_device import OTP_Device
from onelogin.api.models.user import User

from base_provider.transformers.base_transformer import BaseTransformer


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.

    See https://developers.onelogin.com/api-docs/1/users/get-users Get Users documentation
        https://developers.onelogin.com/api-docs/2/users/list-users
    """

    def validate_item_schema(self, raw_item: Tuple[User, List[OTP_Device]]) -> bool:
        return True

    def transform_model(self, raw_item: Tuple[User, List[OTP_Device]]) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user_raw, enrolled_factors_raw = raw_item
        user_id = user_raw.id
        new_user = NewUserRequestSchema(
            uniqueId=user_id,
            name=f'{user_raw.firstname} {user_raw.lastname}',
            firstName=user_raw.firstname,
            lastName=user_raw.lastname,
            **(dict(email=user_raw.email) if user_raw.email else dict()),
            isExternal=False,
            lastLoginAt=user_raw.last_login,
            lastPasswordChangedAt=user_raw.password_changed_at,
            status=self._get_user_status(user_raw.status),
            hasMFA=self._get_has_mfa(enrolled_factors_raw),
        )
        # Every user can be member of 0/1 group (but not many groups!)
        if user_raw.group_id:
            association = NewAccountsAssociationRequestSchema(
                sourceId=user_id,
                targetId=user_raw.group_id,
            )
            bundle.new_accounts_association.append(association)
        bundle.new_users.append(new_user)
        return bundle

    def _get_user_status(self, onelogin_status: int) -> UserStatus:
        if onelogin_status == User.STATUS_UNACTIVATED:
            return UserStatus.Staged
        if onelogin_status == User.STATUS_ACTIVE:
            return UserStatus.Enabled
        if onelogin_status == User.STATUS_SUSPENDED:
            return UserStatus.Suspended
        if onelogin_status == User.STATUS_LOCKED:
            return UserStatus.Suspended
        if onelogin_status == User.STATUS_PASSWORD_EXPIRED:
            return UserStatus.Enabled
        if onelogin_status == User.STATUS_AWAITING_PASSWORD_RESET:
            return UserStatus.Enabled
        self.logger.error("Unknown user status", status=onelogin_status)
        return UserStatus.Unknown

    def _get_has_mfa(self, enrolled_factors_raw: List[OTP_Device]) -> bool:
        return (len(enrolled_factors_raw) > 0)
