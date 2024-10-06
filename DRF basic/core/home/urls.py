
from django.urls import path

from .views import *

urlpatterns = [
   path("", home),
   path("student", post_student),
   path("update-student/<id>/", update_student),
   path("patchupdate-student/<id>/", patchupdate_student),
   path("delete-student/<id>/",delete_student),
   
   path("get-book/", get_book),

   path("stu/", StudentAPI.as_view()) #API view, all the method work with just this url


]