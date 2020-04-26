from .models import University, Professor, ProfessorRating
from .serializers import ProfessorSerializer, UniversityFullSerializer, ProfessorRatingSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.http import JsonResponse


class UniversityViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversityFullSerializer


class ProfessorViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['full_name', 'subjects__name', 'subjects__abbreviation', 'universities__name', 'universities__abbreviation']
    filterset_fields = ['universities', ]


class ProfessorRatingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ProfessorRating.objects.all()
    serializer_class = ProfessorRatingSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data, status = serializer.complete()
        return Response(data, status)


def total_ratings(request):
    professor_id = request.GET['professor_id']
    professor_ratings = ProfessorRating.objects.filter(professor_id=professor_id)
    ones = professor_ratings.filter(value=1).count()
    twos = professor_ratings.filter(value=2).count()
    threes = professor_ratings.filter(value=3).count()
    fours = professor_ratings.filter(value=4).count()
    fives = professor_ratings.filter(value=5).count()
    total = professor_ratings.count()
    average = round((ones * 1 + twos * 2 + threes * 3 + fours * 4 + fives * 5) / total) if total else 0
    return JsonResponse({
        'ones': ones,
        'twos': twos,
        'threes': threes,
        "fours": fours,
        'fives': fives,
        'total': total,
        'average': average
    })


def count_metrics(request):
    professors = Professor.objects.count()
    universities = University.objects.count()
    reviews = ProfessorRating.objects.count()

    return JsonResponse({
        'professors': professors,
        'universities': universities,
        'reviews': reviews
    })

