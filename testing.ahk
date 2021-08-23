MButton::
WinGet, winid ,, A ; <-- need to identify window A = acitive
WinActivate, ahk_exe Discord.exe
Send Hello
WinActivate ahk_id %winid%
Return
    	