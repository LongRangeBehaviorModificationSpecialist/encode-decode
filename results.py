# !/usr/bin/env python3

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.columns import Columns
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

# Make the console object
c = Console()


class Results:


    def __init__(self, data_type, results_dict: dict):
        self.data_type = data_type
        self.results_dict = results_dict


    def set_output_type(self) -> str:
        output_type = Prompt.ask(f"""[bright_white]
Enter output format ("p" = Panels or "t" = Table) """)
        return output_type.strip().lower()


    def print_rotation_results(self, results: str) -> str:
        output = c.print(f"""[bold blue]
\nString Rotation Results
-----------------------\n
[bold khaki3]{results}\n""")
        return output


    def print_results_table(self, data_type, results_dict: dict) -> None:
        results_table = Table(
            box=box.HORIZONTALS,
            show_header=True,
            header_style="bold #2070b2",
            show_lines=True
        )

        results_table.add_column(
            Text("Format", justify="left"),
                justify="left",
                no_wrap=False
        )

        results_table.add_column(
            Text("Encoded String", justify="left"),
                justify="left",
                ratio=2,
                no_wrap=False
            )

        results_table.add_row(
            f"[bold green3]Input Value ({data_type})",
            f"[bold green3]\'{results_dict['user_input']}\'"
        )

        new_dict = {key: value for key, value in results_dict.items() if key not in ["type", "user_input"]}

        for key, value in new_dict.items():
            results_table.add_row(
                f"[bright_white]{key}",
                f"[khaki1]{value}",
                end_section=True
            )

        inner_panel = Panel(
            Align.center(Group(Align.left(results_table)), vertical="middle"),
            box=box.ROUNDED,
            expand=False,
            style="none",
            border_style="none",
            title=f"""Convert from {results_dict["type"].upper()} Input""",
            safe_box=True
        )

        c.print(inner_panel)
