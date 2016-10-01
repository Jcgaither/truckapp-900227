from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('trucks.PlusTruck', AuthorPermissionLogic()),
    ('trucks.PlusTruck', CollaboratorsPermissionLogic()),
    ('trucks.Feedback', AuthorPermissionLogic()),
    ('trucks.Feedback', CollaboratorsPermissionLogic()),

)
