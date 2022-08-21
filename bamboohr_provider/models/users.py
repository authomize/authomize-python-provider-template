"""Model BambooHR user"""
from pydantic import BaseModel

# TODO - autogen itfrom model
USER_MODEL_FIELDS = [
    "id",
    "bestEmail",
    "createdByUserId",
    "supervisorId",
    "supervisorEId",
    "lastChanged",
    "firstName",
    "lastName",
    "fullName5",
    "department",
    "jobTitle",
    "hireDate",
    "city",
    "country",
    "division",
    "employeeNumber",
    "terminationDate",
    "status",
]


class BambooHRUserModel(BaseModel):
    """Model for BambooHR users

    Fields: https://documentation.bamboohr.com/docs/list-of-field-names
    """

    id: str
    bestEmail: str = None
    createdByUserId: str = None
    supervisorId: str = None
    supervisorEId: str = None
    lastChanged: str = None
    firstName: str = None
    lastName: str = None
    fullName5: str = None
    department: str = None
    jobTitle: str = None
    hireDate: str = None
    city: str = None
    country: str = None
    division: str = None
    employeeNumber: str = None
    terminationDate: str = None
    status: str = None
