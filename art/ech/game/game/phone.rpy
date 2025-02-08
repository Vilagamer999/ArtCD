
screen use_phone():
    tag menu
    frame:
        background "ui/phone/blackscreen.png"
        add "ui/phone/message_chase.png" at phone_pickup
        use home_page()
        #if date == 0
    use phone_switch()


screen phone_message():
    tag menu
    frame:
        background "ui/phone/blackscreen.png"
        add "ui/phone/messages_chase.png" at phone_pickup
        #if route progress == 0:
        use message_panel()
    #imagebutton:
     #   idle "ui/phone/icon_on.png"
      #  hover "ui/phone/icon_off.png"
       # action [Return()]

screen home():
    imagebutton:
        xalign 0.5 yalign 0.5
        yoffset 328
        idle "ui/phone/home.png" 
        action [ShowMenu("home_page"), Hide("ad"), Hide("date_chat"), Hide("date_ui2")]

################################################################

screen message_panel():
    tag phone_screen
    modal True
    use phone_switch()
    imagebutton auto "ui/phone/thumb_carl_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "carl")] at message_1
    imagebutton auto "ui/phone/thumb_tj_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "tj")] at message_2
    imagebutton auto "ui/phone/thumb_flynn_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "flynn")] at message_3
    imagebutton auto "ui/phone/thumb_jenna_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "jenna")] at message_4
    imagebutton auto "ui/phone/thumb_leo_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "leo")] at message_5
    imagebutton auto "ui/phone/thumb_mom_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "mom")] at message_6
    imagebutton auto "ui/phone/thumb_vincent_%s.png" action [ShowMenu("chat_content"), SetVariable("chat_who", "vincent")] at message_7
    textbutton "Otters have three holes" action None style "recent_text" text_style "recent_text_button_text" at text_1
    textbutton "Chase, what does twink mean?" action None style "recent_text" text_style "recent_text_button_text" at text_2
    textbutton "Wash your musky ass" action None style "recent_text" text_style "recent_text_button_text" at text_3
    textbutton "chase_spider.mp4" action None style "recent_text" text_style "recent_text_button_text" at text_4
    textbutton "Do you still remember that time..." action None style "recent_text" text_style "recent_text_button_text" at text_5
    textbutton "Wash your underwear" action None style "recent_text" text_style "recent_text_button_text" at text_6
    textbutton "Who am I again?" action None style "recent_text" text_style "recent_text_button_text" at text_7


screen chatlog(scroll=None, yinitial=0.0):
    frame:
        style "chatlog_frame"
        if scroll == "viewport":
            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    transclude
        elif scroll == "vpgrid":
            vpgrid:
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_yfill True
                transclude
        else:
            transclude

screen chat_content_origin():
    tag phone_screen
    if chat_who == "carl":
        add "ui/phone/banner/banner_carl.png" xpos 348 ypos 78
    elif chat_who == "tj":
        add "ui/phone/banner/banner_tj.png" xpos 348 ypos 78
    elif chat_who == "flynn":
        add "ui/phone/banner/banner_flynn.png" xpos 348 ypos 78
    elif chat_who == "jenna":
        add "ui/phone/banner/banner_jenna.png" xpos 348 ypos 78
    elif chat_who == "leo":
        add "ui/phone/banner/banner_leo.png" xpos 348 ypos 78
    elif chat_who == "mom":
        add "ui/phone/banner/banner_mom.png" xpos 348 ypos 78
    elif chat_who == "vincent":
        add "ui/phone/banner/banner_vincent.png" xpos 348 ypos 78
    use chatlog(scroll="viewport"):
        vbox:
            if chat_who == "carl":
                add "ui/phone/testchat2.png"
            else:
                add "ui/phone/testchat.png"
    imagebutton:
        xpos 360 ypos 90
        idle "ui/phone/return.png" 
        action [Hide("chat_content")]

screen chat_content(who):
    tag phone_screen
    if who == "carl":
        add "ui/phone/banner/banner_carl.png" xpos 348 ypos 78
    elif who == "tj":
        add "ui/phone/banner/banner_tj.png" xpos 348 ypos 78
    elif who == "flynn":
        add "ui/phone/banner/banner_flynn.png" xpos 348 ypos 78
    elif who == "jenna":
        add "ui/phone/banner/banner_jenna.png" xpos 348 ypos 78
    elif who == "leo":
        add "ui/phone/banner/banner_leo.png" xpos 348 ypos 78
    elif who == "mom":
        add "ui/phone/banner/banner_mom.png" xpos 348 ypos 78
    elif who == "vincent":
        add "ui/phone/banner/banner_vincent.png" xpos 348 ypos 78

############ home screen ###############

screen phone_switch():
    tag phone_switch
    imagebutton:
        idle "ui/phone/icon_on.png"
        hover "ui/phone/icon_off.png"
        action [ShowMenu("phone_off"), Hide("use_phone"), Hide("date_chat"), Hide("ad")]

screen home_page():
    tag phone_screen
    use extra_menu()
    add "ui/phone/home_screen.png" #at phone_on

    imagebutton auto "ui/phone/predater/icon_%s.png" action [ShowMenu("predater")] at app_4
    imagebutton:
        idle "ui/phone/weather_idle.png" at app_1
        action None 
    imagebutton:
        idle "ui/phone/map_idle.png" at app_2
        action None 
    imagebutton:
        idle "ui/phone/alarm_idle.png" at app_3
        action None 
    imagebutton: 
        idle "ui/phone/call_idle.png" at app_5
        action None 
    imagebutton auto "ui/phone/message_%s.png" action [Return()] at app_6

screen phone_off():
    tag phone_screen
    frame:
        background "ui/phone/blackscreen.png"
        add "ui/phone/phone_chase.png" at phone_hide
    timer 1.2 action [Return()]

############ predater #################
screen predater():
    tag phone_screen
    use extra_menu()
    add "ui/phone/predater/banner.png" at user_page
    use user_page(scroll="viewport"):
        use profiles()
    add "ui/phone/predater/login_2.png" at login_2
    add "ui/phone/predater/login_1.png" at login
    use home()

screen predater2():
    tag phone_screen
    use extra_menu()
    add "ui/phone/predater/banner.png" xpos 340 ypos 78
    use user_page(scroll="viewport"):
        use profiles()
    use home()


screen user_page(scroll=None, yinitial=0.0):
    frame:
        style "user_page"
        if scroll == "viewport":
            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    transclude
        elif scroll == "vpgrid":
            vpgrid:
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_yfill True
                transclude
        else:
            transclude

screen profiles():
    tag phone_screen
    grid 3 6 :
        style_prefix "pslot"
        xalign 0.5
        yalign 0.5
        xoffset 26 yoffset 6
        spacing gui.slot_spacing
        imagebutton:
            idle "ui/phone/predater/icon/unk2_idle.png"
            hover "ui/phone/predater/icon/unk2_hover.png"
            action [ShowMenu("bio"), SetVariable("bio_who", "0")]
        imagebutton:
            idle "ui/phone/predater/icon/4_idle.png" 
            hover "ui/phone/predater/icon/4_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "4")]
        imagebutton:
            idle "ui/phone/predater/icon/5_idle.png" 
            hover "ui/phone/predater/icon/5_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "5")]
        imagebutton:
            idle "ui/phone/predater/icon/unk2_idle.png" 
            hover "ui/phone/predater/icon/unk2_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "6")]
        imagebutton:
            idle "ui/phone/predater/icon/unk3_idle.png"
            hover "ui/phone/predater/icon/unk3_hover.png"  
            action [ShowMenu("bio"), SetVariable("bio_who", "7")]
        imagebutton:
            idle "ui/phone/predater/icon/8_idle.png"
            hover "ui/phone/predater/icon/8_hover.png"  
            action [ShowMenu("bio"), SetVariable("bio_who", "8")]
        imagebutton:
            idle "ui/phone/predater/icon/9_idle.png" 
            hover "ui/phone/predater/icon/9_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "9")]
        imagebutton:
            idle "ui/phone/predater/icon/unk1_idle.png" 
            hover "ui/phone/predater/icon/unk1_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "10")]
        imagebutton:
            idle "ui/phone/predater/icon/unk1_idle.png" 
            hover "ui/phone/predater/icon/unk1_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "11")]
        imagebutton:
            idle "ui/phone/predater/icon/unk1_idle.png" 
            hover "ui/phone/predater/icon/unk1_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "12")]
        imagebutton:
            idle "ui/phone/predater/icon/13_idle.png" 
            hover "ui/phone/predater/icon/13_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "13")]
        imagebutton:
            idle "ui/phone/predater/icon/unk2_idle.png" 
            hover "ui/phone/predater/icon/unk2_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "14")]
        imagebutton:
            idle "ui/phone/predater/icon/unk1_idle.png" 
            hover "ui/phone/predater/icon/unk1_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "15")]
        imagebutton:
            idle "ui/phone/predater/icon/unk2_idle.png" 
            hover "ui/phone/predater/icon/unk2_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "16")]
        imagebutton:
            idle "ui/phone/predater/icon/17_idle.png" 
            hover "ui/phone/predater/icon/17_hover.png" 
            action [ShowMenu("bio"), SetVariable("bio_who", "17")]
        null
        null
        null

    add "ui/phone/predater/ad_apex.png" xoffset 26 yoffset -80

screen bio():
    tag phone_screen
    use extra_menu()
    if bio_who == "0":
        add "ui/phone/predater/bio/0.png" xpos 340 ypos 78
    elif bio_who == "4":
        add "ui/phone/predater/bio/4.png" xpos 340 ypos 78
    elif bio_who == "5":
        add "ui/phone/predater/bio/5.png" xpos 340 ypos 78
    elif bio_who == "6":
        add "ui/phone/predater/bio/6.png" xpos 340 ypos 78
    elif bio_who == "7":
        add "ui/phone/predater/bio/7.png" xpos 340 ypos 78
    elif bio_who == "8":
        add "ui/phone/predater/bio/8.png" xpos 340 ypos 78
    elif bio_who == "9":
        add "ui/phone/predater/bio/9.png" xpos 340 ypos 78
    elif bio_who == "10":
        add "ui/phone/predater/bio/10.png" xpos 340 ypos 78
    elif bio_who == "11":
        add "ui/phone/predater/bio/11.png" xpos 340 ypos 78
    elif bio_who == "12":
        add "ui/phone/predater/bio/12.png" xpos 340 ypos 78
    elif bio_who == "13":
        add "ui/phone/predater/bio/13.png" xpos 340 ypos 78
    elif bio_who == "14":
        add "ui/phone/predater/bio/14.png" xpos 340 ypos 78
    elif bio_who == "15":
        add "ui/phone/predater/bio/15.png" xpos 340 ypos 78
    elif bio_who == "16":
        add "ui/phone/predater/bio/16.png" xpos 340 ypos 78
    elif bio_who == "17":
        add "ui/phone/predater/bio/17.png" xpos 340 ypos 78
    use date_ui()
    use home()


screen date_ui():
    tag ui
    imagebutton:
        xpos 316 ypos 53
        idle "ui/phone/predater/bio/none.png" 
        hover "ui/phone/predater/bio/return.png" 
        action [ShowMenu("predater2"), Hide("date_ui"), Hide("date_ui2")] 

    imagebutton:
       xpos 586 ypos 261
       idle "ui/phone/predater/bio/none.png" 
       hover "ui/phone/predater/bio/chat.png" 
       action [ShowMenu("date_chat")]

    imagebutton:
       xpos 586 ypos 323
       idle "ui/phone/predater/bio/none.png" 
       hover "ui/phone/predater/bio/fav.png" 
       action [ShowMenu("date_ui2")]

    imagebutton:
       xpos 586 ypos 392
       idle "ui/phone/predater/bio/none.png" 
       hover "ui/phone/predater/bio/block.png" 
       action [ShowMenu("ad"), SetVariable("ad_what", "2")]

screen date_ui2():
    tag ui
    imagebutton:
        xpos 316 ypos 53
        idle "ui/phone/predater/bio/none.png" 
        hover "ui/phone/predater/bio/return.png" 
        action [ShowMenu("predater2"), Hide("date_ui"), Hide("date_ui2")] 

    imagebutton:
       xpos 586 ypos 261
       idle "ui/phone/predater/bio/none.png" 
       hover "ui/phone/predater/bio/chat.png" 
       action [ShowMenu("date_chat")]

    imagebutton:
       xpos 586 ypos 323
       idle "ui/phone/predater/bio/fav-ed.png" 
       action [ShowMenu("ad"), SetVariable("ad_what", "1")]

    imagebutton:
       xpos 586 ypos 392
       idle "ui/phone/predater/bio/none.png" 
       hover "ui/phone/predater/bio/block.png" 
       action [ShowMenu("ad"), SetVariable("ad_what", "2")]

screen date_chat():
    tag phone_ad
    modal True
    #use phone_switch()
    use home()
    if bio_who == "11":
        add "ui/phone/predater/chat_1.png" xpos 340 ypos 78
    elif bio_who == "6":
        add "ui/phone/predater/chat_2.png" xpos 340 ypos 78
    else:
        add "ui/phone/predater/chat.png" xpos 340 ypos 78

    imagebutton:
        xpos 316 ypos 53
        idle "ui/phone/predater/bio/return_idle.png" 
        hover "ui/phone/predater/bio/return.png" 
        action [Hide("date_chat")] 

screen ad():
    tag phone_ad
    modal True
    if ad_what == "1":
        add "ui/phone/predater/ad_fav.png" xpos 340 ypos 78
    elif ad_what == "2":
        add "ui/phone/predater/ad_block.png" xpos 340 ypos 78
    timer 4 action [Hide("ad")]


style pslot:
    xsize 99
    ysize 99