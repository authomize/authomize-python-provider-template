from authomize.rest_api_client.generated.schemas import NewPrivilegeRequestSchema, PrivilegeType

USE_APP_PRIVILEGE = NewPrivilegeRequestSchema(
    uniqueId="Access-Application",
    type=PrivilegeType.Use,
    originPrivilegeName="Access Applcation",
)

ROLE_ADMIN_PRIVILEGE = NewPrivilegeRequestSchema(
    uniqueId="Role-Admin",
    type=PrivilegeType.Administrative,
    originPrivilegeName="Role Admin",
)
