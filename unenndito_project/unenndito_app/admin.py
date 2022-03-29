from django.contrib import admin
from .models import UserRegistration, Post

# # For population purposes
# from .models import UserRegistration
# from .models import UserRegistration, HrepsPoliticiansInfo, HrepsVotePatterns
# from .models import UserRegistration, HouseOfRepsBills, HrepsVotePatterns

# # Modyfying the HouseOfRepsBills model to be more efficient in the admin panel aqnd to have better display
# class HouseOfRepsBillsAdmin(admin.ModelAdmin):
#     list_display = ('title_of_bill', 'date', 'category', 'originating_house', 'status', 'current_house', 'stage_of_bill', 'portfolio', 'proposed_ammendments', 'summary', 'link_to_bill', 'date_added')
#     search_fields = ['title_of_bill', 'summary']

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('useremail', 'username', 'firstname', 'middlename', 'lastname', 'address', 'phone', 'age', 'lga', 'datereg')
    search_fields = ['username', 'lastname', 'datereg']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


# One way to register models(Tweaking the display)
# admin.site.register(HouseOfRepsBills, HouseOfRepsBillsAdmin)
admin.site.register(UserRegistration, UserRegistrationAdmin)
admin.site.register(Post, PostAdmin)


# # Alternative way to register models
# admin.site.register(UserRegistration)