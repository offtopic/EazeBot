
[Setup]
#define MyAppName "EazeBot"
#define MyAppVersion GetFileVersion("build\exe.win-amd64-3.6\eazebot.exe")
#define MyAppPublisher "Marcel Beining"
#define MyAppExeName "eazebot.exe"

; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{42F26635-3A1C-44D5-B8F9-8F9FB0D6BE64}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={userpf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=build\exe.win-amd64-3.6\LICENSE
InfoAfterFile=build\exe.win-amd64-3.6\readme.md
OutputBaseFilename=setupEazeBot
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "build\exe.win-amd64-3.6\eazebot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\exe.win-amd64-3.6\*"; Excludes: "lextab.py,yacctab.py"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[UninstallDelete]
Type: files; Name: "{app}\*.json"
Type: files; Name: "{app}\*.py"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Link to Wiki"; Filename: "{app}\Link to Eazebot Wiki.url"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userdesktop}\Link to Eazebot Wiki"; Filename: "{app}\Link to Eazebot Wiki.url"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

