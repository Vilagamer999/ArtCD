## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True
    ## These control the width and height of the screen.

    config.screen_width = 1024
    config.screen_height = 768

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Echo"
    config.window_icon = "icon.png"
    config.quit_action = Quit()

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Echo"
    config.version = "0.0"


    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.glow(
        ## Theme: Glow
        ## Color scheme: Urban Sprawl

        ## The color of an idle widget face.
        widget = "#333333",

        ## The color of a focused widget face.
        widget_hover = "#000000",

        ## The color of the text in a widget.
        widget_text = "#6C8A2F",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face.
        disabled = "#8F0000",

        ## The color of disabled widget text.
        disabled_text = "#333333",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#8F0000",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "ui/Cover.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "ui/bg.jpg",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )



    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.
    ## style.X == 'X' represents the 'show_who_window_style' that was defined in 'script.rpy. (i.e., show_who_window_style="say_flynn" in script.rpy = style.say_flynn in options.rpy)
    ## style.X.background represent the background image of that character dialog window. These are the images in the ui folder.
    ## The four '_padding' variables represent spacing of the character's name. If a name is off center, adjust the values for "left_padding" and/or "right_padding"

    style.say_flynn = Style ('say_who_window')
    style.say_flynn.background = Frame("ui/speaker_flynn.png", 0, 0)
    style.say_flynn.xalign = 0.20
    style.say_flynn.yalign = 0.0
    style.say_flynn.yoffset = -195
    style.say_flynn.xfill = True
    style.say_flynn.yfill = True
    style.say_flynn.ymaximum = 33
    style.say_flynn.xmaximum = 104

    style.say_chase = Style ('say_who_window')
    style.say_chase.background = Frame("ui/speaker_chase.png", 0, 0)
    style.say_chase.xalign = 0.20
    style.say_chase.yalign = 0.0
    style.say_chase.yoffset = -195
    style.say_chase.xfill = True
    style.say_chase.yfill = True
    style.say_chase.ymaximum = 33
    style.say_chase.xmaximum = 104

    style.say_clint = Style ('say_who_window')
    style.say_clint.background = Frame("ui/speaker_clint.png", 0, 0)
    style.say_clint.xalign = 0.20
    style.say_clint.yalign = 0.0
    style.say_clint.yoffset = -195
    style.say_clint.xfill = True
    style.say_clint.yfill = True
    style.say_clint.ymaximum = 33
    style.say_clint.xmaximum = 104

    style.say_jenna = Style ('say_who_window')
    style.say_jenna.background = Frame("ui/speaker_jenna.png", 0, 0)
    style.say_jenna.xalign = 0.20
    style.say_jenna.yalign = 0.0
    style.say_jenna.yoffset = -195
    style.say_jenna.xfill = True
    style.say_jenna.yfill = True
    style.say_jenna.ymaximum = 33
    style.say_jenna.xmaximum = 104

    style.say_carl = Style ('say_who_window')
    style.say_carl.background = Frame("ui/speaker_carl.png", 0, 0)
    style.say_carl.xalign = 0.20
    style.say_carl.yalign = 0.0
    style.say_carl.yoffset = -195
    style.say_carl.xfill = True
    style.say_carl.yfill = True
    style.say_carl.ymaximum = 33
    style.say_carl.xmaximum = 104

    style.say_tj = Style ('say_who_window')
    style.say_tj.background = Frame("ui/speaker_tj.png", 0, 0)
    style.say_tj.xalign = 0.20
    style.say_tj.yalign = 0.0
    style.say_tj.yoffset = -195
    style.say_tj.xfill = True
    style.say_tj.yfill = True
    style.say_tj.ymaximum = 33
    style.say_tj.xmaximum = 104

    style.say_leo = Style ('say_who_window')
    style.say_leo.background = Frame("ui/speaker_leo.png", 0, 0)
    style.say_leo.xalign = 0.20
    style.say_leo.yalign = 0.0
    style.say_leo.yoffset = -195
    style.say_leo.xfill = True
    style.say_leo.yfill = True
    style.say_leo.ymaximum = 33
    style.say_leo.xmaximum = 104

    style.say_unknown = Style ('say_who_window')
    style.say_unknown.background = Frame("ui/speaker_unknown.png", 0, 0)
    style.say_unknown.xalign = 0.20
    style.say_unknown.yalign = 0.0
    style.say_unknown.yoffset = -195
    style.say_unknown.xfill = True
    style.say_unknown.yfill = True
    style.say_unknown.ymaximum = 33
    style.say_unknown.xmaximum = 104

    style.say_kud = Style ('say_who_window')
    style.say_kud.background = Frame("ui/speaker_kudzu.png", 0, 0)
    style.say_kud.xalign = 0.20
    style.say_kud.yalign = 0.0
    style.say_kud.yoffset = -195
    style.say_kud.xfill = True
    style.say_kud.yfill = True
    style.say_kud.ymaximum = 33
    style.say_kud.xmaximum = 104

    style.say_raven = Style ('say_who_window')
    style.say_raven.background = Frame("ui/speaker_raven.png", 0, 0)
    style.say_raven.xalign = 0.20
    style.say_raven.yalign = 0.0
    style.say_raven.yoffset = -195
    style.say_raven.xfill = True
    style.say_raven.yfill = True
    style.say_raven.ymaximum = 33
    style.say_raven.xmaximum = 104

    style.say_duke = Style ('say_who_window')
    style.say_duke.background = Frame("ui/speaker_duke.png", 0, 0)
    style.say_duke.xalign = 0.20
    style.say_duke.yalign = 0.0
    style.say_duke.yoffset = -195
    style.say_duke.xfill = True
    style.say_duke.yfill = True
    style.say_duke.ymaximum = 33
    style.say_duke.xmaximum = 104

    style.say_brian = Style ('say_who_window')
    style.say_brian.background = Frame("ui/speaker_brian.png", 0, 0)
    style.say_brian.xalign = 0.20
    style.say_brian.yalign = 0.0
    style.say_brian.yoffset = -195
    style.say_brian.xfill = True
    style.say_brian.yfill = True
    style.say_brian.ymaximum = 33
    style.say_brian.xmaximum = 104

    style.say_janice = Style ('say_who_window')
    style.say_janice.background = Frame("ui/speaker_janice.png", 0, 0)
    style.say_janice.xalign = 0.20
    style.say_janice.yalign = 0.0
    style.say_janice.yoffset = -195
    style.say_janice.xfill = True
    style.say_janice.yfill = True
    style.say_janice.ymaximum = 33
    style.say_janice.xmaximum = 104

    style.say_sydney = Style ('say_who_window')
    style.say_sydney.background = Frame("ui/speaker_sydney.png", 0, 0)
    style.say_sydney.xalign = 0.20
    style.say_sydney.yalign = 0.0
    style.say_sydney.yoffset = -195
    style.say_sydney.xfill = True
    style.say_sydney.yfill = True
    style.say_sydney.ymaximum = 33
    style.say_sydney.xmaximum = 104

    style.say_micha = Style ('say_who_window')
    style.say_micha.background = Frame("ui/speaker_micha.png", 0, 0)
    style.say_micha.xalign = 0.20
    style.say_micha.yalign = 0.0
    style.say_micha.yoffset = -195
    style.say_micha.xfill = True
    style.say_micha.yfill = True
    style.say_micha.ymaximum = 33
    style.say_micha.xmaximum = 104

    style.say_heather = Style ('say_who_window')
    style.say_heather.background = Frame("ui/speaker_heather.png", 0, 0)
    style.say_heather.xalign = 0.20
    style.say_heather.yalign = 0.0
    style.say_heather.yoffset = -195
    style.say_heather.xfill = True
    style.say_heather.yfill = True
    style.say_heather.ymaximum = 33
    style.say_heather.xmaximum = 104

    style.say_jeremy = Style ('say_who_window')
    style.say_jeremy.background = Frame("ui/speaker_jeremy.png", 0, 0)
    style.say_jeremy.xalign = 0.20
    style.say_jeremy.yalign = 0.0
    style.say_jeremy.yoffset = -195
    style.say_jeremy.xfill = True
    style.say_jeremy.yfill = True
    style.say_jeremy.ymaximum = 33
    style.say_jeremy.xmaximum = 104

    style.say_daxton = Style ('say_who_window')
    style.say_daxton.background = Frame("ui/speaker_daxton.png", 0, 0)
    style.say_daxton.xalign = 0.20
    style.say_daxton.yalign = 0.0
    style.say_daxton.yoffset = -195
    style.say_daxton.xfill = True
    style.say_daxton.yfill = True
    style.say_daxton.ymaximum = 33
    style.say_daxton.xmaximum = 104

    style.say_mayor = Style ('say_who_window')
    style.say_mayor.background = Frame("ui/speaker_mayor.png", 0, 0)
    style.say_mayor.xalign = 0.20
    style.say_mayor.yalign = 0.0
    style.say_mayor.yoffset = -195
    style.say_mayor.xfill = True
    style.say_mayor.yfill = True
    style.say_mayor.ymaximum = 33
    style.say_mayor.xmaximum = 104

    style.say_ryan = Style ('say_who_window')
    style.say_ryan.background = Frame("ui/speaker_ryan.png", 0, 0)
    style.say_ryan.xalign = 0.20
    style.say_ryan.yalign = 0.0
    style.say_ryan.yoffset = -195
    style.say_ryan.xfill = True
    style.say_ryan.yfill = True
    style.say_ryan.ymaximum = 33
    style.say_ryan.xmaximum = 104

    style.say_casey = Style ('say_who_window')
    style.say_casey.background = Frame("ui/speaker_casey.png", 0, 0)
    style.say_casey.xalign = 0.20
    style.say_casey.yalign = 0.0
    style.say_casey.yoffset = -195
    style.say_casey.xfill = True
    style.say_casey.yfill = True
    style.say_casey.ymaximum = 33
    style.say_casey.xmaximum = 104

    style.say_mike = Style ('say_who_window')
    style.say_mike.background = Frame("ui/speaker_mike.png", 0, 0)
    style.say_mike.xalign = 0.20
    style.say_mike.yalign = 0.0
    style.say_mike.yoffset = -195
    style.say_mike.xfill = True
    style.say_mike.yfill = True
    style.say_mike.ymaximum = 33
    style.say_mike.xmaximum = 104

    style.say_julian = Style ('say_who_window')
    style.say_julian.background = Frame("ui/speaker_julian.png", 0, 0)
    style.say_julian.xalign = 0.20
    style.say_julian.yalign = 0.0
    style.say_julian.yoffset = -195
    style.say_julian.xfill = True
    style.say_julian.yfill = True
    style.say_julian.ymaximum = 33
    style.say_julian.xmaximum = 104

    style.say_dad = Style ('say_who_window')
    style.say_dad.background = Frame("ui/speaker_dad.png", 0, 0)
    style.say_dad.xalign = 0.20
    style.say_dad.yalign = 0.0
    style.say_dad.yoffset = -195
    style.say_dad.xfill = True
    style.say_dad.yfill = True
    style.say_dad.ymaximum = 33
    style.say_dad.xmaximum = 104

    style.say_dev = Style ('say_who_window')
    style.say_dev.background = Frame("ui/speaker_devon.png", 0, 0)
    style.say_dev.xalign = 0.20
    style.say_dev.yalign = 0.0
    style.say_dev.yoffset = -195
    style.say_dev.xfill = True
    style.say_dev.yfill = True
    style.say_dev.ymaximum = 33
    style.say_dev.xmaximum = 104

    style.say_cam = Style ('say_who_window')
    style.say_cam.background = Frame("ui/speaker_cameron.png", 0, 0)
    style.say_cam.xalign = 0.20
    style.say_cam.yalign = 0.0
    style.say_cam.yoffset = -195
    style.say_cam.xfill = True
    style.say_cam.yfill = True
    style.say_cam.ymaximum = 33
    style.say_cam.xmaximum = 104

    style.say_mrbronson = Style ('say_who_window')
    style.say_mrbronson.background = Frame("ui/speaker_mrbronson.png", 0, 0)
    style.say_mrbronson.xalign = 0.20
    style.say_mrbronson.yalign = 0.0
    style.say_mrbronson.yoffset = -195
    style.say_mrbronson.xfill = True
    style.say_mrbronson.yfill = True
    style.say_mrbronson.ymaximum = 33
    style.say_mrbronson.xmaximum = 104

    style.say_injy = Style ('say_who_window')
    style.say_injy.background = Frame("ui/speaker_injy.png", 0, 0)
    style.say_injy.xalign = 0.20
    style.say_injy.yalign = 0.0
    style.say_injy.yoffset = -195
    style.say_injy.xfill = True
    style.say_injy.yfill = True
    style.say_injy.ymaximum = 33
    style.say_injy.xmaximum = 104

    style.say_car = Style ('say_who_window')
    style.say_car.background = Frame("ui/speaker_carny.png", 0, 0)
    style.say_car.xalign = 0.20
    style.say_car.yalign = 0.0
    style.say_car.yoffset = -195
    style.say_car.xfill = True
    style.say_car.yfill = True
    style.say_car.ymaximum = 33
    style.say_car.xmaximum = 104

    ##TODO: Modify window properties

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("ui/message_box.png", 0, 0)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.say_window.left_margin = 25
    style.say_window.right_margin = 25
    #style.say_window.top_margin = 0
    style.say_window.bottom_margin = 0
    style.say_window.xfill = True
    style.say_window.xmaximum = 750
    style.say_window.xalign = 0.5

    style.say_two_window_vbox.xalign = 0.5
    style.say_two_window_vbox.xfill = True

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 30
    style.window.right_padding = 30
    style.window.top_padding = 25
    style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.say_window.yminimum = 198
    style.say_window.ymaximum = 198
    style.say_window.yoffset = 20

    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "ui/Arcon.otf"

    ## The default size of text.

    style.default.size = 20
    style.default.line_spacing = 22


    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "sfx/click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "Theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = Fade(0.2, 0.0, 0.2)
    #config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = Fade(0.2, 0.0, 0.2)
    #config.exit_transition = None

    ## Used between screens of the game menu.
    #config.intra_transition = Fade(0.2, 0.0, 0.2)
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = Fade(0.2, 0.0, 0.2)

    ## Used when returning to the main menu from the game.
    config.game_main_transition = Fade(0.2, 0.0, 0.2)

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = Fade(0.2, 0.0, 0.2)

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = Fade(0.2, 0.0, 0.2)

    ## Used when a game is loaded.
    config.after_load_transition = Fade(0.2, 0.0, 0.2)

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "Echo-1433615853"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 30

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.

init python:
    renpy.music.register_channel("background", "sfx", loop=True)
    renpy.music.register_channel("loop", "sfx", loop=True, tight=True)

## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Echo-1.01"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Echo"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

#
init:
    define config.mouse = {"default" : [("ui/cursor.png", 0, 0)]}


################ phone code stars ###################
# This script is based on https://lemmasoft.renai.us/forums/viewtopic.php?t=40245 phone message system by Nadia Nova and other contributers of the forum.

image phone_chase = "ui/phone/phone_chase.png"
image phone_shadowchase = "ui/phone/phone_shadowchase.png"
image messages_chase = "ui/phone/messages_chase.png"
image login = "ui/phone/predater/login.png"
image phone_sad = "ui/phone/phone_sad.png"
image phone_terror = "ui/phone/phone_terror.png"
image phone_no = "ui/phone/phone_no.png"

# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.9 xoffset 0 yoffset 0

transform text_pickup:
    alpha 0.0 xalign 0.5 yalign 1.0 yoffset 900
    parallel:
        pause 0.5
        easein 0.5 alpha 1
    parallel:
        easein 0.9 yoffset 0
    on hide:
        yalign 1.0 xalign 0.5 xoffset 0 yoffset 0 alpha 1
        parallel:
            easeout 0.2 alpha 0
        parallel:
            easeout 0.9 yoffset 900

transform phone_on:
    alpha 0
    pause 1
    alpha 1

transform phone_hide:
    yalign 1.0 xalign 0.5
    xoffset 0 yoffset 0
    #pause 0.5
    easeout 0.9 yoffset 900

transform phone_message_bubble_tip:
    xoffset -10
    yoffset 16

transform phone_message_bubble_tip2:
    xoffset 230
    yoffset 16

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message

########### recent messages on screen #############

transform message_1:
    alpha 0.0 xpos 342 ypos 147
    easein 0.9 alpha 1 ypos 147

transform message_2:
    alpha 0.0 xpos 342 ypos 222
    easein 0.9 alpha 1 ypos 222

transform message_3:
    alpha 0.0 xpos 342 ypos 297
    easein 0.9 alpha 1 ypos 297

transform message_4:
    alpha 0.0 xpos 342 ypos 372
    easein 0.9 alpha 1 ypos 372

transform message_5:
    alpha 0.0 xpos 342 ypos 447
    easein 0.9 alpha 1 ypos 447

transform message_6:
    alpha 0.0 xpos 342 ypos 522
    easein 0.9 alpha 1 ypos 522

transform message_7:
    alpha 0.0 xpos 342 ypos 597
    easein 0.9 alpha 1 ypos 597

transform text_1:
    alpha 0.0 xoffset 428 ypos 210 xalign 0.0
    easein 0.9 alpha 1 ypos 210

transform text_2:
    alpha 0.0 xoffset 428 ypos 285 xalign 0.0
    easein 0.9 alpha 1 ypos 285

transform text_3:
    alpha 0.0 xoffset 428 ypos 360 xalign 0.0
    easein 0.9 alpha 1 ypos 360

transform text_4:
    alpha 0.0 xoffset 428 ypos 435 xalign 0.0
    easein 0.9 alpha 1 ypos 435

transform text_5:
    alpha 0.0 xoffset 428 ypos 510 xalign 0.0
    easein 0.9 alpha 1 ypos 510

transform text_6:
    alpha 0.0 xoffset 428 ypos 585 xalign 0.0
    easein 0.9 alpha 1 ypos 585

transform text_7:
    alpha 0.0 xoffset 428 ypos 660 xalign 0.0
    easein 0.9 alpha 1 ypos 660

transform app_1:
    xpos 390 ypos 128

transform app_2:
    xpos 530 ypos 128

transform app_3:
    xpos 390 ypos 258

transform app_4:
    xpos 530 ypos 258

transform app_5:
    xpos 390 ypos 538

transform app_6:
    xpos 530 ypos 538

transform login:
    xalign 0.5 yalign 0.5 alpha 1 yoffset -5
    pause 0.5
    easeout 0.9 alpha 0

transform login_2:
    xalign 0.5 yalign 0.5 alpha 1 yoffset -5
    pause 2
    easein 0.9 alpha 0

transform user_page:
    xpos 340 ypos 78 alpha 0
    pause 1
    easein 0.9 alpha 1


###################################################

#### phone #####

label phone_start:
    #window hide
    $ phone_flag=False
    show phone_chase at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_sad:
    $ phone_flag=False
    show phone_sad at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_terror:
    $ phone_flag=False
    show phone_terror at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_no:
    $ phone_flag=False
    show phone_no at phone_pickup
    $ renpy.pause(0.2)
    return

label text_chase(who):
    $ phone_flag=False
    show phone_chase at phone_pickup
    show screen home
    if who.lower() == "leo":
        show leo_bg at text_pickup
    elif who.lower() == "leo2":
        show leo2_bg at text_pickup
    elif who.lower() == "carl":
        show carl_bg at text_pickup
    elif who.lower() == "flynn":
        show flynn_bg at text_pickup
    elif who.lower() == "tj":
        show tj_bg at text_pickup
    elif who.lower() == "jenna":
        show jenna_bg at text_pickup
    return


label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return

label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return

label phone_msgi:
    $ renpy.pause()
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return


label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label phone_end:
    #$ renpy.pause()
    #$ phone_flag=True
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen home
    $ renpy.pause(0.2)
    show phone_chase at phone_hide
    $ renpy.pause(0.2)
    return

label sad_end:
    #$ renpy.pause()
    #$ phone_flag=True
    hide screen home
    $ renpy.pause(0.2)
    show phone_sad at phone_hide
    $ renpy.pause(0.2)
    return

label no_end:
    #$ renpy.pause()
    #$ phone_flag=True
    hide screen home
    $ renpy.pause(0.2)
    show phone_no at phone_hide
    $ renpy.pause(0.2)
    return

label terror_end:
    #$ renpy.pause()
    #$ phone_flag=True
    hide screen home
    $ renpy.pause(0.2)
    show phone_terror at phone_hide
    $ renpy.pause(0.2)
    return

label text_end:
    #$ phone_flag=True
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen home
    $ renpy.pause(0.2)
    hide leo_bg
    hide leo2_bg
    hide carl_bg
    hide flynn_bg
    hide tj_bg
    hide jenna_bg
    show phone_chase at phone_hide
    $ renpy.pause(0.5)
    return

label text_shadow:
    #$ phone_flag=True
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen home
    $ renpy.pause(0.2)
    hide leo_bg
    show phone_shadowchase
    $ renpy.pause(1)
    hide phone_chase
    show phone_shadowchase at phone_hide
    $ renpy.pause(0.5)
    return

label reply_message(what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    return

label message_img(who, what,img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return


label text_0(who, what):
    $ renpy.pause(0.9)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "m":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    $ renpy.pause(0.3)
    return

label text(who, what):
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "m":
        show screen phone_message2(who, what)
    #elif who.lower() == "e":
     #   show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    $ renpy.pause(0.3)
    return

##############################################
