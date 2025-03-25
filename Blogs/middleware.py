from .models import PostEngagement


class PostViewTrackingMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response

    def __call__(self , request):
        response = self.get_response(request)

        # Only track GET requests to post detail views
        if (request.method == 'GET' and
                request.path.startswith('/api/blog/posts/') and
                request.path.count('/') == 4):

            post_id = request.path.split('/')[3]
            try:
                engagement = PostEngagement.objects.get(post_id=post_id)
                engagement.views += 1

                # Track unique views based on session
                if f'post_viewed_{post_id}' not in request.session:
                    engagement.unique_views += 1
                    request.session[f'post_viewed_{post_id}'] = True

                engagement.save()
            except PostEngagement.DoesNotExist:
                pass

        return response