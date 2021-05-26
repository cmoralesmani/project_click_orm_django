import click

products_list = [
    {
        'id': 1,
        'name': 'TV Smart 14"',
        'price': 400,
        'available': True
    },
    {
        'id': 2,
        'name': 'Abanico',
        'price': 110,
        'available': True
    },
    {
        'id': 3,
        'name': 'Llave Cruz',
        'price': 35,
        'available': False
    },
]

@click.command()
@click.option('--name', default=str(''), prompt='Nombre del producto',
              help='Filtro para buscar los productos por su nombre.')
def products_filter(name):
    """
    Simple program to filter products by name
    If you do not specify any filter, it returns all products
    """
    products_filtered = [p for p in products_list if name in p['name']]
    click.echo("*** Listado de productos ***")
    for product in products_filtered:
        click.echo(f"Nombre: {product['name']} Precio: {product['price']}")

if __name__ == '__main__':
    products_filter()