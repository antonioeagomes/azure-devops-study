import click

@click.command(help="This is just a hello world.")
@click.option("--name", prompt="Your name")
@click.option("--color", prompt="A color")
def hello(name, color):
    if name == "Michelangelo":
        click.echo("Nunchacos")
        click.echo(click.style(f"Hello {name}", fg="red"))
    else:
        click.echo("Mestre Splinter")
        click.echo(click.style(f"Hello {name}", fg=color))

if __name__ == "__main__":
    hello()