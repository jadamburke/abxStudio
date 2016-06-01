
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

R:\studio\nyc\bin\ffmpeg\20150312\win\bin\ffmpeg.exe -r 30 -start_number %startfr% -i %filename%.%%04d.%extn% -s 3840x2160 -threads 0 -vcodec libx264 -b:v 60000k -bufsize 90000k -maxrate 120000k -vf format=yuv420p -r 30 %filename%.mp4