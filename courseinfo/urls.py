from django.urls import path

from courseinfo.views import (
    InstructorList,
    SectionList,
    CourseList,
    SemesterList,
    StudentList,
    RegistrationList,
    InstructorDetail,
    SectionDetail,
    SemesterDetail,
    InstructorCreate,
    SectionCreate,
    InstructorUpdate,
    SectionUpdate,
    RegistrationDelete,
)

urlpatterns = [
    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_detail_urlpattern'),

    path('instructor/create/',
         InstructorCreate.as_view(),
         name='courseinfo_instructor_create_urlpattern'),

    path('instructor/<int:pk>/update/',
         InstructorUpdate.as_view(),
         name='courseinfo_instructor_update_urlpattern'),

    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),

    path('section/<int:pk>/update/',
         SectionUpdate.as_view(),
         name='courseinfo_section_update_urlpattern'),

path('section/create/',
         SectionCreate.as_view(),
         name='courseinfo_section_create_urlpattern'),

    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('semester/<int:pk/',
         SemesterDetail.as_view(),
         name='courseinfo_semeste_detail_urlpattern'),

    path('student/',
         StudentList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('registration/<int:pk>/delete/',
         RegistrationDelete.as_view(),
         name='courseinfo_registration_delete_urlpattern'),

]
