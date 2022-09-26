import click

from rule_of_three import __version__
from rule_of_three.rule_of_three import rule_of_three


@click.command()
@click.version_option(version=__version__)
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.argument("c", type=float)
def main(a, b, c):
    """A is to B what C is to ??"""
    x = rule_of_three(a, b, c)
    click.echo(f"{x}")


if __name__ == "__main__":
    main()
