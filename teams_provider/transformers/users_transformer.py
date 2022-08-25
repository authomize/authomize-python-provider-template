from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    NewIdentityRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema, UserStatus,
)

from base_provider.transformers.base_transformer import BaseTransformer


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.

    """

    def validate_item_schema(self, raw_item: Dict) -> bool:
        return True

    def transform_model(self, raw_item: Dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user_id = raw_item['id']
        status = UserStatus.Enabled
        if raw_item['deletedDateTime'] is not None:
            status = UserStatus.Deleted
        elif raw_item['accountEnabled'] is False:
            status = UserStatus.Disabled
        elif raw_item['externalUserState'] == 'PendingAcceptance':
            status = UserStatus.Staged

        new_user = NewUserRequestSchema(
            id=user_id,
            name=f'{raw_item["givenName"]} {raw_item["surname"]}',
            email=raw_item['mail'],
            firstName=raw_item['givenName'],
            lastName=raw_item['surname'],
            status=status,
            isExternal=raw_item['externalUserState'] is not None,
        )
        new_identity = NewIdentityRequestSchema(
            id=user_id,
            name=f'{raw_item["givenName"]} {raw_item["surname"]}',
            email=raw_item['mail'],
            firstName=raw_item['givenName'],
            lastName=raw_item['surname'],
            status=status,
            country=raw_item['country'],
            department=raw_item['department'],
            title=raw_item['jobTitle'],
            hireDate=raw_item['employeeHireDate'],
            terminationDate=raw_item.get('employeeLeaveDateTime', None),
        )

        bundle.new_users.append(new_user)
        bundle.new_identities.append(new_identity)
        return bundle
