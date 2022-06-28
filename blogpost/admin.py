from django.contrib import admin
from django.db.models import Q

from .models import Post, Block
from .models import Comment
from .models import Author
# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display = ['content',]

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user == obj.user or request.user == obj.post.author.user:
                return True

    def has_delete_permission(self, request, obj=None):
        if obj:
            if request.user == obj.user or request.user == obj.post.author.user:
                return True


admin.site.register(Comment,CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'content']
    list_filter =['dateCreated',]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Post.objects.all()
        allposts=Post.objects.all()
        blockObjects = Block.objects.filter().all()
        if blockObjects:
            for b in blockObjects:
                for p in allposts:
                    if b.bloked_user == request.user and b.bloking_user == p.author.user:
                        allposts=allposts.filter(~Q(title=p.title)).all()
        return allposts

    def has_change_permission(self, request, obj=None):
        if obj:
            blockObjects = Block.objects.filter(bloking_user=request.user).all()
            if blockObjects:
                for b in blockObjects:
                    if b.bloked_user == request.user:
                        return False
            if request.user == obj.author.user:
                return True

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.author.user:
            return True


admin.site.register(Post,PostAdmin)




class BlockAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Block.objects.all()
        queryset = Block.objects.filter(bloking_user=request.user).all()
        return queryset

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user == obj.bloking_user:
                return True

    def has_delete_permission(self, request, obj=None):
        if obj:
            if request.user == obj.bloking_user:
                return True
admin.site.register(Block,BlockAdmin)


class AuthorAdmin(admin.ModelAdmin):

    list_display = ['first_name','last_name','country']
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
           return True
        if obj and request.user == obj.user :
            return True

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True

admin.site.register(Author,AuthorAdmin)

