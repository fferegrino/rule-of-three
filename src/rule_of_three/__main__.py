import click

from rule_of_three import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """Rule of three!"""
    click.echo("Rule of three for you")

if __name__ == "__main__":
    main()
