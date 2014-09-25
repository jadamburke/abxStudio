:: Write access must be set for the following folders on C drive must be set to everyone ^

@echo off

net use \\pp-fs-nyc\Pipeline T: 

:: After Effects CC Scripts ^

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\Startup "C:\Program Files\Adobe\Adobe After Effects CC\Support Files\Scripts\Startup" ClearCache.jsx /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /log:error_log.txt

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\UIPanels "C:\Program Files\Adobe\Adobe After Effects CC\Support Files\Scripts\ScriptUI Panels" PPNY_Qube_Submitter.jsx /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /log+:error_log.txt

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\Preferences\CC\12.1 "C:\Users\%username%\AppData\Roaming\Adobe\After Effects\12.1" *.* /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /S /log+:error_log.txt

:: After Effects CC 2014 Scripts ^

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\Startup "C:\Program Files\Adobe\Adobe After Effects CC 2014\Support Files\Scripts\Startup" ClearCache.jsx /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /log+:error_log.txt

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\UIPanels "C:\Program Files\Adobe\Adobe After Effects CC 2014\Support Files\Scripts\ScriptUI Panels" PPNY_Qube_Submitter.jsx /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /log+:error_log.txt

robocopy \\pp-fs-nyc\pipeline\nyc\tools\aftereffects\Preferences\CC2014\13.0 "C:\Users\%username%\AppData\Roaming\Adobe\After Effects\13.0" *.* /e /z /fft /purge /r:0 /w:0 /nocopy /xo /XF /TEE /COPY:DT /S /log+:error_log.txt

C:\Users\fernandog\AppData\Roaming\Adobe\After Effects\13.0

start "" "C:\Program Files\Adobe\Adobe After Effects %PP_AE%\Support Files\AfterFX.exe" 

exit

:: the purpose of this script is to force the user to clear out their cache and provide them with a passion ny qube submitter ^