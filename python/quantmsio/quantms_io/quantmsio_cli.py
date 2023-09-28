"""
Commandline interface for quantmsio package allows generating the quantms.io file format from different sources and
 steps. The quantms.io specification is available in the docs folder of this repository.
"""

import click

from quantms_io import __version__ as __version__
from quantms_io.commands.parquet_command import compare_feature_convert
from quantms_io.commands.project_command import generate_pride_project_json
from quantms_io.commands.differential_expression_command import (
    convert_msstats_differential,
)
from quantms_io.commands.feature_command import convert_feature_file
from quantms_io.commands.psm_command import convert_psm_file, compare_set_of_psms

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.version_option(
    version=__version__, package_name="quantms_io", message="%(package)s %(version)s"
)
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    This is the main tool that gives access to all commands to convert SDRF files into pipelines specific configuration files
    """
    pass


cli.add_command(generate_pride_project_json)
cli.add_command(convert_msstats_differential)
cli.add_command(convert_feature_file)
cli.add_command(convert_psm_file)
cli.add_command(compare_feature_convert)
cli.add_command(compare_set_of_psms)


def quantms_io_main():
    """
    Main function to run the quantmsio command line interface
    :return: none
    """
    cli()


if __name__ == "__main__":
    quantms_io_main()