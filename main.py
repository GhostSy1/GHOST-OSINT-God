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
 [bold yellow]         Ultimate OSINT & Corporate Intelligence Suite (2026)[/bold yellow]
 [italic cyan]                         Ghost-SY1 Security[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
async def run_osint():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing Ghost-OSINT-God Interactive Engine...[/bold yellow]\n")
    console.print("[bold cyan][1][/bold cyan] Network & Domain Geolocation & DNS Forensics")
    console.print("[bold cyan][2][/bold cyan] Global Social Media Username Profiling")
    console.print("[bold cyan][3][/bold cyan] Email Credential Leak & Breach Intelligence")
    console.print("[bold cyan][4][/bold cyan] Website Tech Stack & Corporate WHOIS Intelligence")
    choice = Prompt.ask("[bold yellow]Select Intelligence Module[/bold yellow]", choices=["1", "2", "3", "4"])
    if choice == "1":
        target = Prompt.ask("[bold cyan]Enter Domain or IP Address[/bold cyan]")
        engine = IntelligenceEngine(target)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Gathering Network Intelligence...", total=None)
            ip = engine.resolve_domain(target) if not target.replace(".", "").isdigit() else target
            ip_info = engine.get_ip_info(ip)
        if ip_info:
            t = Table(title="IP & Network Intelligence", border_style="bold red")
            t.add_column("Field", style="cyan"); t.add_column("Data", style="white")
            for k, v in ip_info.items(): t.add_row(str(k), str(v))
            console.print(t)
    elif choice == "2":
        username = Prompt.ask("[bold cyan]Enter Target Username[/bold cyan]")
        social = SocialIntelligence(username)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description=f"Profiling username '{username}' across global platforms...", total=None)
            results = await social.run()
        if results:
            t = Table(title="Social Media Profile Discovery", border_style="bold green")
            t.add_column("Platform", style="cyan"); t.add_column("Verified URL", style="white")
            for p, u in results.items(): t.add_row(p, u)
            console.print(t)
        else:
            console.print("[bold red][!][/bold red] No public profiles matched.")
    elif choice == "3":
        email = Prompt.ask("[bold cyan]Enter Target Email Address[/bold cyan]")
        breach = BreachIntelligence(email)
        if breach.validate_email():
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
                progress.add_task(description="Querying Breach Intelligence Databases...", total=None)
                res = breach.check_breaches()
            console.print(Panel(f"[bold green]Intelligence Status:[/bold green] {res['message']}", border_style="blue"))
        else:
            console.print("[bold red][!][/bold red] Invalid email format supplied.")
    elif choice == "4":
        url = Prompt.ask("[bold cyan]Enter Target Corporate URL[/bold cyan]")
        web_intel = WebsiteIntelligence(url)
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Analyzing Corporate Tech Stack & WHOIS...", total=None)
            tech = web_intel.get_tech_stack()
        if tech:
            t = Table(title="Corporate Technology Stack", border_style="bold yellow")
            t.add_column("Component", style="cyan"); t.add_column("Detection", style="white")
            for item in tech:
                parts = item.split(": ")
                t.add_row(parts[0], parts[1] if len(parts)>1 else "Detected")
            console.print(t)
        else:
            console.print("[bold red][!][/bold red] No specific technologies identified.")
def main():
    asyncio.run(run_osint())
if __name__ == "__main__":
    main()
