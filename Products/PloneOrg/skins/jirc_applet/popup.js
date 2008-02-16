function popupChat() {
        win=window.open("demo4.html", "JPilotChat",
                   "resizable=no,height=220,width=520");
}     


function send()
{
   if (document.UserInfo.NICKNAME.value == null ||
                                        document.UserInfo.NICKNAME.value == "")
   {
        window.alert("You must enter your nick name.")
        return false
   }

 var USERNICK = document.UserInfo.NICKNAME.value

 win=window.open("","IRC","resizable=no,height=320,width=500")
 win.document.write('<html><head><title>JPilot jIRC Chat</title></head>')
 win.document.write('<body bgcolor="#C0C0C0">')

win.document.write('<applet codebase="classes" archive="jirc_nss.zip,resources.zip" code="Chat.class" width=490 height=300 MAYSCRIPT >')         

win.document.write('<param name="CABBASE" value="jirc_mss.cab,resources.cab">')

win.document.write('<param name="DirectStart" value="true">')

win.document.write('<param name="FilterKeys" value=":) :( :D :P ;) :confused: :mad: :cool: ;( :love: :thumbup: :thumbdown: :evil: :kiss: :hello: :applause: :banghead: :bye:">')
win.document.write('<param name="FilterVals" value="smile.gif frown.gif biggrin.gif tongue.gif wink.gif confused.gif mad.gif cool.gif evil.gif love.gif thumbup.gif thumbdown.gif evil.gif kiss.gif hello.gif applause.gif banghead.gif bye.gif">')

win.document.write('<param name="HostName" value="jpilot" >')

win.document.write('<param name="UseModeIcons" value="true">')
win.document.write('<param name="TimeStampFormat" value="hh:mm a" >')
win.document.write('<param name="AllowTimeStamp" value="true">')

win.document.write('<param name="UserProfileURL" value="http://www.jpilot.com/cgi-bin/products/jirc/viewprofile.cgi?nick" >')

win.document.write('<param name="FieldNameProfileButton" value="View profile">')
win.document.write('<param name="FieldNameChannelJoined" value="just entered the chat room" >')
win.document.write('<param name="FieldNameChannelLeft" value="just left the chat room" >')
win.document.write('<param name="FieldNameChannelLeft" value="You just left the chat room" >')
win.document.write('<param name="FieldNameNickNotify" value="has changed his/her nickname to">')
win.document.write('<param name="FieldNamePrivateIgnore" value="Ignore This User">')
win.document.write('<param name="FieldNameConnecting" value="Connecting to the server, please wait ....">')
win.document.write('<param name="FieldNameConnected" value="Connected to server, sending login information ...">')
win.document.write('<param name="FieldNameConnectionClose" value="Connection to server closed.">')
win.document.write('<param name="FieldNameQuitMsg" value="Bye bye">')
win.document.write('<param name="FieldNamePrivateClose" value="Close">')
win.document.write('<param name="FieldNamePrivateChatTitle" value="Private Chat with: ">')
win.document.write('<param name="WelcomeMessage" value="Welcome to Java IRC chat!">')
win.document.write('<param name="RealName" value="JPilot jIRC applet user">')
win.document.write('<param name="NickName" value="'+USERNICK+'">')
win.document.write('<param name="UserName" value="jirc">')
win.document.write('<param name="IgnoreUser" value="ignore user : ">')
win.document.write('<param name="ActivateUser" value="activate  user : ">')

win.document.write('<param name="UserCmdColor" value="yellow">')
win.document.write('<param name="BackgroundColor" value="119,124,170">')
win.document.write('<param name="TextColor" value="white">')
win.document.write('<param name="TextScreenColor" value="black">')
win.document.write('<param name="ListTextColor" value="white">')
win.document.write('<param name="ListScreenColor" value="50,50,100">')
win.document.write('<param name="LogoBorderColor" value="black">')
win.document.write('<param name="ConfigBorderColor" value="204,153,51">')
win.document.write('<param name="LogoBgColor" value="white">')
win.document.write('<param name="TitleForegroundColor" value="white">')
win.document.write('<param name="TitleBackgroundColor" value="black">')
win.document.write('<param name="TextFontSize" value="12">')
win.document.write('<param name="TextFontName" value="Arial">')
win.document.write('<param name="FGColor" value="black">')
win.document.write('<param name="InputTextColor" value="black">')
win.document.write('<param name="InputScreenwhiteColor" value="white">')



win.document.write('<param name="AllowJoinSound" value="true" >')
win.document.write('<param name="AllowLeaveSound" value="true">')
win.document.write('<param name="LogoGifName" value="IRClogo.gif">')
win.document.write('<param name="RefreshColorCode" value="false">')
win.document.write('<param name="SoundMsg" value="Play Sound">')
win.document.write('<param name="NickNameColor" value="6">')
win.document.write('<param name="NickMaskStart" value="">')
win.document.write('<param name="NickMaskEnd" value=":">')

win.document.write('<param name="PWindowHeight" value="250">')
win.document.write('<param name="PWindowWidth" value="400">')
win.document.write('<param name="BorderSpacing" value="0">')
win.document.write('<param name="BorderVsp" value="3">')

win.document.write('<param name="IgnoreMOTD" value="true">')
win.document.write('<param name="IgnoreModeMsg" value="true">')
win.document.write('<param name="IgnoreServerMsg" value="true">')
win.document.write('<param name="IgnoreCode" value="5" >')


win.document.write('<param name="ServerPort" value="6667">')
win.document.write('<param name="ServerName1" value="irc.jpilot.com">')
win.document.write('<param name="ServerName2" value="irc.prison.net">')
win.document.write('<param name="Channel1" value="jpilot">')
win.document.write('<param name="Channel2" value="finance">')
win.document.write('<param name="Channel3" value="lobby">')
win.document.write('<param name="Channel4" value="science">')
win.document.write('<param name="Channel5" value="movies">')
win.document.write('<param name="Channel6" value="jpilot">')
win.document.write('<param name="Channel8" value="fun">')
win.document.write('<param name="Channel7" value="chat">')

win.document.write('<param name="AllowShowURL" value="true">')
win.document.write('<param name="AllowIdentd" value="true">')

	win.document.close()
	return true
}
