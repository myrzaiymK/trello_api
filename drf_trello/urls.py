from django.urls import path
from drf_trello import api
from drf_trello.card import api as card
from drf_trello.card.api_detail import *
from .views import *
from drf_trello.register import verify, register


urlpatterns = [
    # user
    path('users/', register.UserList.as_view(), name='api_users'),
    path('users/<int:pk>/', register.UserDetail.as_view()),
    path('email-verify/', verify.VerifyEmail.as_view(), name='email-verify'),
    path('reset_password/', verify.ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password/token/', verify.PasswordTokenCheckAPI.as_view(), name='reset_password_confirm'),

    # board
    path('boards/', api.BoardList.as_view(), name='boards'),
    path('boards/<int:pk>/', BoardDetail.as_view(), name='api_boards_detail'),
    path('members/', api.MemberList.as_view(), name='members'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='member_detail'),

    # column
    path('columns/', api.ColumnList.as_view(), name='api_columns'),
    path('columns/<int:pk>/', ColumnDetail.as_view(), name='api_columns_detail'),

    # comment
    path('comments/', api.CommentList.as_view(), name='api_comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),

    # card
    path('cards/', card.CardList.as_view(), name='api_cards'),
    path('cards/<int:pk>/', CardDetail.as_view(), name='api_cards_detail'),
    path('labels/', card.LabelList.as_view(), name='api_labels'),
    path('labels/<int:pk>/', LabelDetail.as_view(), name='api_labels_detail'),
    path('label_colors/', card.LabelColorList.as_view(), name='api_label_colors'),
    path('label_colors/<int:pk>/', LabelColorDetail.as_view(), name='api_label_colors_detail'),
    path('label_cards/', card.LabelCardList.as_view(), name='api_label_cards'),
    path('label_cards/<int:pk>/', LabelCardDetail.as_view(), name='api_label_cards_detail'),
    path('checklist/', card.CheckListCardView.as_view(), name='api_checklist'),
    path('checklist/<int:pk>/', CheckListDetail.as_view(), name='api_checklist_detail'),
    path('checklistcard/', card.CheckListCardView.as_view(), name='api_checklistcard'),
    path('checklistcard/<int:pk>/', CheckListCardDetail.as_view(), name='api_checklistcard_detail'),
    path('attachments/', card.AttachmentList.as_view(), name='api_attachments'),
    path('attachments/<int:pk>/', AttachmentDetail.as_view(), name='api_attachments_detail'),
    path('attachmentscard/', card.AttchmentCardList.as_view(), name='api_attachmentscard'),
    path('attachmentscard/<int:pk>/', AttachmentCardDetail.as_view(), name='attachmentscard_detail'),

    # functions
    path('archive/', api.ArchiveList.as_view(), name='archives'),
    path('archive/<int:pk>/', ArchiveDetail.as_view(), name='archive_detail'),
    path('favourites/', api.FavoriteList.as_view(), name='favourites'),
    path('favourites/<int:pk>/', FavouriteDetail.as_view(), name='favourites_detail'),
    path('search/', api.CustomSearchFilter, name='favourites'),
    path('recent_views/', api.RecentViewsView.as_view(), name='recent_views'),
]