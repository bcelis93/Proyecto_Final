from django.test import TestCase
from blog.models import Autor, Libro, Editorial

# Create your tests here.


def test_crear_autor(self):
    autor = Autor.objects.create(nombre="Jorge ", apellido="Borges")
    todos_los_autores = autor.objects.all()
    assert len(todos_los_autores) == 1
    assert todos_los_autores[0].nombre == "Jorge"


def test_crear_libro(self):
    libro = Libro.objects.create(titulo=" Rayuela", genero="Ficcion")
    todos_los_libros = libro.objects.all()
    assert len(todos_los_libros) == 1
    assert todos_los_libros[0].titulo == "Rayuela"


def test_crear_editorial(self):
    editorial = Editorial.objects.create(nombre=" Alfaguara")
    todos_las_editoriales = editorial.objects.all()
    assert len(todos_las_editoriales) == 1
    assert todos_las_editoriales[0].nombre == "Alfaguara"
