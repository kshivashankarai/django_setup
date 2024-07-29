from api.authentication.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    ActiveSessionViewSet,
    LogoutViewSet,
)
from rest_framework import routers
from api.user.viewsets import UserViewSet
from api.main.viewsets.role import RoleViewSet
# from api.main.viewsets.user_role import UserRoleViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"edit", UserViewSet, basename="user-edit")

router.register(r"register", RegisterViewSet, basename="register")

router.register(r"login", LoginViewSet, basename="login")

router.register(r"checkSession", ActiveSessionViewSet, basename="check-session")

router.register(r"logout", LogoutViewSet, basename="logout")

router.register(r"role", RoleViewSet, basename="role")

# router.register(r"user_role", UserRoleViewSet, basename="user_role")

urlpatterns = [
    *router.urls,
]
