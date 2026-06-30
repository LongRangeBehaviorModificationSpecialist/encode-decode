# !/usr/bin/env python3

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


# Make the console object
c = Console()


class Results:


    def __init__(self, results_dict: dict):
        self.results_dict = results_dict


    def print_rotation_results(self, results: str) -> str:
        output = c.print(f"""[bold blue]
\nString Rotation Results
-----------------------\n
[bold khaki3]{results}\n""")
        return output


    def print_results_table(self, results_dict: dict) -> None:
        results_table = Table(
            box=box.HORIZONTALS,
            show_header=True,
            header_style="bold #2070b2",
            show_lines=True)

        results_table.add_column(
            Text("Format", justify="left"),
                justify="left",
                no_wrap=False)

        results_table.add_column(
            Text("Encoded String", justify="left"),
                justify="left",
                ratio=2,
                no_wrap=False)

        results_table.add_row(
            f"[bold green3]Input Value",
            f"[bold green3]\'{results_dict['user_input']}\'")

        new_dict = {key: value for key, value in results_dict.items() if key not in ["type", "user_input"]}

        for key, value in new_dict.items():
            results_table.add_row(
                f"[bright_white]{key}",
                f"[khaki1]{value}",
                end_section=True)

        inner_panel = Panel(
            Align.center(Group(Align.left(results_table)), vertical="middle"),
            box=box.ROUNDED,
            expand=False,
            style="none",
            border_style="none",
            title=f"Input Data Type : {results_dict['type']}",
            safe_box=True)

        c.print("\n")
        c.print(inner_panel)
