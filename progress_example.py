from rich.progress import Progress
import asyncio

async def lots_of_work(n: int, progress: Progress) -> None:
    for i in progress.track(range(n), description=f"[red]Computing {n}..."):
        await asyncio.sleep(.1)

async def main():
    with Progress() as progress:
        async with asyncio.TaskGroup() as g:
            g.create_task(lots_of_work(40, progress))
            g.create_task(lots_of_work(30, progress))

asyncio.run(main())
