from rest_framework.serializers import ModelSerializer

from example.models import Example, ExampleRelatedModel


class ExampleRelatedModelSerializer(ModelSerializer):
    class Meta:
        model = ExampleRelatedModel
        fields = '__all__'


# read serializer нужен для того чтобы при запросе выдавать полноценную информацию
class ExampleReadSerializer(ModelSerializer):
    related_model = ExampleRelatedModelSerializer()

    class Meta:
        model = Example
        fields = ('name', 'status', 'related_model')


class ExampleWriteSerializer(ModelSerializer):
    class Meta:
        model = Example
        fields = ('name', 'status', 'related_model')
