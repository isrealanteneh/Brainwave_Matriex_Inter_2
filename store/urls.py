from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_link_view,name='home_link_view'),
    path("viewusers/",views.view_user, name="view_user"),
    path("manage/<int:pk>/", views.manage_user, name='manage_user'),
    path("saveuserchange/<int:pk>/",views.save_change_user, name="save_change_user"),
    # orders    
    path('manageorder/', views.manage_order, name="manage_order"),
    path("makeorders/",views.make_order_view ,name="make_order_view"),
    path("savedorders/<int:pk>/",views.saved_orders, name="saved_orders"),
    path("orders/<int:pk>/", views.make_order, name='make_order'),
    path("vieworders/", views.view_saved_order, name="view_saved_order"),
    # sales
    path("sale/",views.view_sales, name="view_sales"),
    # auth
    path("signup/", views.signup_view, name="signup_view"),
    path("login/", views.login_user, name='login_user'),
    path("logout/", views.logout_view, name="logout_view"),
    
    # cruds in products
    path("add/", views.create_inventory, name="create_inventory"),
    path("view/", views.view_inventory, name="view_inventory"),
    path("update/<int:pk>/", views.update_inventory, name="update_inventory"), 
    path("save/<int:pk>/", views.save_changes, name="save_changes"),
    path("delete/<int:pk>/", views.delete_inventory, name="delete_inventory"),
    # report 
    path("report/",views.generate_report, name="generate_report"),

]
