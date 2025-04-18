from rest_framework import serializers
from blog.models import Post , Category 
from accounts.models import Profile



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name']


# Post serializer for single and list post  
class PostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields =['id','author','title','content','status','category','absolute_url','created_date','published_date']
        read_only_fields = ['author']
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url',None)
        else:
            rep.pop('content',None)
       
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)