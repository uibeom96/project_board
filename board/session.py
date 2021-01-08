from django.conf import settings
from board.models import Post



class Hit_session(object):
    def __init__(self, request):
        self.session = request.session
        hits = self.session.get(settings.HIT_ID)

        if not hits:
            hits = self.session[settings.HIT_ID] = {}

        self.hits = hits 


    def hit_add(self, post):
        if str(post.id) not in self.hits:
            post.hit_count += 1
            post.save()
        self.hits[(post.id)] = {str(post):str(post.author)}
        self.saves()
        

    def saves(self):
        self.session[settings.HIT_ID] = self.hits         
        self.session.modified = True

