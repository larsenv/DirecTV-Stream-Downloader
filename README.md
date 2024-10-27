# DirecTV Stream Downloader

This tool lets you download DirecTV content either that is a recording, on demand video, or live TV stream.

You need a L3 Widevine CDM, [WidevineProxy](http://github.com/DevLARLEY/WidevineProxy2/) installed on the browser that you're using to stream DirecTV, and [Nm3u8DLRE](http://github.com/nilaoda/N_m3u8DL-RE/releases/latest/) if you're using Mac / Linux.

Here are the instructions.

1. Run the Python script here.
2. Make sure WidevineProxy is enabled and that your CDM is loaded with the tool. Play back whatever you want to download, and the key should show up 3 times in the window of the extension. Copy and paste the key to the script when it asks you.
3. Open Developer Mode and then find the first m3u8 it loaded. Make sure the m3u8 starts with the word output, but don't grab the m3u8 that has information about the bitrate, codec, resolution, framerate, etc in it. Copy and paste that to the script when it asks you.
4. If you're downloading a livestream, write the duration of how much you want to record.
5. Enter the filename if you want.

The script will make a mp4 file in the directory