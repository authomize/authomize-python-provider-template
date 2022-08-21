"""Methods related to transforming raw data into connectors-rest-api identities entity"""
from datetime import datetime

from authomize.rest_api_client.generated.schemas import (
    NewIdentityRequestSchema,
    RequestsBundleSchema,
    UserStatus,
)

from bamboohr_provider.constants import USER_ID_FORMAT
from bamboohr_provider.models.users import BambooHRUserModel
from base_provider.transformers.base_transformer import BaseTransformer


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.
    """

    def validate_item_schema(self, raw_item: dict) -> bool:
        return True

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user = BambooHRUserModel(**raw_item)
        user_id = USER_ID_FORMAT.format(id=user.id)
        manager_id = USER_ID_FORMAT.format(id=user.supervisorId) if user.supervisorId else None
        hire_date = (
            datetime.strptime(user.hireDate, '%Y-%m-%d')
            if user.hireDate and user.hireDate != '0000-00-00'
            else None
        )
        termination_date = (
            datetime.strptime(user.terminationDate, '%Y-%m-%d')
            if user.terminationDate and user.terminationDate != '0000-00-00'
            else None
        )
        if user.status == "Active":
            status = UserStatus.Enabled
        elif user.status == "Inactive":
            status = UserStatus.Disabled
        else:
            raise ValueError("User status")

        identity = NewIdentityRequestSchema(
            uniqueId=user_id,
            name=user.fullName5,
            **(dict(email=user.bestEmail) if user.bestEmail else dict()),
            employeeNumber=user.employeeNumber,
            country=user.country,
            city=user.city,
            department=user.department,
            division=user.division,
            managerId=manager_id,
            hireAt=hire_date,
            terminationAt=termination_date,
            title=user.jobTitle,
            firstName=user.firstName,
            lastName=user.lastName,
            status=status,
        )

        bundle.new_identities.append(identity)
        return bundle
