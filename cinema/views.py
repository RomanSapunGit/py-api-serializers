# write views here
from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, MovieSession, CinemaHall, Actor, Genre
from cinema.serializers import (
    ListMovieSerializer,
    DetailMovieSerializer,
    MovieSerializer,
    DetailMovieSessionSerializer,
    MovieSessionSerializer,
    ListMovieSessionSerializer,
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
    DetailCinemaHallSerializer
)


class MovieViewSet(ModelViewSet):
    queryset = (Movie.objects
                .all()
                .prefetch_related("genres", "actors")
                )

    def get_serializer_class(self):
        if self.action == "list":
            return ListMovieSerializer
        if self.action == "retrieve":
            return DetailMovieSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = (MovieSession
                .objects
                .all()
                .prefetch_related("movie", "cinema_hall")
                )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailMovieSessionSerializer
        if self.action == "list":
            return ListMovieSessionSerializer
        return MovieSessionSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailCinemaHallSerializer
        return CinemaHallSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
