import urllib.parse
import os
import platform

print("DirecTV Stream Downloader by Larsenv\n")

key = input("Enter the decryption key: ")
stream = (
    urllib.parse.quote_plus(input("Enter the stream m3u8 url: "))
    .replace("%3A", ":")
    .replace("%2F", "/")
)
duration = input(
    "Enter the duration of the stream (HH:MM:SS) - leave blank if not using livestream: "
)
output_name = input(
    "Enter the output file name without extension - leave blank to use default: "
)

if len(duration) == 8 and duration.count(":") == 2:
    duration_time = (
        " "
        + "--live-real-time-merge"
        + " "
        + "--live-record-limit"
        + " "
        + duration
        + " "
    )
else:
    duration_time = ""

if output_name != "":
    output_filename = " " + "--save-name" + " " + output_name + " "
else:
    output_filename = ""

os.system(
    ".\\"
    if platform.system() == "Windows"
    else ""
    + "N_m3u8DL-RE"
    + " "
    + stream
    + " "
    + "--key"
    + " "
    + key
    + " "
    + "--mux-after-done"
    + " "
    + "format=mp4"
    + duration_time
    + output_filename
)
