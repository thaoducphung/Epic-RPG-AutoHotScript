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
		SendInput, RPG hunt{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG hunt{Enter} 	
	}
	Return

; XButton2::
; 	If (Toggle = 1) {
; 		WinGet, winid ,, A ; <-- need to identify window A = acitive
; 		WinActivate, ahk_exe Discord.exe
; 		SendInput, RPG hunt{Enter} 	
; 		sleep 120 ;
; 		WinActivate ahk_id %winid%
; 	} else {
; 		WinActivate, ahk_exe Discord.exe
; 		SendInput, RPG hunt{Enter} 	
; 	}
; 	Return

!w:: ; ALT-W
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG fish{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG fish{Enter} 	
	}
	Return

; XButton1::
; 	If (Toggle = 1) {
; 		WinGet, winid ,, A ; <-- need to identify window A = acitive
; 		WinActivate, ahk_exe Discord.exe
; 		SendInput, RPG fish{Enter} 	
; 		sleep 120 ;
; 		WinActivate ahk_id %winid%
; 	} else {
; 		WinActivate, ahk_exe Discord.exe
; 		SendInput, RPG fish{Enter} 	
; 	}
; 	Return

XButton2::
	WinGet, winid ,, A ; <-- need to identify window A = acitive
	SetTitleMatchMode, RegEx
	WinActivate event-drops
	Send, fish{Enter}
	sleep 120 ;
	WinActivate ahk_id %winid%
	return
	
XButton1::
	WinGet, winid ,, A ; <-- need to identify window A = acitive
	SetTitleMatchMode, RegEx
	WinActivate event-drops
	Send, chop{Enter}
	sleep 120 ;
	WinActivate ahk_id %winid%
	return

!e:: ; ALT-E
KeyWait Control, L  ; Wait for both Control and Alt to be released.
KeyWait Alt, L  ; Wait for both Control and Alt to be released.
	If (Toggle = 1) {
		WinGet, winid ,, A ; <-- need to identify window A = acitive
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG tr{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG tr{Enter} 	
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
		SendInput, RPG P S{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG P S{Enter} 	
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
		SendInput, RPG farm carrot{Enter} 	
		sleep 120 ;
		WinActivate ahk_id %winid%
	} else {
		WinActivate, ahk_exe Discord.exe
		SendInput, RPG farm carrot{Enter} 	
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
; X = catch using mouse special
; C = CD/COLDOWN
; B = BUY ED LB
; N = NO

!z:: ; ALT-Z
WinGet, winid ,, A ; <-- need to identify window A = acitive
	SetTitleMatchMode, RegEx
	WinActivate arena
	Send, join{Enter}
	sleep 120 ;
	WinActivate ahk_id %winid%
	return

!x:: ; ALT-X
	WinGet, winid ,, A ; <-- need to identify window A = acitive
	SetTitleMatchMode, RegEx
	WinActivate event-drops
	Send, catch{Enter}
	sleep 120 ;
	WinActivate ahk_id %winid%
	return
	
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
