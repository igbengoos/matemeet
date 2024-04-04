from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDisLike, UserSearch, FollowerList, AddCommentLike, AddCommentDisLike, CommentReplyView, PostNotification, FollowNotification, RemoveNotification

urlpatterns = [
    
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='edit-post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete-post'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDisLike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    path('post/<int:pk>/likes', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislikes', AddDisLike.as_view(), name='dislike'),
    path('profile/<int:pk>/followers', FollowerList.as_view(), name='list-followers'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='edit-profile'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', UserSearch.as_view(), name='search-user'),
    path('notification/<int:notification_pk>/post/<int:post_pk>/', PostNotification.as_view(), name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>/', FollowNotification.as_view(), name='follow-notification'),
    path('notification/delete/<int:notification_pk>/', RemoveNotification.as_view(), name='delete-notification'),
    
]
