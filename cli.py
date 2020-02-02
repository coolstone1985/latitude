import click
from src.generate_fixed_width_file import generate_fixed_width_file
from src.parse_fixed_width_file import parse_fixed_width_file
from src.config import load_spec

@click.group()
@click.option('--spec', '-s', help='spec file location', required=True)
@click.pass_context
def cli(ctx, spec):
    ctx.obj = load_spec(spec)

@cli.command()
@click.argument('output_file')
@click.pass_context
def generate_file(ctx, output_file):
    generate_fixed_width_file(ctx.obj, output_file)

@cli.command()
@click.argument('output_file')
@click.argument('input_file')
@click.pass_context
def parse_file(ctx, output_file, input_file):
    parse_fixed_width_file(ctx.obj, input_file, output_file)


if __name__ == '__main__':
    cli(obj={})
