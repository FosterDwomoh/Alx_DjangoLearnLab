from rest_framework import serializers
from .models import Post, Comment


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class PostSerializer(serializer.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'comments', 'created_at' 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def create(self, validated_date):
        validated_date['author'] = self.context['request'].user
        return super().create(validated_date)