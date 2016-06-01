
setlocal EnableDelayedExpansion
for /F "tokens=1 delims=." %%a in ("%1") do (
      set filename=%%a
)
for /F "tokens=2 delims=." %%a in ("%1") do (
      set extn=%%a
)

R:\studio\nyc\bin\ffmpeg\20150312\win\bin\ffmpeg.exe -i %filename%.%extn% -c copy -ss 12 -to 30  %filename%_crop.mp4