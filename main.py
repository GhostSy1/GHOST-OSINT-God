import os
import sys
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from core.intel import IntelligenceEngine
from core.social import SocialIntelligence
from core.breach import BreachIntelligence
from core.website import WebsiteIntelligence
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
async def run_osint():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold cyan][1][/bold cyan] Network & Domain Intel")
    console.print("[bold cyan][2][/bold cyan] Social Media Recon")
    console.print("[bold cyan][3][/bold cyan] Email & Breach Check")
    console.print("[bold cyan][4][/bold cyan] Website & Corporate Tech Intel")
    choice = Prompt.ask("[bold yellow]Select Intelligence Module[/bold yellow]", choices=["1", "2", "3", "4"])
    if choice == "1":
        target = Prompt.ask("[bold yellow]Enter Domain or IP[/bold yellow]")
        engine = IntelligenceEngine(target)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Gathering Network Intelligence...", total=None)
            ip = engine.resolve_domain(target) if not target.replace(".", "").isdigit() else target
            ip_info = engine.get_ip_info(ip)
            dns_info = engine.get_dns_records(target) if not target.replace(".", "").isdigit() else None
        if ip_info:
            t = Table(title="IP Intelligence", border_style="bold red")
            t.add_column("Field", style="cyan"); t.add_column("Data", style="white")
            for k, v in ip_info.items(): t.add_row(str(k), str(v))
            console.print(t)
    elif choice == "2":
        username = Prompt.ask("[bold yellow]Enter Username to Search[/bold yellow]")
        social = SocialIntelligence(username)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description=f"Searching for '{username}' across platforms...", total=None)
            results = await social.run()
        if results:
            t = Table(title="Social Media Results", border_style="bold green")
            t.add_column("Platform", style="cyan"); t.add_column("URL", style="white")
            for p, u in results.items(): t.add_row(p, u)
            console.print(t)
    elif choice == "4":
        url = Prompt.ask("[bold yellow]Enter Target URL[/bold yellow]")
        web_intel = WebsiteIntelligence(url)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Analyzing Website Technology Stack...", total=None)
            tech = web_intel.get_tech_stack()
        if tech:
            t = Table(title="Technology Intelligence", border_style="bold yellow")
            t.add_column("Component", style="cyan"); t.add_column("Detection", style="white")
            for item in tech:
                parts = item.split(": ")
                t.add_row(parts[0], parts[1] if len(parts)>1 else "Detected")
            console.print(t)
        else:
            console.print("[bold red][!][/bold red] No specific technologies detected.")
def main():
    asyncio.run(run_osint())
if __name__ == "__main__":
    main()
