from rest_framework import serializers
from ...models import Task


class TaskSerializer(serializers.Serializer):
    # absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    
    class Meta: 
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date', 'updated_date']
        
    # def get_abs_url(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.pk)