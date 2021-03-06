from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_resources__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permissions on resource
            
        #path('', views.index, name="resource.index"),
        #path('delete_unpublished', views.delete_unpublished, name="resource.delete_unpublished"), 
        #path('new', views.new, name="resource.new"),
        #path('<int:resource_id>/edit', views.edit, name="resource.edit"),
        #path('<int:resource_id>/delete', views.delete_item, name="resource.delete_item"), 
        #path('<int:resource_id>/publish_item', views.publish_item, name="resource.publish_item"), 
        #path('<int:resource_id>/save', views.save, name="resource.save")
        
        """

        testcases = [           
            {
                "route":"resource.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
            {
                "route":"resource.index as lesson-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
            {
                "route":"resource.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"resource.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"resource.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/99999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"resource.delete as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/99999999/delete",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"resource.publish_item as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/99999999/publish_item",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"resource.save as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/resources/99999999/save",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"resource.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/{self.test_reference}/edit",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Edit: OCR AS and A Level Computer Science",
            },
            {
                "route":"resource.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/delete_unpublished",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"resource.publish_item as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/{self.test_reference}/publish_item",
                "enter_username": "schemeofwork-owner@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
        ]
        
        self.run_testcases__permission(testcases, "resource")