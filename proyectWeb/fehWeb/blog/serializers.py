from .models import Post

from rest_framework import serializers

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
    
    def validate_titulo(self, value):
        existe = Post.objects.filter(titulo=value).exists()

        if existe:
            raise serializers.ValidationError('el titulo ya existe')
        return value