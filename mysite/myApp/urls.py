from django.urls import path
from . import views

urlpatterns = [
    # path('due_dates/', views.get_assignment_due_dates, name='due_dates'),
    # path('students/', views.get_students_details, name='students'),
    # path('list_quizzes/', views.get_quizzes_with_multiple_attempts, name='get_quizzes_with_multiple_attempts'),
    # path('list_assignments/', views.list_assignments_with_grades, name='list_assignments_with_grades'),
    # path('list_assignment_submissions/', views.list_assignment_submissions, name='list_assignment_submissions'),
    # path('list_group_assignments/', views.list_group_assignments, name='list_group_assignments'),
    # path('reminders/', views.assignment_reminder, name='assignment_reminder'),
    # path('inboxReminders/', views.send_messages_to_missing_assignments, name='send_messages_to_missing_assignments'),
    # path('send_reminders/', views.send_due_date_reminders, name='send_due_date_reminders'),
    # path('message', views.send_welcome_message_to_all_students, name='send_welcome_message_to_all_students'),
    # path('notify_students/', views.index, name='notify_students'),
    path('', views.index),
    # path('assignment reainder', views.assignment_reminder, name='assignment_reminder'),
]