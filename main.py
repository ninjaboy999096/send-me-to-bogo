from pyscript import document # pyright: ignore[reportMissingImports]
from pyscript import WebSocket as websockets # pyright: ignore[reportMissingImports]
element=document.querySelector("#output")
import asyncio
import json
from pyodide.http import pyfetch # pyright: ignore[reportMissingImports]
from decimal import Decimal,getcontext,MAX_EMAX
import datetime as dt
import math
import csv

CSV_URL="https://docs.google.com/spreadsheets/d/e/2PACX-1vTuPEsPcLX3dLRD66g81Qotpm0MpaxXyN8dU_SOg5ijDXAQBlc0kaBxzcGOoQl8MlndYJUe7fPN3bXM/pub?output=csv"
async def render_csv():
    table=document.querySelector("#table-body")
    res=await pyfetch(CSV_URL,method="GET")
    news=csv.reader((await res.string()).splitlines())
    htmlrows=[]
    for row in news:
        if(len(row)>=1):
            htmlrows.append(f"<tr><td>{row[0]}</td><td>{row[1]if len(row)>1 else ""}</td></tr>")
    table.innerHTML="".join(htmlrows[::-1])
if __name__ == "__main__":
    asyncio.ensure_future(render_csv())
