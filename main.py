import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from core.intel import IntelligenceEngine
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗██╗   ██╗ ██╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔════╝╚██╗ ██╔╝███║[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ███████╗ ╚████╔╝ ╚██║[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ╚════██║  ╚██╔╝   ██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ███████║   ██║    ██║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚══════╝   ╚═╝    ╚═╝[/bold blue]
 [bold yellow]             Ultimate OSINT Intelligence Suite[/bold yellow]
 [italic cyan]                    Developed by Ghost-SY1[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    target = Prompt.ask("[bold yellow]Enter Target (Domain or IP)[/bold yellow]")
    if not target: return
    engine = IntelligenceEngine(target)
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Gathering Intelligence...", total=None)
        ip = engine.resolve_domain(target) if not target.replace(".", "").isdigit() else target
        ip_info = engine.get_ip_info(ip)
        dns_info = engine.get_dns_records(target) if not target.replace(".", "").isdigit() else None
    if ip_info:
        ip_table = Table(title="IP Intelligence", border_style="bold red")
        ip_table.add_column("Field", style="cyan")
        ip_table.add_column("Data", style="white")
        for k, v in ip_info.items():
            ip_table.add_row(str(k), str(v))
        console.print(ip_table)
    if dns_info:
        dns_table = Table(title="DNS Records", border_style="bold blue")
        dns_table.add_column("Type", style="cyan")
        dns_table.add_column("Records", style="white")
        for t, r in dns_info.items():
            dns_table.add_row(t, ", ".join(r) if r else "N/A")
        console.print(dns_table)
if __name__ == "__main__":
    main()
