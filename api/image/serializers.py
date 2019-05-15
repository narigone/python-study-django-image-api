from image.models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    image_file = serializers.FileField(max_length=None, use_url=True, required=False, allow_empty_file=True)

    class Meta:
        model = Image
        fields = '__all__' 