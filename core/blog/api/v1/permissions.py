from rest_framework import permissions

#making class for  post editing permissions only when you owner of the post are

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    only allows owner of the post to edit the post 
    ''' 
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.user == request.user