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

goutham="""

░██████╗░░█████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░
██╔════╝░██╔══██╗██║░░░██║╚══██╔══╝██║░░██║██╔══██╗
██║░░██╗░██║░░██║██║░░░██║░░░██║░░░███████║███████║
██║░░╚██╗██║░░██║██║░░░██║░░░██║░░░██╔══██║██╔══██║
╚██████╔╝╚█████╔╝╚██████╔╝░░░██║░░░██║░░██║██║░░██║
░╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝

░██████╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗
╚█████╗░█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗
██████╔╝███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝


Copyright (C) 2021 by GouthamSER @Github, < https://github.com/GouthamSER >.
This file is part of dev project,
and is released under the "MIT License Agreement".
All rights reserved.
"""

print(goutham)
api_id = input("Enter Your API ID: ")
api_hash = input("Enter Your API HASH : ")

get("\n")

with Client("GOutham", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \nThanks To @im_goutham_josh \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
