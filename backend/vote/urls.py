from django.urls import path

from vote.views.voting_menu import VotingMenuView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/vote/voting-menu/
    path(
        route="voting-menu/",
        view=VotingMenuView.as_view(),
        name="voting_menu",
    ),
]
