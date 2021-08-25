#InstallKeybdHook
#UseHook On

Toggle := 0

!1:: ; ALT-1
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	Toggle ^= 1
Return




; Q = HUNT
; W = FISH/CHOP/AXE/PICKAXE
; E = TRAINING
; Y = Y/YES
; I = I/INVENTORY
; P = P/PROFILE

!q:: ; ALT-Q
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HUNT T {Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HUNT T {Enter} 	
	}
	Return

XButton2::
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HUNT T {Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HUNT T {Enter} 	
	}
	Return

!w:: ; ALT-W
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CHAINSAW{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CHAINSAW{Enter} 	
	}
	Return

XButton1::
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CHAINSAW{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CHAINSAW{Enter} 	
	}
	Return


!e:: ; ALT-E
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG TRAINING {Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG TRAINING {Enter} 	
	}
	Return

!y:: ; ALT-Y
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, Y{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, Y{Enter} 	
	}
	Return

!i:: ; ALT-I
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG I{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG I{Enter} 	
	}
	Return


!p:: ; ALT-P
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG P{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG P{Enter} 	
	}
	Return


; A = ADV/ADVENTURE
; D = RD/READY
; F = FARM/FARM CARROT/FARM POTATO
; H = HEAL
; J = JOIN

!a:: ; ALT-A
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG ADVENTURE{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG ADVENTURE{Enter} 	
	}
	Return

!d:: ; ALT-D
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG RD{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG RD{Enter} 	
	}
	Return

!f:: ; ALT-F
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG FARM{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG FARM{Enter} 	
	}
	Return

!h:: ; ALT-H
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HEAL{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG HEAL{Enter} 	
	}
	Return

!j:: ; ALT-j
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, JOIN{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, JOIN{Enter} 	
	}
	Return


; Z = FIGHT
; C = CD/COLDOWN
; B = BUY ED LB
; N = NO

!z:: ; ALT-Z
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, FIGHT{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, FIGHT{Enter} 	
	}
	Return

!c:: ; ALT-C
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CD{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG CD{Enter} 	
	}
	Return

!b:: ; ALT-B
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG BUY ED LB{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG BUY ED LB{Enter} 	
	}
	Return

!n:: ; ALT-N
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, N{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, N{Enter} 	
	}
	Return
