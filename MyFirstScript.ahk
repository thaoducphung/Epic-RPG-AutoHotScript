!q:: ; ALT-Q
Send, RPG HUNT T {Enter}
return

!w:: ; ALT-W
Send, RPG AXE {Enter}
return

!e:: ; ALT-E
Send, RPG TRAINING {Enter}
return

!s:: ; ALT-S
Send, RPG CD {Enter}
return

!a:: ; ALT-A
Send, RPG ADVENTURE {Enter}
return

!f:: ; ALT-F
Send, RPG FARM CARROT {Enter}
return

!b:: ; ALT-B
Send, RPG BUY ED LB {Enter}
return

!h:: ; ALT-H
Send, RPG HEAL {Enter}
return

!z::Send {Alt Down}{Tab}{Alt Up}

MButton::
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG I{Enter}
	If (Toggle = 1) {
	sleep 500
	SetKeyDelay 30,50
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

MButton::
WinGet, winid ,, A ; <-- need to identify window A = acitive
WinActivate, ahk_exe Discord.exe
Send Hello
sleep 500 ;
WinActivate ahk_id %winid%
Return