
setlocal EnableDelayedExpansion

for /F "tokens=1 delims=." %%a in ("%1") do (
      set filename=%%a
)
for /F "tokens=2 delims=." %%a in ("%1") do (
      set startfr=%%a
)
for /F "tokens=3 delims=." %%a in ("%1") do (
      set extn=%%a
)

T:\nyc\bin\ffmpeg\20150312\win\bin\ffmpeg.exe -start_number %startfr% -i %filename%.%%04d.%extn% -vcodec libx264 -b:v 30000k -vf format=yuv420p -r 30 %filename%.mp4