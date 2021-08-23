SetKeyDelay, 100, 200     ;
Random, , 1234     ; Initiate random number generator for  'humanizing'
Random, RndNum , 10, 1000    ; Generate first random number between 10-1000(10ms-1second)
#HotkeyModifierTimeout, 100

Toggle := 0

!1:: ; ALT-1
	Toggle ^= 1
Return

!q:: ; ALT-Q
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG HUNT T {Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!w:: ; ALT-W
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG PICKAXE{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!e:: ; ALT-E
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG TRAINING {Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!c:: ; ALT-C
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG CD{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!a:: ; ALT-A
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG ADVENTURE{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!d:: ; ALT-D
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG RD{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!f:: ; ALT-F
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG FARM CARROT{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!b:: ; ALT-B
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG BUY ED LB{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!h:: ; ALT-H
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG HEAL{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!p:: ; ALT-P
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG P{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!y:: ; ALT-Y
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, y{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!n:: ; ALT-N
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, n{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!i:: ; ALT-I
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, RPG I{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}

!z:: ; ALT-z
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, fight{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}


!j:: ; ALT-j
If WinExist("ahk_exe discord.exe"){
	WinActivate
	if ErrorLevel
	Return
	else
	SendInput, join{Enter}
	If (Toggle = 1) {
	sleep 500
	Send, {Alt Down}{Tab}{Alt Up}
	}
	Return
}
