import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()

############################################################
# Ejemplo

url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format(1))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')

ejemplo = libros[0].select('.star-rating.Three')
ejemplo2 = libros[0].select('a')[1]['title']
print(ejemplo2)
