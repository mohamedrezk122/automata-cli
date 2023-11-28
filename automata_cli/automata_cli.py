import click
import dot2tex

from automata_cli.renderer import *
from automata_cli.scanner import *

filename_arg    = click.argument("filename", required=True, type=click.Path(exists=True))
output_file_opt = click.option(
    "-o", 
    "--output",
    default ="output" , 
    show_default= True , 
    type=click.Path(),
    help = "output file path, default output.[format]"
)
config_opt = click.option(
    "-c",
    "--config",
    type=click.Path(exists=True),
    default ="config.yaml" , 
    show_default= True , 
    help="configuration file path if not specified the default configs will be loaded",
)


@click.group()
def cli():
    """
        A programmatic Automata renderer and minimizer \n
        AUTHOR : Mohamed Rezk
    """
    pass


@cli.command("render" , short_help = "render automata specification to media format")
@filename_arg
@output_file_opt
@config_opt 
@click.option(
    "-f",
    "--format",
    type=str,
    default ="png" , 
    show_default= True , 
    help="output format can be [pdf|png|eps|svg|gif|...]",
)
@click.option(
    "-s",
    "--keep_source",
    is_flag=True,
    default = False , 
    show_default= True , 
    help="keep graphviz source file, default False"
)
@click.option(
    "-v",
    "--view",
    is_flag=True, 
    default = False , 
    show_default= True , 
    help="view output in default application, default False"
)
def render(filename, output, config, format, keep_source, view):
    """
    render automata specification source file to whatever 
    """
    rendering_graph =  dry_render(filename, output, config, format)
    rendering_graph.render(cleanup= not keep_source, view=view)

    click.echo()
    click.echo(f"DONE rendering {filename} to {format} ")
    click.echo(f"Output is written to {output_name}")



@cli.command("minimize")
@filename_arg
@output_file_opt
def minimize(filename, output):
    raise NotImplementedError()




@cli.command("export", short_help = "export dot source to tex [tikz] format")
@filename_arg
@output_file_opt
@config_opt
@click.option(
    "-f",
    "--format",
    type=click.Choice(['pstricks', 'pgf', 'pst', 'tikz', 'psn']),
    default ="tikz" , 
    show_default= True , 
    help="output format ",
)
def export(filename,output,config, format):
    """
    export automata specification source to tex format for latex embedding 
    """
    rendering_graph = dry_render(filename,output,config,format="png")
    tex_source = dot2tex.dot2tex(
        rendering_graph.source, format=format, duplicate=True, autosize=True, prog="dot"
    )

    output_name = output + ".tex" if ".tex" not in output else output

    with open(output_name, "w") as file:
        file.write(tex_source)

    click.echo()
    click.echo(f"DONE exporting {filename} to tex ")
    click.echo(f"Output is written to {output_name}")

if __name__ == "__main__":
    cli()
