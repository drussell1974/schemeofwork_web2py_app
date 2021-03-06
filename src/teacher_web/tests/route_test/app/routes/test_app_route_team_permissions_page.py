from django.urls import resolve, reverse
from django.test import TestCase
from app.teampermissions.views import index, edit, delete, request_access, approve, reject, TeamPermissionRequestLoginView

# Create your tests here.
class test_app_route_team_permissions_page(TestCase):

    def test_index_url_resolves_to_account_team_permissions(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/')
        self.assertEqual("team-permissions.index", url.url_name)
        self.assertEquals(url.func, index)


    def test_index_url_resolves_to_account_team_permissions__reverse(self):
        url = reverse("team-permissions.index", args=[127671276711, 67])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/", url)


    def test_edit_url_resolves_to_account__team_permissions_edit(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/edit')
        self.assertEqual("team-permissions.edit", url.url_name)
        self.assertEquals(url.func, edit)

    
    def test_edit_url_resolves_to_account_team_permissions_edit__reverse(self):
        url = reverse("team-permissions.edit", args=[127671276711, 67, 56,6069])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/edit", url)


    def test_delete_url_resolves_to_account__team_permissions_delete(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/delete')
        self.assertEqual("team-permissions.delete", url.url_name)
        self.assertEquals(url.func, delete)

    
    def test_delete_url_resolves_to_account_team_permissions_delete__reverse(self):
        url = reverse("team-permissions.delete", args=[127671276711, 67, 56, 6069])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/delete", url)


    def test_requestaccess_url_resolves_to_account__team_permissions_requestaccess(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/SCHEMEOFWORK.VIEWER/request-access')
        self.assertEqual("team-permissions.request-access", url.url_name)
        self.assertEquals(url.func, request_access)

    
    def test_requestaccess_url_resolves_to_account_team_permissions_requestaccess__reverse(self):
        url = reverse("team-permissions.request-access", args=[127671276711, 67, 56, "SCHEMEOFWORK.VIEWER"])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/SCHEMEOFWORK.VIEWER/request-access", url)


    def test_login_url_resolves_to_account__team_permissions_login(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/SCHEMEOFWORK.EDITOR/login')
        self.assertEqual("team-permissions.login-as", url.url_name)
        self.assertEquals(url.func.__name__, TeamPermissionRequestLoginView.__name__)

    
    def test_login_url_resolves_to_account_team_permissions_login__reverse(self):
        url = reverse("team-permissions.login-as", args=[127671276711, 67, 56, "SCHEMEOFWORK.EDITOR"])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/SCHEMEOFWORK.EDITOR/login", url)


    def test_edit_url_resolves_to_account__team_permissions_approve(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/approve')
        self.assertEqual("team-permissions.approve", url.url_name)
        self.assertEquals(url.func, approve)

    
    def test_edit_url_resolves_to_account_team_permissions_approve__reverse(self):
        url = reverse("team-permissions.approve", args=[127671276711, 67, 56, 6069])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/approve", url)


    def test_edit_url_resolves_to_account__team_permissions_reject(self):
        url = resolve('/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/reject')
        self.assertEqual("team-permissions.reject", url.url_name)
        self.assertEquals(url.func, reject)

    
    def test_edit_url_resolves_to_account_team_permissions_reject__reverse(self):
        url = reverse("team-permissions.reject", args=[127671276711, 67, 56, 6069])
        self.assertEqual("/accounts/team-permissions/institute/127671276711/department/67/schemeofwork/56/teacher/6069/reject", url)