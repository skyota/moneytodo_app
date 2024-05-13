import calendar, datetime
from collections import deque
from .models import Task

class BaseCalendarMixin:
  first_weekday = 0
  week_names = ['月', '火', '水', '木', '金', '土', '日']
  def setup_calendar(self):
    self._calendar = calendar.Calendar(self.first_weekday)

  def get_week_names(self):
    week_names = deque(self.week_names)
    week_names.rotate(-self.first_weekday)
    return week_names
  
class WeekCalendarMixin(BaseCalendarMixin):
  def get_week_days(self):
    month = self.kwargs.get('month')
    year = self.kwargs.get('year')
    day = self.kwargs.get('day')
    if month and year and day:
      date = datetime.date(year=int(year), month=int(month), day=int(day))
    else:
      date = datetime.date.today()

    for week in self._calendar.monthdatescalendar(date.year, date.month):
      if date in week:
          return week

  def get_week_calendar(self):
    self.setup_calendar()
    days = self.get_week_days()
    first = days[0]
    last = days[-1]
    calendar_data = {
      'now': datetime.date.today(),
      'week_days': days,
      'week_previous': first - datetime.timedelta(days=7),
      'week_next': first + datetime.timedelta(days=7),
      'week_names': self.get_week_names(),
      'week_first': first,
      'week_last': last,
    }
    return calendar_data
  
class WeekWithScheduleMixin(WeekCalendarMixin):
  def get_week_schedules(self, start, end, days):
    lookup = {
      # '例えば、date__range: (1日, 31日)'を動的に作る
      '{}__range'.format(self.date_field): (start, end)
    }
    # 例えば、Schedule.objects.filter(date__range=(1日, 31日)) になる
    queryset = self.model.objects.filter(**lookup).order_by('start_time')

    # {1日のdatetime: 1日のスケジュール全て, 2日のdatetime: 2日の全て...}のような辞書を作る
    day_schedules = {day: [] for day in days}
    for schedule in queryset:
      schedule_date = getattr(schedule, self.date_field)
      day_schedules[schedule_date].append(schedule)
    return day_schedules

  def get_week_calendar(self):
    calendar_context = super().get_week_calendar()
    calendar_context['week_day_schedules'] = self.get_week_schedules(
      calendar_context['week_first'],
      calendar_context['week_last'],
      calendar_context['week_days']
    )
    return calendar_context