$mediaRoot = Join-Path (Split-Path $PSScriptRoot -Parent) 'media'

New-Item -ItemType Directory -Force -Path "$mediaRoot\video", "$mediaRoot\imges" | Out-Null
Copy-Item -Path 'C:\Users\轩\Desktop\video\*' -Destination "$mediaRoot\video" -Recurse -Force
Copy-Item -Path 'C:\Users\轩\Desktop\imges\*' -Destination "$mediaRoot\imges" -Recurse -Force

Write-Output "媒体文件已复制到 $mediaRoot"
