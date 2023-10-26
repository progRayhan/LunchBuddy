from django.urls import path

from winner_restaurant.views.current_day_result import CurrentDayWinnerResultView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/winner-restaurant/current-day-list/
    path(
        route="current-day-list/",
        view=CurrentDayWinnerResultView.as_view(),
        name="current_day_winner_result",
    ),
]
