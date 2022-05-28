from django.urls import path
from .views import MonthCalendar

app_name = 'MonthCalenderApp'

urlpatterns = [
    path('', MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', MonthCalendar.as_view(), name='month'),
]