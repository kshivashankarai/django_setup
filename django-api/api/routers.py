from api.authentication.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    ActiveSessionViewSet,
    LogoutViewSet,
)
from rest_framework import routers
from api.user.viewsets import UserViewSet
from api.main.viewsets.role import RoleViewSet
from api.main.viewsets.user_role import UserRoleViewSet
from api.main.viewsets.module import ModuleViewSet
from api.main.viewsets.module_field import ModuleFieldViewSet
from api.main.viewsets.gender import GenderViewSet
from api.main.viewsets.employee import EmployeeViewSet
from api.main.viewsets.content import ContentViewSet
from api.main.viewsets.permission import PermissionViewSet
from api.main.viewsets.role_permission import RolePermissionViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"edit", UserViewSet, basename="user-edit")

router.register(r"register", RegisterViewSet, basename="register")

router.register(r"login", LoginViewSet, basename="login")

router.register(r"checkSession", ActiveSessionViewSet, basename="check-session")

router.register(r"logout", LogoutViewSet, basename="logout")

router.register(r"role", RoleViewSet, basename="role")

router.register(r"user_role", UserRoleViewSet, basename="user_role")

router.register(r"module", ModuleViewSet, basename="module")

router.register(r"module_field", ModuleFieldViewSet, basename="module-field")

router.register(r"gender", GenderViewSet, basename="gender")

router.register(r"employee", EmployeeViewSet, basename="employee")

router.register(r"content", ContentViewSet, basename="content")

router.register(r"permission", PermissionViewSet, basename="permission")

router.register(r"role_permission", RolePermissionViewSet, basename="role-permission")

urlpatterns = [
    *router.urls,
]
