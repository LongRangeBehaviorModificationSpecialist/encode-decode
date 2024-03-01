# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich import box, print
from rich.align import Align
from rich.console import Console, Group
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Make the console object
console = Console()


class Results:


    def set_output_type(self) -> str:
        output_type: str = console.input(f'''[bright_white]
Enter output format (`p` = Panels or `t` = Table) >>> ''')
        return output_type.strip().lower()


    def print_results(self, results: str) -> str:
        output: str = console.print(f'''[bold dodger_blue1]
RESULTS:
[bold yellow2]{results}''')
        return output


    def print_results_table(self, results_dict: dict) -> None:
        results_table = Table(
            box=box.HORIZONTALS,
            show_header=True,
            header_style='bold #2070b2',
            show_lines=True)

        results_table.add_column(
            Text('Format', justify='left'),
                justify='left',
                no_wrap=False)

        results_table.add_column(
            Text('Encoded String', justify='left'),
                justify='left',
                ratio=2,
                no_wrap=False)

        results_table.add_row(
            f'[bold green3]Input Value',
            f'[bold green3]`{results_dict["input"]}`')

        new_dict = {key: value for key, value in results_dict.items() if key not in ['type','input']}

        for key, value in new_dict.items():
            results_table.add_row(
                f'[bright_white]{key}',
                f'[khaki1]{value}',
                end_section=True)

        inner_panel = Panel(
            Align.center(
                Group(
                    Align.left(results_table)),
                vertical='middle'),
            box=box.ROUNDED,
            expand=False,
            style='none',
            border_style='none',
            title=f'Convert from {results_dict["type"].upper()} Input',
            safe_box=True)

        print(inner_panel)


    def print_results_panels(self, results_dict: dict) -> None:
        new_dict = {key: value for key, value in results_dict.items() if key not in ['type','input']}
        for key, value in new_dict.items():
            rend = [Panel(f'[yellow]{value}',
                          border_style='blue',
                          expand=True,
                          title=f'{key}',
                          padding=(0,1),
                          safe_box=True)]
            print(Columns(rend))
