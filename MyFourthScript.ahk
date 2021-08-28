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
	
!x:: ; ALT-X
	WinGet, winid ,, A ; <-- need to identify window A = acitive
	SetTitleMatchMode, RegEx
	WinActivate event-drops
	Send, catch{Enter}
	sleep 120 ;
	WinActivate ahk_id %winid%
	return
		
