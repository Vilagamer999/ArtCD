#### EXTRA SCREENS
#This script is based on https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=50040 extras gallery by gas.

## The audio player on top of the screen ########################################
screen mp3():
    frame:
        xpos 12
        background None
        hbox:
            spacing 5
            imagebutton auto "ui/gallery/mp3_previous_%s.png" action [
                        Play ("ex_sfx", "sfx/click.wav"),
                        mr.Previous(),
                        renpy.restart_interaction]
            imagebutton auto "ui/gallery/mp3_play_%s.png" action [
                        Play ("ex_sfx", "sfx/click.wav"),
                        mr.Play(),
                        renpy.restart_interaction]
            imagebutton auto "ui/gallery/mp3_stop_%s.png" action [
                        Play ("ex_sfx", "sfx/click.wav"),
                        mr.Stop()]
            imagebutton auto "ui/gallery/mp3_next_%s.png" action [
                        Play ("ex_sfx", "sfx/click.wav"),
                        mr.Next(),
                        renpy.restart_interaction]
            #imagebutton auto "ui/gallery/mp3_random_%s.png" action [
             #           Play ("ex_sfx", "sfx/click.wav"),
              #          mr.RandomPlay(),
               #         renpy.restart_interaction]
            #frame:
             #   background None
              #  xpos 308
               # xalign 0.5
                #ypos 6
                #$ titletrack=renpy.music.get_playing()
                #if titletrack:
                 #   $ titletrack=titletrack[:len(titletrack)-4]
                  #  $ titletrack=titletrack.replace("_"," ")
                    #$ titletrack=titletrack.title()
                   # text "{size=+15}{font=ui/gallery/28 days later.ttf}[titletrack]" xalign 0 size 30
                #else:
                 #   null

## EXTRA Menu screen ############################################################
screen exgame_menu(scroll=None, yinitial=0.0):
    window:
        style "gallery_bg_window"
    frame:
        style "game_menu_content_frame"
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



    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    use mp3
    #add "godray"

image godray:
    "ui/gallery/godray1.png" with Dissolve(1.5, alpha=True)
    pause 2.0
    "ui/gallery/godray2.png" with Dissolve(1.5, alpha=True)
    pause 2.0
    "ui/gallery/godray3.png" with Dissolve(1.5, alpha=True)
    pause 2.0

    repeat
###################################
screen extra_ui():

    add "ui/gallery/lakebottom_1.png" xalign 0.5 yalign 1

    imagebutton:
        xpos -10 ypos 620
        idle "ui/gallery/return_idle.png"
        action [Play ("menu_sfx", "splash.mp3"), mr.Play("theme.ogg"), Return(), With(fade)]

    imagebutton:
        xpos 860 ypos 460
        idle "ui/gallery/window0.png"
        hover "window_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("scenegallery"), With(dissolve)]

    imagebutton:
        xpos 550 ypos 595
        idle "ui/gallery/letter0.png"
        hover "letter_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("imagegallery"), With(dissolve)]

    add "ui/gallery/lakebottom_2.png" xalign 0.5 yalign

    imagebutton:
        xpos 330 ypos 690
        idle "ui/gallery/music_idle.png"
        ##hover "music_hover"
        action [Play ("menu_sfx", "popper.ogg"), ShowMenu("music_room"), With(dissolve)]

    add "godray"

screen extra_ui_1():

    add "ui/gallery/lakebottom_1.png" xalign 0.5 yalign 1

    imagebutton:
        xpos -10 ypos 620
        idle "ui/gallery/return_idle.png"
        action [Play ("menu_sfx", "splash.mp3"), mr.Play("theme.ogg"), Return(), With(fade)]

    imagebutton:
        xpos 890 ypos 470
        idle "ui/gallery/window0.png"
        hover "window_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("scenegallery"), With(dissolve)]

    imagebutton:
        xpos 550 ypos 595
        idle "ui/gallery/letter0.png"
        hover "letter_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("imagegallery"), With(dissolve)]

    add "ui/gallery/lakebottom_2.png" xalign 0.5 yalign

    add "godray"

screen extra_ui_2():

    add "ui/gallery/lakebottom_1.png" xalign 0.5 yalign 1

    imagebutton:
        xpos -10 ypos 620
        idle "ui/gallery/return_idle.png"
        action [Play ("menu_sfx", "splash.mp3"), mr.Play("theme.ogg"), Return(), With(fade)]

    imagebutton:
        xpos 890 ypos 470
        idle "ui/gallery/window0.png"
        hover "window_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("scenegallery"), With(dissolve)]

    add "ui/gallery/lakebottom_2.png" xalign 0.5 yalign

    imagebutton:
        xpos 330 ypos 690
        idle "ui/gallery/music_idle.png"
        ##hover "music_hover"
        action [Play ("menu_sfx", "popper.ogg"), ShowMenu("music_room"), With(dissolve)]

    add "godray"

screen extra_ui_3():

    add "ui/gallery/lakebottom_1.png" xalign 0.5 yalign 1

    imagebutton:
        xpos -10 ypos 620
        idle "ui/gallery/return_idle.png"
        action [Play ("menu_sfx", "splash.mp3"), mr.Play("theme.ogg"), Return(), With(fade)]

    imagebutton:
        xpos 550 ypos 595
        idle "ui/gallery/letter0.png"
        hover "letter_hover"
        action [Play ("menu_sfx", "static.ogg"), ShowMenu("imagegallery"), With(dissolve)]

    add "ui/gallery/lakebottom_2.png" xalign 0.5 yalign

    imagebutton:
        xpos 330 ypos 690
        idle "ui/gallery/music_idle.png"
        ##hover "music_hover"
        action [Play ("menu_sfx", "popper.ogg"), ShowMenu("music_room"), With(dissolve)]

    add "godray"

#############################################
image window_hover:
    "ui/gallery/window0.png" with Dissolve(1.5, alpha=True)
    pause 3.0
    "ui/gallery/window1.png" with Dissolve(1.5, alpha=True)
    pause 3.0
    "ui/gallery/window2.png" with Dissolve(1.5, alpha=True)
    pause 3.0
    "ui/gallery/window3.png" with Dissolve(1.5, alpha=True)
    pause 6.0
    "ui/gallery/window4.png" with Dissolve(1.5, alpha=True)
    pause 3.0
    "ui/gallery/window5.png" with Dissolve(1.5, alpha=True)
    pause 3.0
    repeat

image letter_hover:
    "ui/gallery/letter1.png"
    pause 1.0
    "ui/gallery/letter2.png"
    pause 1.0
    repeat

### IMAGE GALLERY! ##########################################
init python:
    g = Gallery()

    #common

    g.button("cg_gallery01")
    g.unlock_image("groupphoto")

    g.button("cg_gallery02")
    g.unlock_image("apology")

    g.button("cg_gallery03")
    g.unlock_image("chaseswim")

    g.button("cg_gallery04")
    g.unlock_image("argument")

    #carl

    g.button("cg_gallery05")
    g.unlock_image("carltree")

    g.button("cg_gallery06")
    g.unlock_image("bg carlechobeanbag")

    g.button("cg_gallery07")
    g.unlock_image("sheets")

    g.button("cg_gallery08")
    g.unlock_image("image08")

    #leo

    g.button("cg_gallery09")
    g.unlock_image("leoandchase")

    g.button("cg_gallery10")
    g.unlock_image("bg chaseleostadium")

    g.button("cg_gallery11")
    g.unlock_image("bg ChaseEmbrace")
    g.unlock_image("bg ChaseDay1")
    #g.unlock_image("bg ChaseDay2")
    g.unlock_image("bg ChaseDay3")
    #g.unlock_image("bg ChaseDay4")
    g.unlock_image("bg ChaseNight1")
    g.unlock_image("bg ChaseNight2")
    #g.unlock_image("bg ChaseNight3")
    g.unlock_image("bg ChaseNight4")

    g.button("cg_gallery12")
    g.unlock_image("bg Justice")

    #tj

    g.button("cg_gallery13")
    g.unlock_image("bg hike")

    g.button("cg_gallery14")
    g.unlock_image("mirror")

    g.button("cg_gallery15")
    g.unlock_image("bg kiss")

    g.button("cg_gallery16")
    g.unlock_image("sunsetlake")

    #flynn

    g.button("cg_gallery17")
    g.unlock_image("bg SmokeRoom1")
    g.unlock_image("bg SmokeRoom2")
    g.unlock_image("bg SmokeRoom3")
    g.unlock_image("bg SmokeRoom4")
    #g.unlock_image("bg SmokeRoom5")

    g.button("cg_gallery18")
    g.unlock_image("bg lookhowtheymassacredmyboar")

    g.button("cg_gallery19")
    g.unlock_image("bg hill_small")
    g.unlock_image("bg hill_monster_small")


    g.button("cg_gallery20")
    g.unlock_image("bg areyoureal")



    g.button("cg_gallery23")
    g.unlock_image("bg ChaseSpiderTarantula")
    g.unlock_image("bg ChaseSpiderWidow")

    g.button("cg_gallery24")
    g.unlock_image("bg Muerte1")
    g.unlock_image("Muerte2")

    #jenna

    g.button("cg_gallery21")
    g.unlock_image("bg nightwalk")

    g.button("cg_gallery22")
    g.unlock_image("backlitvan")

    g.button("cg_gallery25")
    g.unlock_image("bg kandb")



    #other


    #g.button("cg_gallery26")
    #g.unlock_image("keithframe")

    #g.button("cg_gallery27")
    #g.unlock_image("chasealone")
    #g.unlock_image("chaseleo1")
    #g.unlock_image("chaseleo2")

    g.locked_button=("images/thumbnails/locked.png")

    g.transition = dissolve

image com_0:
    "Cover.png"
    zoom 0.2

image com_1:
    "groupphoto.png"
    zoom 0.2

image com_2:
    "apology.png"
    zoom 0.2

image com_3:
    "chaseswim.png"
    zoom 0.2

image com_4:
    "argument.png"
    zoom 0.2

#############################
image carl_1:
    "carltree.png"
    zoom 0.2

image carl_2:
    "carlechobeanbag.png"
    zoom 0.2

image carl_3:
    "sheets.png"
    zoom 0.2

#############################
image leo_1:
    "leoandchase.png"
    zoom 0.2

image leo_2:
    "stadium.png"
    zoom 0.2

image leo_3:
    "chaseday1.png"
    zoom 0.2
    randompause(10,20)
    "chaseembrace.png"
    zoom 0.2

image leo_3b:
    "chaseembrace.png"
    zoom 0.2

#https://lemmasoft.renai.us/forums/viewtopic.php?t=10781
init python:
    def randompause(min,max):
        return renpy.random.randint(min,max)

image leo_4:
    "Justice.jpg"
    zoom 0.2

#############################
image tj_1:
    "Hike.png"
    zoom 0.2

image tj_2:
    "mirror.png"
    zoom 0.2

image tj_3:
    "Kiss.png"
    zoom 0.2

image tj_4:
    "sunsetlake.png"
    zoom 0.2

#############################
image flynn_1:
    "SmokeRoom1.png"
    zoom 0.2

image flynn_2:
    "lookhowtheymassacredmyboar.png"
    zoom 0.2

image flynn_3:
    "hill_small.png"
    zoom 0.2

image flynn_4:
    "AreYouReal.png"
    zoom 0.2

image flynn_5:
    "ChaseSpiderTarantula.jpg"
    zoom 0.2

image flynn_6:
    "Muerte1.jpg"
    zoom 0.2

#############################
image jenna_1:
    "nightwalk.png"
    zoom 0.2

image jenna_2:
    "backlitvan.png"
    zoom 0.2

image jenna_3:
    "kandb.jpg"
    zoom 0.2

#############################

screen imagegallery():
    tag menu
    use exgame_menu(scroll="viewport"):
        grid 4 10 :
            style_prefix "gslot"
            xalign 0.5
            yalign 0.5
            spacing gui.slut_spacing

            #common
            null
            add g.make_button("cg_gallery01","com_1", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery02","com_2", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery03","com_3", xpadding = 0, ypadding = 0)

            null
            add g.make_button("cg_gallery04","com_4", xpadding = 0, ypadding = 0)
            null
            null

            #carl
            add "images/thumbnails/carl.png"
            add g.make_button("cg_gallery05","carl_1", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery06","carl_2", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery07","carl_3", xpadding = 0, ypadding = 0)

            #leo
            add "images/thumbnails/leo.png"
            add g.make_button("cg_gallery09","leo_1",  xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery10","leo_2",  xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery11","leo_3", xpadding = 0, ypadding = 0)

            null
            add g.make_button("cg_gallery12","leo_4",  xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery19","flynn_3", xpadding = 0, ypadding = 0)
            null

            #tj
            add "images/thumbnails/tj.png"
            add g.make_button("cg_gallery13","tj_1", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery14","tj_2", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery15","tj_3", xpadding = 0, ypadding = 0)

            null
            add g.make_button("cg_gallery16","tj_4", xpadding = 0, ypadding = 0)
            null
            null

            #flynn
            add "images/thumbnails/flynn.png"
            add g.make_button("cg_gallery17","flynn_1", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery23","flynn_5", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery18","flynn_2", xpadding = 0, ypadding = 0)

            null
            add g.make_button("cg_gallery24","flynn_6", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery20","flynn_4", xpadding = 0, ypadding = 0)
            null

            #jenna
            add "images/thumbnails/jenna.png"
            add g.make_button("cg_gallery21","jenna_1", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery22","jenna_2", xpadding = 0, ypadding = 0)
            add g.make_button("cg_gallery25","jenna_3", xpadding = 0, ypadding = 0)

            #add g.make_button("cg_gallery25","com_0", xpadding = 0, ypadding = 0)
            #add g.make_button("cg_gallery26","images/thumbnails/hand_2.png", xpadding = 0, ypadding = 0)
            #add g.make_button("cg_gallery27","images/thumbnails/hand_1.png", xpadding = 0, ypadding = 0)
            #null

    use extra_ui_2

style gslot:
    xsize 205
    ysize 154

define gui.slut_spacing = 10
define gui.slut2_spacing = 11.7

### SCENE GALLERY! ##########################################
image what_saturday:
    "Saturday1.png"
    zoom 0.2

image all_sunday:
    "Sunday.png"
    zoom 0.2

image all_monday:
    "monday1.png"
    zoom 0.2

image all_tuesday:
    "tuesday.png"
    zoom 0.2

image all_wednesday:
    "allwednesday.png"
    zoom 0.2

image all_thursday:
    "thursday.png"
    zoom 0.2

image all_friday:
    "friday.png"
    zoom 0.2

image all_saturday:
    "saturday.png"
    zoom 0.2

##########################
image carl_tuesday:
    "carltuesday.png"
    zoom 0.2

image carl_saturday:
    "saturdaycarl2.png"
    zoom 0.2

image carl_sunday:
    "sundaycarl2.png"
    zoom 0.2

##########################
image leo_friday:
    "fridayleo2.png"
    zoom 0.2

image leo_sunday:
    "sundayleo2.png"
    zoom 0.2

##########################
image tj_tuesday:
    "tjtuesday.png"
    zoom 0.2

image tj_thursday:
    "tjthursday.png"
    zoom 0.2

image tj_saturday:
    "tjsaturday.png"
    zoom 0.2

##########################
image flynn_friday:
    "fridayflynn.png"
    zoom 0.2

image flynn_sunday:
    "flynnsunday1.jpg"
    zoom 0.2

image flynn_sunday2:
    "flynnsunday2.jpg" with Dissolve(0.1, alpha=True), zoom 0.2
    pause 1.0
    "flynnsunday1.jpg" with Dissolve(0.1, alpha=True), zoom 0.2

##########################
image jenna_friday:
    "fridayjenna.png"
    zoom 0.2

image jenna_sunday:
    "sundayjenna2.png"
    zoom 0.2

image jenna_sunday2:
    "sundayjenna3.png" with Dissolve(1.0, alpha=True), zoom 0.2
    pause 1.0
    "sundayjenna2.png" with Dissolve(1.0, alpha=True), zoom 0.2
    pause 1.0
    repeat

##########################

screen scenegallery():
    tag menu
    use exgame_menu(scroll="viewport"):
        grid 4 14:
            style_prefix "gslot"
            xalign 0.5
            yalign 0.5
            spacing gui.slut2_spacing
            ## common
            null



            if renpy.seen_label("saturday"):
                imagebutton idle "what_saturday" action [Start("saturday")]
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("wideshot"):
                imagebutton idle "all_sunday" action [Start("wideshot")]
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("monday"):
                imagebutton idle "all_monday" action [Start("monday")]
            else:
                add "images/thumbnails/locked.png"


            ## carl
            add "images/thumbnails/carl.png"

            if renpy.seen_label("carltuesday"):
                imagebutton idle "carl_tuesday" action Start("carltuesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("carlwednesday"):
                imagebutton idle "all_wednesday" action Start("carlwednesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("carlthursday"):
                imagebutton idle "all_thursday" action Start("carlthursday")
            else:
                add "images/thumbnails/locked.png"

            null

            if renpy.seen_label("carlfriday"):
                imagebutton idle "all_friday" action Start("carlfriday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("carlsaturday"):
                imagebutton idle "carl_saturday" action Start("carlsaturday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("carlsunday"):
                imagebutton idle "carl_sunday" action Start("carlsunday")
            else:
                add "images/thumbnails/locked.png"

            ## leo
            add "images/thumbnails/leo.png"

            if renpy.seen_label("leotuesday"):
                imagebutton idle "all_tuesday" action Start("leotuesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("leowednesday"):
                imagebutton idle "all_wednesday" action Start("leowednesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("leothursday"):
                imagebutton idle "all_thursday" action Start("leothursday")
            else:
                add "images/thumbnails/locked.png"

            null

            if renpy.seen_label("leofriday"):
                imagebutton idle "leo_friday" action Start("leofriday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("leosaturdaya"):
                imagebutton idle "all_saturday" action Start("leosaturdaya")
            elif renpy.seen_label("leosaturdayb"):
                imagebutton idle "all_saturday" action Start("leosaturdayb")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("leosunday"):
                imagebutton idle "leo_sunday" action Start("leosunday")
            else:
                add "images/thumbnails/locked.png"

            ## tj
            add "images/thumbnails/tj.png"

            if renpy.seen_label("tjtuesday"):
                imagebutton idle "tj_tuesday" action Start("tjtuesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("tjwednesday"):
                imagebutton idle "all_wednesday" action Start("tjwednesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("tjthursday"):
                imagebutton idle "tj_thursday" action Start("tjthursday")
            else:
                add "images/thumbnails/locked.png"

            null

            if renpy.seen_label("tjfriday"):
                imagebutton idle "all_friday" action Start("tjfriday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("tjsaturday"):
                imagebutton idle "tj_saturday" action Start("tjsaturday")
            else:
                add "images/thumbnails/locked.png"

            null

            ## flynn
            add "images/thumbnails/flynn.png"

            if renpy.seen_label("flynntuesday"):
                imagebutton idle "all_tuesday" action Start("flynntuesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("flynnwednesday"):
                imagebutton idle "all_wednesday" action Start("flynnwednesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("flynnthursday"):
                imagebutton idle "all_thursday" action Start("flynnthursday")
            else:
                add "images/thumbnails/locked.png"

            null

            if renpy.seen_label("flynnfriday"):
                imagebutton idle "flynn_friday" action Start("flynnfriday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("flynnsaturday"):
                imagebutton idle "all_saturday" action Start("flynnsaturday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("flynnsunday"):
                imagebutton:
                    idle "flynn_sunday"
                    hover "flynn_sunday2"
                    action Start("flynnsunday")
            else:
                add "images/thumbnails/locked.png"

            ## jenna
            add "images/thumbnails/jenna.png"

            if renpy.seen_label("jennatuesday"):
                imagebutton idle "all_tuesday" action Start("jennatuesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("jennawednesday"):
                imagebutton idle "all_wednesday" action Start("jennawednesday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("jennathursday"):
                imagebutton idle "all_thursday" action Start("jennathursday")
            else:
                add "images/thumbnails/locked.png"

            null

            if renpy.seen_label("jennafriday"):
                imagebutton idle "jenna_friday" action Start("jennafriday")
            else:
                add "images/thumbnails/locked.png"

            if renpy.seen_label("jennasunday"):
                imagebutton:
                    idle "jenna_sunday"
                    hover "jenna_sunday2"
                    action Start("jennasunday")
            else:
                add "images/thumbnails/locked.png"

            null

            #bonus
            add "images/thumbnails/chase.png"
            imagebutton idle "images/thumbnails/date.png" action Start("sidestory_date")
            imagebutton idle "images/thumbnails/runaway.png" action Start("sidestory_runaway")
            imagebutton idle "images/thumbnails/lights.png" action Start("sidestory_lights")

            null
            imagebutton idle "images/thumbnails/phone.png" action Start("sidestory_phone")
            imagebutton idle "images/thumbnails/party.png" action Start("sidestory_party")
            imagebutton idle "images/thumbnails/metaphor.png" action Start("sidestory_metaphor")

            null
            imagebutton idle "images/thumbnails/trip.png" action Start("sidestory_trip")
            null
            null

    use extra_ui_3

### MUSIC ROOM ###########################################

init python:
    mr = MusicRoom(fadein=1.0, loop=True, single_track=True, shuffle=False)
    mr.add("theme.ogg", always_unlocked=True)
    #mr.add("65sting.ogg")
    mr.add("748.ogg")
    mr.add("acousticbreeze.ogg")
    mr.add("adastra.ogg")
    mr.add("adastratheme.ogg")
    mr.add("anger.ogg")
    mr.add("anniemay.ogg")
    mr.add("argument.ogg")
    mr.add("atmosphere.ogg")
    mr.add("backstage1.ogg")
    mr.add("backstage2.ogg")
    mr.add("backstage3.ogg")
    mr.add("badparty.ogg")
    mr.add("banter.ogg")
    mr.add("becauseforeverythingthereissomeone.ogg")
    mr.add("bent.ogg")
    mr.add("bgkitworth.ogg")
    mr.add("bittersweet.ogg")
    mr.add("blackballed.ogg")
    mr.add("blurry.ogg")
    mr.add("bookofjob.ogg")
    mr.add("brianstheme.ogg")
    mr.add("carefree.ogg")
    mr.add("cast_from_dust.ogg")
    mr.add("coldbloodsoakedfur.ogg")
    mr.add("comeover.ogg")
    mr.add("creep.ogg")
    mr.add("crimeslow.ogg")
    mr.add("daze.ogg")
    mr.add("deadlybeauty.ogg", always_unlocked=True)
    mr.add("drag.ogg")
    mr.add("echo.ogg")
    #mr.add("electronic.ogg")
    mr.add("emo.ogg")
    mr.add("end.ogg")
    mr.add("end1.ogg")
    mr.add("epiphany.ogg")
    mr.add("finalchat.ogg")
    mr.add("goodmorning.ogg")
    mr.add("hiphop.ogg")
    mr.add("hitchhikers.ogg")
    mr.add("intimate.ogg")
    mr.add("jennastheme.ogg")
    mr.add("lazy.ogg")
    mr.add("loneliness.ogg")
    mr.add("meeting2.ogg")
    mr.add("melancholia.ogg")
    mr.add("mitt.ogg")
    mr.add("moth.ogg")
    mr.add("neutral.ogg")
    mr.add("nicetomeetyou.ogg")
    mr.add("nostalgia.ogg")
    mr.add("oldwinds.ogg")
    mr.add("payton.ogg")
    mr.add("pop.ogg")
    mr.add("quiet.ogg")
    mr.add("reckoning.ogg")
    mr.add("reverb.ogg")
    mr.add("rock.ogg")
    mr.add("sex.ogg")
    mr.add("shiver.ogg")
    mr.add("static statues.ogg")
    mr.add("sunrise without you.ogg")
    mr.add("terrorbelowthesurface.ogg")
    mr.add("echothemedark.ogg")
    mr.add("themeforalonelywolf.ogg")
    mr.add("themeforalonelywolf2.ogg")
    mr.add("themepiano.ogg")
    mr.add("this lingering hope.ogg")
    mr.add("TJtheme.ogg")
    mr.add("transition.ogg")
    mr.add("unease.mp3")
    mr.add("Vanishing_Paradise.ogg")
    mr.add("wasted.ogg")
    mr.add("Wastelandp1.ogg")
    mr.add("when stars align.ogg")
    mr.add("when_your_arms_were_around_me.ogg")
    mr.add("wyawamv2.ogg")

    #mr.add("five_3_2.ogg")
    #mr.add("onelastkiss.ogg")
    #mr.add("beholdiwasshapenininiquity.ogg")

screen music_room:

    tag menu
    use exgame_menu(scroll="viewport"):

        vbox:
            xpos 140
            # The buttons that play each track.
            textbutton "{font=ui/gallery/28 days later.ttf}theme" action mr.Play("theme.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}748 shiver remix" action mr.Play("748.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}acoustic breeze" action mr.Play("acousticbreeze.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}adastra" action mr.Play("adastra.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}adastra theme" action mr.Play("adastratheme.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}anger" action mr.Play("anger.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}anniemay" action mr.Play("anniemay.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}argument" action mr.Play("argument.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}atmosphere" action mr.Play("atmosphere.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}backstage 1" action mr.Play("backstage1.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}backstage 2" action mr.Play("backstage2.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}backstage 3" action mr.Play("backstage3.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}bad party" action mr.Play("badparty.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}banter" action mr.Play("banter.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}because for everything" action mr.Play("becauseforeverythingthereissomeone.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}behold i was shapen in iniquity" action mr.Play("beholdiwasshapenininiquity.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}bent" action mr.Play("bent.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}bgkitworth" action mr.Play("bgkitworth.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}bittersweet" action mr.Play("bittersweet.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}blackballed" action mr.Play("blackballed.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}blurry" action mr.Play("blurry.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}book of job" action mr.Play("bookofjob.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}brian theme" action mr.Play("brianstheme.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}carefree" action mr.Play("carefree.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}cast from dust" action mr.Play("cast_from_dust.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}cold blood soaked fur" action mr.Play("coldbloodsoakedfur.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}comeover" action mr.Play("comeover.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}creep" action mr.Play("creep.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}crimeslow" action mr.Play("crimeslow.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}daze" action mr.Play("daze.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}deadly beauty" action mr.Play("deadlybeauty.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}drag" action mr.Play("drag.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}electronic" action mr.Play("electronic.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}echo" action mr.Play("echo.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}emo" action mr.Play("emo.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}end" action mr.Play("end.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}end1" action mr.Play("end1.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}epiphany" action mr.Play("epiphany.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}final chat" action mr.Play("finalchat.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}good morning" action mr.Play("goodmorning.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}hiphop" action mr.Play("hiphop.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}hitchhikers" action mr.Play("hitchhikers.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}intimate" action mr.Play("intimate.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}jenna theme" action mr.Play("jennastheme.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}lazy" action mr.Play("lazy.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}loneliness" action mr.Play("loneliness.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}meeting" action mr.Play("meeting2.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}melancholia" action mr.Play("melancholia.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}mitt" action mr.Play("mitt.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}moth" action mr.Play("moth.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}neutral" action mr.Play("neutral.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}nice to meet you" action mr.Play("nicetomeetyou.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}nostalgia" action mr.Play("nostalgia.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}old winds" action mr.Play("oldwinds.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}one last kiss" action mr.Play("onelastkiss.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}payton" action mr.Play("payton.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}pop" action mr.Play("pop.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}quiet" action mr.Play("quiet.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}reckoning" action mr.Play("reckoning.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}reverb" action mr.Play("reverb.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}rock" action mr.Play("rock.ogg") style "music_list" text_style "music_list_button_text"
            #textbutton "{font=ui/gallery/28 days later.ttf}sex" action mr.Play("sex.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}shiver" action mr.Play("shiver.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}static statues" action mr.Play("static statues.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}sunrise without you" action mr.Play("sunrise without you.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}terror below the surface" action mr.Play("terrorbelowthesurface.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}theme dark" action mr.Play("echothemedark.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}theme for a lonely wolf" action mr.Play("themeforalonelywolf.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}theme for a lonely wolf 2" action mr.Play("themeforalonelywolf2.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}theme piano" action mr.Play("themepiano.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}this lingering hope" action mr.Play("this lingering hope.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}tj theme" action mr.Play("TJtheme.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}transition" action mr.Play("transition.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}unease" action mr.Play("unease.mp3") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}vanishing paradise" action mr.Play("Vanishing_Paradise.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}wasted" action mr.Play("wasted.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}wasteland" action mr.Play("Wastelandp1.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}when stars align" action mr.Play("when stars align.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}when your arms were around me" action mr.Play("when_your_arms_were_around_me.ogg") style "music_list" text_style "music_list_button_text"
            textbutton "{font=ui/gallery/28 days later.ttf}when your arms were around me v2" action mr.Play("wyawamv2.ogg") style "music_list" text_style "music_list_button_text"
            textbutton " " action None style "music_list" text_style "music_list_button_text"


    use mp3
    use extra_ui_1
