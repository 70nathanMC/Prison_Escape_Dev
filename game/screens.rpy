################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 108

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill False
    xsize gui.textbox_width
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background gui.textbox_background

style namebox:
    xpos 80
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos 30
    ysize gui.namebox_height

    background gui.namebox_background 
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 80
    xsize gui.dialogue_width
    ypos 85

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

transform choice_zoom:
    transform_anchor True
    on idle:
        easein 0.1 zoom 0.97 # Barely shrinks (96%) to keep the large box stable
    on hover:
        easein 0.1 zoom 1.0  # Snaps to 100% when hovered

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            $ cost = i.kwargs.get("cost", None) if i.kwargs else None

            # 1. We apply the terminal_zoom transform directly to the whole button!
            button at choice_zoom:
                action i.action
                style "choice_button" 
                
                hbox:
                    xfill True
                    yalign 0.5
                    
                    # 2. Since it's a 'button', we add the text manually
                    text "> " + i.caption style "choice_button_text" yalign 0.5
                    
                    # 3. The Cost Indicator (Invisible until hovered)
                    if cost is not None:
                        text ( "-[cost] MIN" if cost > 0 else "FREE" ):
                            yalign 0.5
                            xalign 1.0
                            font gui.text_font
                            size 28 # Bumped up slightly to account for the 0.8 idle shrink
                            bold True
                            idle_color "#00000000" 
                            hover_color ("#32cd32" if cost == 0 else "#ff8c00")


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    idle_background gui.choice_button_background
    hover_background gui.choice_button_hover_background
    padding (25, 12, 25, 12) 

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    font gui.text_font 
    size 30 # Bumped from 28 to 32 so it stays readable when shrunk to 80%
    idle_color "#aaaaaa"
    hover_color "#32cd32"

style choice_cost_text:
    size 28
    bold True
    color "#00000000" 
    hover_color "#ff8c00"


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

transform quick_menu_zoom:
    transform_anchor True # Keeps the zoom perfectly centered
    on idle:
        easein 0.1 zoom 0.85
    on hover:
        easein 0.1 zoom 1.0


screen quick_menu():

    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.015
            yoffset -15 
            spacing 35  

            # We added 'at terminal_zoom' to the end of each command!
            textbutton _("BACK") action Rollback() at quick_menu_zoom
            textbutton _("HISTORY") action ShowMenu('history') at quick_menu_zoom
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True) at quick_menu_zoom
            textbutton _("AUTO") action Preference("auto-forward", "toggle") at quick_menu_zoom
            textbutton _("SAVE") action ShowMenu('save') at quick_menu_zoom
            textbutton _("Q.SAVE") action QuickSave() at quick_menu_zoom
            textbutton _("Q.LOAD") action QuickLoad() at quick_menu_zoom
            textbutton _("SETTINGS") action ShowMenu('preferences') at quick_menu_zoom


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 0.999
    spacing 30 # Adds clean, even spacing between the system commands

style quick_button:
    padding (12, 4)
    background None

style quick_button_text:
    font gui.name_text_font # Orbitron
    size 20 # <-- Render it large so it stays crisp!
    kerning 1
    
    outlines [ (2, "#000000", 0, 0) ]
    
    idle_color "#aaaaaa" 
    hover_color "#32cd32"
    selected_color "#32cd32"
    selected_idle_color "#32cd32"
    selected_hover_color "#32cd32"

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    # This check asks: "Is the current screen NOT the main_menu?"
    # If we are in Settings, Load, or About, this will be True.
    if renpy.get_screen("main_menu") is None:
        
        # --- HORIZONTAL TOP BAR (For Settings, Load, About) ---
        hbox:
            style_prefix "navigation"
            xalign 0.5    
            ypos 30       
            spacing 30    

            # 1. Only show HISTORY if we are actually in a game
            if not main_menu:
                textbutton _("HISTORY") action ShowMenu("history") at quick_menu_zoom
                textbutton _("SAVE") action ShowMenu("save") at quick_menu_zoom

            # 2. These are ALWAYS relevant
            textbutton _("LOAD") action ShowMenu("load") at quick_menu_zoom
            textbutton _("SETTINGS") action ShowMenu("preferences") at quick_menu_zoom
            textbutton _("ABOUT") action ShowMenu("about") at quick_menu_zoom
            
            # 3. Only show "MAIN MENU" if we are currently playing
            if not main_menu:
                textbutton _("MAIN MENU") action MainMenu() at quick_menu_zoom
            
            if renpy.variant("pc"):
                textbutton _("QUIT") action Quit(confirm=True) at quick_menu_zoom
            
            textbutton _("BACK") action Return() at quick_menu_zoom
    else:
        # On the Main Menu, we do nothing because we hard-coded 
        # the buttons into the main_menu screen earlier.
        pass

## --- NAVIGATION STYLING ---

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    background None
    padding (10, 5, 10, 5)
    # This ensures the BUTTON BOX itself stays on the right
    xalign 1.0 

style navigation_button_text:
    font gui.name_text_font 
    size 28 # Slightly smaller for the horizontal bar
    kerning 1
    idle_color "#ff8c00"
    hover_color "#32cd32"
    selected_color "#32cd32"
    
    # Change these to 0.5 so they work for BOTH vertical and horizontal
    text_align 0.5
    xalign 0.5

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform terminal_blink:
    alpha 1.0
    pause 0.4
    alpha 0.0
    pause 0.4
    repeat

screen main_menu():

    tag menu
    style_prefix "main_menu"

    # This forces the image to stretch or shrink to exactly 1920x1080
    add "menu_screen.png":
        size (1920, 1080) 
        align (0.5, 0.5)

    # --- TRUE TERMINAL TYPING ENGINE ---
    
    # 1. We store the text, color, size, and bold properties in a list of Data
    default boot_lines = [
        ("SYSTEM BOOT SEQUENCE INITIATED...", "#32cd32", 18, False),
        ("LOADING KERNEL............. OK", "#32cd32", 18, False),
        ("MOUNTING VIRTUAL DRIVES.... OK", "#32cd32", 18, False),
        ("BYPASSING SECURITY......... OK", "#32cd32", 18, False),
        ("ESTABLISHING CONNECTION.... OK", "#32cd32", 18, False),
        ("", "#32cd32", 18, False), # Empty line to create spacing before the orange text
        ("AWAITING USER INPUT.", "#ff8c00", 18, True)
    ]

    # 2. Trackers for the animation state
    default curr_line = 0
    default curr_char = 0
    default is_done = False

    # 3. The Typing Engine Loop (Fires every 0.02 seconds, immune to mouse-hover bugs!)
    timer 0.02 repeat True action [
        If(not is_done,
            If(curr_char < len(boot_lines[curr_line][0]),
                # If the line isn't finished, add 1 character
                SetScreenVariable("curr_char", curr_char + 1),
                
                # If the line IS finished, move to the next line
                If(curr_line < len(boot_lines) - 1,
                    [SetScreenVariable("curr_line", curr_line + 1), SetScreenVariable("curr_char", 0)],
                    # If we are on the very last line, stop the engine!
                    SetScreenVariable("is_done", True) 
                )
            )
        )
    ]

    # 2. DECORATION: The Display Canvas (Bottom Left)
    vbox:
        xpos 15
        yalign 1.0    # Pushes the box to the bottom
        yoffset -100   # Margin from the bottom edge
        spacing 8

        # Step A: Print all previous lines that are 100% complete
        for i in range(curr_line):
            text boot_lines[i][0] color boot_lines[i][1] size boot_lines[i][2] bold boot_lines[i][3]

        # Step B: Print the line currently being typed, with a SOLID cursor attached to the end!
        if not is_done:
            $ partial_text = boot_lines[curr_line][0][:curr_char]
            hbox:
                text partial_text color boot_lines[curr_line][1] size boot_lines[curr_line][2] bold boot_lines[curr_line][3]
                text "█" color boot_lines[curr_line][1] size boot_lines[curr_line][2] 
                
        # Step C: Once all typing finishes, print the final line and switch to a BLINKING cursor!
        else:
            hbox:
                text boot_lines[curr_line][0] color boot_lines[curr_line][1] size boot_lines[curr_line][2] bold boot_lines[curr_line][3]
                text "█" color boot_lines[curr_line][1] size boot_lines[curr_line][2] at terminal_blink

    # 4a. THE GAME TITLE: Independent and Locked
    vbox:
        xalign 1.0
        yalign 1.0
        xoffset -15
        yoffset -350 
        spacing 0 

        # DELETE the extra "xalign 1.0" that was sitting right here!

        text "[config.name!t]":
            font gui.name_text_font 
            size 80 
            color "#32cd32" 
            kerning 5 
            xalign 1.0 
            outlines [(4, "#32cd3220", 0, 0), (2, "#000000", 1, 1)]
            
        text "v. [config.version]":
            font gui.text_font 
            size 18 
            color "#aaaaaa" 
            xalign 1.0 
            yoffset -5
            outlines [(1, "#000000", 1, 1)]

    # 4b. THE NAVIGATION BUTTONS: Independent and Animated
    vbox:
        xalign 1.0
        yalign 1.0
        xoffset -15
        yoffset -80 # Locked to the bottom
        spacing 10
        style_prefix "navigation"
        
        textbutton _("START") action Start() at quick_menu_zoom
        textbutton _("LOAD") action ShowMenu("load") at quick_menu_zoom
        textbutton _("SETTINGS") action ShowMenu("preferences") at quick_menu_zoom
        textbutton _("ABOUT") action ShowMenu("about") at quick_menu_zoom

        if renpy.variant("pc"):
            textbutton _("QUIT") action Quit(confirm=not main_menu) at quick_menu_zoom

## --- MAIN MENU STYLES ---
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # Terminal Backgrounds (Always pure pitch black, no exceptions!)
    add Solid("#020802")

    frame:
        style "game_menu_outer_frame"

        # The Content Frame (Save/Load/Settings)
        # We removed the navigation frame so this spans the whole screen!
        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        spacing spacing
                        transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    spacing spacing
                    transclude

            else:
                transclude

    # Use our new horizontal top-bar navigation ON TOP of everything
    use navigation

    # The Page Title (e.g., "SAVE", "PREFERENCES")
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


## --- STYLES FOR THE HACKER MENU ---

style game_menu_outer_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style game_menu_outer_frame:
    xfill True
    yfill True
    top_padding 200 # Leaves space for the navigation and title at the top
    bottom_padding 45
    background None # Remove the default image background

style game_menu_content_frame:
    xalign 0.5 # Centers the Save slots / Settings
    xsize 1600 # Widen the content area since we removed the side bar
    left_margin 30
    right_margin 30

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 100
    ypos 140 # Positioned below the navigation bar

style game_menu_label_text:
    font gui.name_text_font # Uses Orbitron!
    size 45
    color "#32cd32" # Neon Green
    yalign 0.5
    kerning 2


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    # No scrollbar!
    use game_menu(_("SYSTEM INFO // ABOUT")):

        style_prefix "about"

        # 1. THE CANVAS: 'fixed' automatically fills the entire available screen space.
        fixed:
            xfill True
            yfill True

            # 2. THE TRUE CENTER: This box finds the exact middle of the 'fixed' canvas.
            vbox:
                align (0.5, 0.5)
                spacing 40
                xsize 800 

                # --- TOP BLOCK: Title and Version ---
                hbox:
                    xalign 0.5
                    spacing 20
                    
                    text "[config.name!t]" style "about_title" yalign 1.0
                    text "v. [config.version!t]" style "about_version" yalign 1.0

                # --- MIDDLE BLOCK: Fake System Diagnostics ---
                vbox:
                    xalign 0.5
                    spacing 8
                    
                    text "> INITIALIZING DIAGNOSTICS..." style "about_sys_text"
                    text "> ENGINE: REN'PY [renpy.version_only]" style "about_sys_text"
                    text "> OS: AI_CORE_v9.9.2" style "about_sys_text"
                    text "> BUILD DATE: 2055.05.02" style "about_sys_text" 
                    text "> LICENSE: SECURED" style "about_sys_text"

                # --- BOTTOM BLOCK: Author Text & Licenses ---
                if gui.about:
                    text "[gui.about!t]" style "about_text" xalign 0.5 text_align 0.5

                # The required Ren'Py license text
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a}.\n\n[renpy.license!t]") style "about_license"


## --- ABOUT SCREEN STYLES ---

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_title:
    font gui.name_text_font # Orbitron
    size 60
    color "#32cd32" # Neon Green
    kerning 3

style about_version:
    font gui.name_text_font
    size 26 # Bumped the size up slightly so it balances well next to the title
    color "#ff8c00" # Orange warning color
    kerning 2

style about_sys_text:
    font gui.text_font # Exo 2
    size 20
    color "#aaaaaa"
    xalign 0.5 # Ensures the console commands stay perfectly centered under the title

style about_text:
    font gui.text_font
    size 22
    color "#ffffff"
    layout "subtitle" 

style about_license:
    font gui.text_font
    size 14
    color "#555555" 
    text_align 0.5
    xalign 0.5

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}"), auto=_("AUTO SAVES"), quick=_("QUICK SAVES"))

    use game_menu(title):

        # We use a vbox to perfectly stack the page numbers on top of the grid
        vbox:
            xalign 0.5
            ypos 50 # Pushes the whole block down slightly
            spacing 40

            # --- THE TOP PAGE NAVIGATION ---
            hbox:
                xalign 0.5
                spacing 25

                textbutton _("<") action FilePagePrevious() style "page_button"
                textbutton _("AUTO") action FilePage("auto") style "page_button"
                textbutton _("QUICK") action FilePage("quick") style "page_button"

                # Generates buttons for Pages 1 through 9
                for page in range(1, 10):
                    textbutton str(page) action FilePage(page) style "page_button"

                textbutton _(">") action FilePageNext() style "page_button"


            # --- THE DATA PACKET GRID (SAVE SLOTS) ---
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                spacing 30 # Nice wide gap between slots

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        style "slot_button" 

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            
                            # 1. Reduce the general spacing so the text lines sit closer together
                            spacing 5 

                            # The Screenshot
                            add Transform(FileScreenshot(slot), size=(360, 220)) xalign 0.5
                            
                            # 2. Add a hardcoded invisible spacer to push the text away from the image!
                            null height 15 

                            # The Timestamp (Custom formatted to look like a system log!)
                            text FileTime(slot, format=_("%Y-%m-%d // %H:%M:%S"), empty=_("EMPTY // NO DATA")):
                                style "slot_time_text"

                            # The Save Name
                            text FileSaveName(slot):
                                style "slot_name_text"


## --- SLOT STYLING ---

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

# Strip the background from the page numbers (<, 1, 2, 3, >)
style page_button:
    background None
    padding (10, 5)

style page_button_text:
    font gui.name_text_font
    size 22
    idle_color "#aaaaaa"
    hover_color "#32cd32"
    selected_idle_color "#32cd32"
    selected_hover_color "#32cd32"

style slot_button:
    xsize 380
    ysize 310 # <-- Increased from 260 to give the text room to breathe!
    padding (15, 15, 15, 15)
    
    # IDLE: Pitch black with a subtle 1px grey border
    idle_background Composite(
        (380, 310),
        (0, 0), Solid("#050505"),
        (0, 0), Transform(Solid("#333333"), xsize=380, ysize=1), # Top
        (0, 309), Transform(Solid("#333333"), xsize=380, ysize=1), # Bottom
        (0, 0), Transform(Solid("#333333"), xsize=1, ysize=310), # Left
        (379, 0), Transform(Solid("#333333"), xsize=1, ysize=310) # Right
    )
    
    # HOVER: Dark green tint, thick 2px Neon Green border
    hover_background Composite(
        (380, 310),
        (0, 0), Solid("#081208"),
        (0, 0), Transform(Solid("#32cd32"), xsize=380, ysize=2), # Top
        (0, 308), Transform(Solid("#32cd32"), xsize=380, ysize=2), # Bottom
        (0, 0), Transform(Solid("#32cd32"), xsize=2, ysize=310), # Left
        (378, 0), Transform(Solid("#32cd32"), xsize=2, ysize=310) # Right
    )

style slot_time_text:
    font gui.name_text_font # Orbitron
    size 18
    idle_color "#aaaaaa"
    hover_color "#32cd32"
    xalign 0.5

style slot_name_text:
    font gui.text_font
    size 16
    color "#ffffff"
    xalign 0.5


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    use game_menu(_("SETTINGS"), scroll="viewport"):

        vbox:
            xfill True
            ypos 50
            spacing 60

            # This hbox splits the screen into a Left Column (Toggles) and Right Column (Sliders)
            hbox:
                xalign 0.5
                spacing 80

                # --- LEFT COLUMN (Display & Skip) ---
                vbox:
                    spacing 40
                    xsize 350

                    if renpy.variant("pc") or renpy.variant("web"):
                        vbox:
                            spacing 15
                            text _("DISPLAY") style "hacker_pref_header"
                            textbutton _("WINDOWED") action Preference("display", "window") style "hacker_radio"
                            textbutton _("FULLSCREEN") action Preference("display", "fullscreen") style "hacker_radio"

                    vbox:
                        spacing 15
                        text _("SKIP") style "hacker_pref_header"
                        textbutton _("UNSEEN TEXT") action Preference("skip", "toggle") style "hacker_radio"
                        textbutton _("AFTER CHOICES") action Preference("after choices", "toggle") style "hacker_radio"
                        textbutton _("TRANSITIONS") action InvertSelected(Preference("transitions", "toggle")) style "hacker_radio"

                # --- RIGHT COLUMN (Sliders & Audio) ---
                vbox:
                    spacing 40
                    xsize 600

                    # Text Sliders
                    vbox:
                        spacing 15
                        text _("TEXT SPEED") style "hacker_pref_header"
                        bar value Preference("text speed") style "hacker_slider"

                    vbox:
                        spacing 15
                        text _("AUTO-FORWARD TIME") style "hacker_pref_header"
                        bar value Preference("auto-forward time") style "hacker_slider"

                    # Audio Sliders
                    if config.has_music:
                        vbox:
                            spacing 15
                            text _("MUSIC VOLUME") style "hacker_pref_header"
                            bar value Preference("music volume") style "hacker_slider"

                    if config.has_sound:
                        vbox:
                            spacing 15
                            text _("SOUND VOLUME") style "hacker_pref_header"
                            hbox:
                                spacing 20
                                bar value Preference("sound volume") style "hacker_slider"
                                if config.sample_sound:
                                    textbutton _("TEST") action Play("sound", config.sample_sound) style "hacker_radio"

                    if config.has_voice:
                        vbox:
                            spacing 15
                            text _("VOICE VOLUME") style "hacker_pref_header"
                            hbox:
                                spacing 20
                                bar value Preference("voice volume") style "hacker_slider"
                                if config.sample_voice:
                                    textbutton _("TEST") action Play("voice", config.sample_voice) style "hacker_radio"

                    if config.has_music or config.has_sound or config.has_voice:
                        vbox:
                            spacing 15
                            textbutton _("MUTE ALL AUDIO") action Preference("all mute", "toggle") style "hacker_radio"


## --- HACKER PREFERENCES STYLES ---
# We delete the messy default GUI styles and build pure, custom ones.

style hacker_pref_header:
    font gui.name_text_font # Orbitron
    size 28
    color "#32cd32" # Neon Green
    kerning 2

style hacker_radio is button
style hacker_radio_text is button_text

style hacker_radio:
    padding (0, 5)
    # We explicitly remove the default radio/checkbox images!
    foreground None 

style hacker_radio_text:
    font gui.text_font # Exo 2
    size 22
    
    # IDLE: Dark Grey
    idle_color "#555555"
    hover_color "#ffffff"
    
    # SELECTED: Neon Green
    selected_idle_color "#32cd32"
    selected_hover_color "#32cd32"

# This uses pure color blocks instead of image files for sliders.
style hacker_slider is bar:
    xsize 525 
    ysize 20
    
    # The empty right side of the bar (Almost black)
    right_bar Solid("#050505")
    
    # The filled left side of the bar (Neon Green)
    left_bar Solid("#32cd32")
    
    # The draggable thumb (Crisp White Block - Sized correctly via Transform!)
    thumb Transform(Solid("#ffffff"), xsize=20, ysize=30) 
    thumb_offset 10


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    # Predict false ensures we don't try to load images for this text-heavy screen
    predict False

    use game_menu(_("SYSTEM LOG // HISTORY"), scroll="vpgrid", yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            # Each history entry is contained within its own box
            frame:
                style "history_entry_box"

                vbox:
                    xfill True
                    spacing 5

                    # THE SPEAKER NAME
                    if h.who:
                        label h.who:
                            style "history_name"
                            
                            # We check if the 'who' matches specific colors so the log matches the game!
                            # (If you add more characters later, you can add them here, or just let them be default green)
                            if h.who == "You":
                                text_color "#4da6ff"
                            elif h.who == "Soldier":
                                text_color "#32cd32"
                            elif h.who == "AI":
                                text_color "#ff4d4d"
                            elif h.who == "SYSTEM BOT":
                                text_color "#ffd700"
                            else:
                                text_color "#32cd32" # Default hacker green

                    # THE DIALOGUE TEXT
                    # We inject our Hacker Arrow directly into the text for the history view!
                    text "> " + h.what:
                        style "history_text"

        if not _history_list:
            text _("LOG EMPTY // NO DATA RECORDED") style "history_empty"


## --- HISTORY STYLES ---

style history_entry_box is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_empty is gui_text

style history_entry_box:
    xfill True
    bottom_padding 15
    bottom_margin 15

style history_name:
    xalign 0.0

style history_name_text:
    font gui.name_text_font # Orbitron
    size 20
    bold True
    kerning 1

style history_text:
    font gui.text_font # Exo 2
    size 22
    color "#aaaaaa"
    xalign 0.0
    # Adds a bit of left margin so the text indents under the name
    left_margin 20 

style history_empty:
    font gui.name_text_font
    size 28
    color "#ff4d4d" # Crimson warning red
    xalign 0.5
    yalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200

    style_prefix "confirm"

    # Darkens the entire screen behind the pop-up to focus the player
    add Solid("#000000cc") 

    frame:
        style "confirm_frame"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40

            # Warning Header
            text _("SYSTEM OVERRIDE REQUIRED:") style "confirm_header" xalign 0.5

            # The actual question (e.g., "Are you sure you want to quit?")
            label _(message):
                style "confirm_prompt"
                xalign 0.5

            # The YES / NO buttons
            hbox:
                xalign 0.5
                spacing 120

                textbutton _("YES") action yes_action style "confirm_button"
                textbutton _("NO") action no_action style "confirm_button"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


## --- CONFIRM SCREEN STYLES ---

style confirm_frame is empty
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    xalign 0.5
    yalign 0.5
    padding (45, 45, 45, 45)
    xsize 600
    
    # We use a smart Frame here so the box automatically stretches 
    # to fit the text, but keeps a 2px Crimson Red border!
    background Frame(Solid("#050505"), outline=(2, "#ff4d4d", 0))

style confirm_header:
    font gui.name_text_font # Orbitron
    size 22
    color "#ff4d4d" # Crimson Red
    kerning 2

style confirm_prompt_text:
    font gui.text_font # Exo 2
    size 24
    color "#ffffff"
    text_align 0.5
    layout "subtitle"

style confirm_button:
    background None
    padding (10, 5)

style confirm_button_text:
    font gui.name_text_font # Orbitron
    size 28
    idle_color "#aaaaaa"
    
    # We make the hover color Neon Green so it feels like a positive/active choice
    hover_color "#32cd32"


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize 12
    unscrollable "hide"
    
    # The Track: A very thin, 2px dark grey wire running horizontally
    base_bar Transform(Solid("#111111"), ysize=2, yalign=0.5)
    
    # The Thumb: A muted green block that sits on the wire
    thumb Transform(Solid("#1e7b1e"), ysize=8, yalign=0.5)
    
    # Hover State: The block lights up pure Neon Green when grabbed!
    hover_thumb Transform(Solid("#32cd32"), ysize=8, yalign=0.5)

style vscrollbar:
    xsize 12
    unscrollable "hide"
    
    # The Track: A very thin, 2px dark grey wire running vertically
    base_bar Transform(Solid("#111111"), xsize=2, xalign=0.5)
    
    # The Thumb: A muted green block that sits on the wire
    thumb Transform(Solid("#1e7b1e"), xsize=8, xalign=0.5)
    
    # Hover State: The block lights up pure Neon Green when grabbed!
    hover_thumb Transform(Solid("#32cd32"), xsize=12, xalign=0.5)

# Ensure the History and Settings screens inherit this new sleek look
style game_menu_vscrollbar is vscrollbar:
    unscrollable "hide"

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900