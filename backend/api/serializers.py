from rest_framework import serializers
from api.models import University, Professor, ProfessorRating, Subject
from utils import constants
from rest_framework import status


class SubjectShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    abbreviation = serializers.CharField()


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class ProfessorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorRating
        exclude = ('updated_at',)

    def to_representation(self, instance):
        output = super().to_representation(instance)
        output['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return output

    def complete(self):
        email = self.validated_data['email']
        professor = self.validated_data['professor']
        if ProfessorRating.objects.last_review_in_week(email, professor):
            return constants.REVIEW_ALREADY_SUBMITTED, status.HTTP_400_BAD_REQUEST
        rating = ProfessorRating.objects.create(**self.validated_data)
        serializer = ProfessorRatingSerializer(instance=rating)
        return serializer.data, status.HTTP_201_CREATED


class ProfessorSerializer(serializers.ModelSerializer):
    ratings = ProfessorRatingSerializer(many=True, read_only=True)
    universities = UniversitySerializer(many=True)
    subjects = SubjectShortSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'first_name', 'last_name', 'patronymic',
                  'full_name', 'avatar', 'ratings', 'subjects',
                  'average_rating', 'rating_count', 'universities'
                  ]


class ProfessorShortSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    avatar = serializers.FileField()


class UniversityFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'abbreviation', 'description', 'logo', 'professor_set', 'subjects']

    professor_set = ProfessorShortSerializer(many=True, read_only=True)
    subjects = SubjectShortSerializer(many=True, read_only=True)

