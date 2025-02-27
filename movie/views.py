import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .models import Movie

# Create your views here.

def home(request):
    #return HttResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html', {'name': 'William Andres Henao'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .models import Movie  # Asegúrate de importar el modelo correcto

def statistics_view(request):
    # Obtener todas las películas
    all_movies = Movie.objects.all()

    # ======= Gráfica de películas por año =======
    movie_counts_by_year = {}
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        movie_counts_by_year[year] = movie_counts_by_year.get(year, 0) + 1

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))

    plt.figure(figsize=(10, 5))
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    graphic_year = base64.b64encode(buffer1.getvalue()).decode()
    buffer1.close()
    plt.close()

    # ======= Gráfica de películas por género =======
    movie_counts_by_genre = {}
    for movie in all_movies:
        genres = movie.genre.split(',')  # Suponiendo que los géneros están separados por comas
        first_genre = genres[0].strip() if genres else "None"
        movie_counts_by_genre[first_genre] = movie_counts_by_genre.get(first_genre, 0) + 1

    bar_positions_genre = range(len(movie_counts_by_genre))

    plt.figure(figsize=(10, 5))
    plt.bar(bar_positions_genre, movie_counts_by_genre.values(), width=bar_width, align='center', color='skyblue')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions_genre, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    graphic_genre = base64.b64encode(buffer2.getvalue()).decode()
    buffer2.close()
    plt.close()

    # Renderizar la plantilla con ambas gráficas
    return render(request, 'statistics.html', {'graphic_year': graphic_year, 'graphic_genre': graphic_genre})