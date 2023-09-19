from django.contrib import admin
from .models import StudentsEvent
from .models import SportEvent
from .models import CreativeEvent
from .models import StudiesEvent
from .models import ScienceEvent
from .models import RatingTable
from .models import UserContext

admin.site.register(StudentsEvent)
admin.site.register(SportEvent)
admin.site.register(CreativeEvent)
admin.site.register(StudiesEvent)
admin.site.register(ScienceEvent)
admin.site.register(RatingTable)
admin.site.register(UserContext)