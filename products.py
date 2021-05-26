import os
import sys

import click
import django

@click.command()
@click.option('--name', default=str(''), prompt='Nombre del producto',
              help='Filtro para buscar los productos por su nombre.')
def products_filter(name):
    """
    Simple program to filter products by name
    If you do not specify any filter, it returns all products
    """
    from service.products.models import Product
    products_filtered = Product.objects.filter(name__contains = name)
    click.echo("*** Listado de productos ***")
    for product in products_filtered:
        click.echo(f"Nombre: {product.name} Precio: {product.price}")

if __name__ == '__main__':
    # Turn off bytecode generation
    sys.dont_write_bytecode = True

    # Django specific settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
    django.setup()

    products_filter()