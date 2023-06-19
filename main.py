# Copyright (c) 2021 GOUTHAM SER

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pyrogram
from pyrogram import Client
import time
import os


print("Starting...")
time.sleep(1.5)

code=">>>>>>\n"
x=0

for i in code:
    x=x+1
    time.sleep(0.6)
    print(code[0:x])



goutham="""

░██████╗░░█████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░░███╗  ░██████╗███████╗██████╗░
██╔════╝░██╔══██╗██║░░░██║╚══██╔══╝██║░░██║██╔══██╗████╗░████║  ██╔════╝██╔════╝██╔══██╗
██║░░██╗░██║░░██║██║░░░██║░░░██║░░░███████║███████║██╔████╔██║  ╚█████╗░█████╗░░██████╔╝
██║░░╚██╗██║░░██║██║░░░██║░░░██║░░░██╔══██║██╔══██║██║╚██╔╝██║  ░╚═══██╗██╔══╝░░██╔══██╗
╚██████╔╝╚█████╔╝╚██████╔╝░░░██║░░░██║░░██║██║░░██║██║░╚═╝░██║  ██████╔╝███████╗██║░░██║
░╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░╚══════╝╚═╝░░╚═╝



Copyright (C) 2021 by GouthamSER @Github, < https://github.com/GouthamSER >.
This file is part of dev project,
and is released under the "MIT License Agreement".
All rights reserved.
"""


print(goutham)
API_ID=int(input("Enter Your API_ID: "))
API_HASH=input("Enter Your API_HASH: ")

print("\n")

app = Client(
    "session",
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=True,
)

app.start()
print("\n\n ⚠️⚠️⚠️ PLEASE COPY FROM HERE THE SESSION STRING ⚠️⚠️⚠️")

print("\nSession String:", 
      app.export_session_string())

print("\n\n")

input("Press ENTER to close...")

os._exit(0)
