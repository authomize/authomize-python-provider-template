from authomize.rest_api_client.generated import schemas
from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema, RequestsBundleSchema, \
    NewGroupingsAssociationRequestSchema

from base_provider.transformers.base_transformer import BaseTransformer
from jumpcloud_provider.models.application_associations import ApplicationAssociations


class ApplicationsTransformer(BaseTransformer):
    """
    Transform a list of all Apps in a JumpCloud account.

    See https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/applications_api.py
        https://docs.jumpcloud.com/api/1.0/index.html#operation/applications_list
    """

    def validate_item_schema(self, raw_item: ApplicationAssociations) -> bool:
        return True

    def transform_model(self, raw_item: ApplicationAssociations) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetsRequestSchema(
            id=raw_item.id,
            name=raw_item.name,
        )
        bundle.new_assets.append(asset)

        for user_association in raw_item.user_associations:
            user_association_request = schemas.NewAccountsAssociationRequestSchema(
                sourceId=raw_item.id,
                targetId=user_association.user_id
            )
            bundle.new_accounts_association.append(user_association_request)

        for user_group_association in raw_item.user_group_associations:
            user_group_association_request = NewGroupingsAssociationRequestSchema(
                sourceId=raw_item.id,
                targetId=user_group_association.group_id
            )
            bundle.new_groupings_association.append(user_group_association_request)

        return bundle
