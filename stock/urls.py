from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.get_client_ip, name="home"),
    path('view_stock', views.view_stock, name="view_stock"),
    path('add_stock', views.add_stock, name="add_stock"),
    path('add_loc', views.add_loc, name="add_loc"),
    path('add_loc1', views.add_loc1, name="add_loc1"),
    path('add_loc2', views.add_loc2, name="add_loc2"),
    path('add_task', views.add_task, name="add_task"),
    path('task_view', views.task_view, name="task_view"),
    path('add-cat', views.add_cat, name="add_cat"),
    path('update_stock/<str:pk>/', views.update_stock, name="update_stock"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_stock/<str:pk>/', views.delete_stock, name="delete_stock"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_item/<str:pk>/', views.issue_item, name="issue_item"),
    path('receive_item/<str:pk>/', views.receive_item, name="receive_item"),
    path('re_order/<str:pk>/', views.re_order, name="re_order"),
    path('co_order/<str:pk>/', views.co_order, name="co_order"),
    path('register', views.new_register, name="register"),
    path('view_history', views.view_history, name="view_history"),
    path('dependent_forms', views.dependent_forms, name='dependent_forms'),
    path('dependent_update/<str:pk>/', views.dependent_forms_update, name='dependent_update'),
    path('depend_form_view', views.dependent_forms_view, name='depend_form_view'),
    path('depend_form_delete/<str:pk>', views.delete_dependant, name='delete_dependant'),
    path('ajax/load-states/', views.load_stats, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('scrumboard', views.scrum_list, name='scrumboard'),
    path('scrumboard_view', views.scrum_view, name='scrumboard_view'),
    path('contacts', views.contact, name='contacts'),
    # path('accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

