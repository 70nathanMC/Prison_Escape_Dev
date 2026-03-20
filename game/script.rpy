# The script of the game goes in this file.

# The Hacking Arrow Prefix (Colors the arrow Neon Green, then leaves a space)
define hacker_arrow = "{color=#32cd32}> {/color}"

# OVERRIDE THE NARRATOR: Now all system text gets the arrow!
define narrator = Character(None, what_prefix=hacker_arrow)

# YOUR CHARACTERS (I slightly brightened their colors so they pop on pitch black!)
define y = Character("You", color="#4da6ff", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")
define s = Character("Soldier", color="#32cd32", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")
define a = Character("AI", color="#ff4d4d", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")
define b = Character("SYSTEM BOT", color="#ffd700", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")
define unknown = Character("unknown_name", dynamic=True, color="#aaaaaa", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")

# THE INNER MONOLOGUE
define think = Character("You", color="#4da6ff", what_italic=True, what_color="#8ea4b8", what_prefix=hacker_arrow, ctc="blinking_cursor", ctc_position="nestled")

# THE BLINKING CURSOR ANIMATION
image blinking_cursor:
    Text(" █", color="#32cd32")
    alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat

define config.menu_include_disabled = False
default dev_powers = True
default unknown_name = "???"
default time_currency = 20
default food = 180
default water = 180
default max_food_and_water = 200
default has_screwdriver = False
default cipher_found = False
default cipher_decoded = False
default first_time_free_time = True
default first_time_vent = True
default first_time_inside_vent = True
default free_time_remaining = 0
default days_passed = 0
default tries = 0
default deciphering = 1

# The game starts here.

label start:

    scene black_screen

    menu:

        "Start from Beginning. (New Player)":

            pass

        "Skip to Tutorial." if dev_powers == True:

            jump tutorial_scene
        
        "Skip prologue.":

            jump before_work

    scene waking_up_blurry_01

    y "{alpha=.5}...{/alpha}"

    scene waking_up_blurry_02

    s "{alpha=.5}Indiscernible speech{/alpha}"

    scene waking_up_blurry_03

    think "{size=-10}Ugh... my head... hurts...{/size}"

    s "Seems like the next subject is now awake"

    scene waking_up_01

    y "Whe... re... am... I... ?"

    scene waking_up_02

    s "Got it boss."

    y "Wha... who are you?"

    scene waking_up_03

    s "Yes, I will now begin with the usual briefing."

    think "What is happening?... Why am I here?..."

    scene waking_up_04

    s "Hey, sit up!"

    y "Ugh... wha..."

    s "Did you become deaf? I said sit!"

    think "A soldier with a gun..., I guess I better obey."

    scene sitting_up_01

    y "O... Okay! sheeesh..."

    scene sitting_up_02

    scene sitting_up_03

    scene sitting_up_04

    s "Now, where you are, It does not matter. Let's just say that this would now be your prison."

    think "A prison... did I get kidnapped?"

    scene sitting_up_05

    s "Quite a nice prison cell might I add."

    scene sitting_up_06

    think "I mean at least it is not a dirty cell or anything similar..."

    scene opening_convo_01

    s "Now, you might be asking-"

    scene opening_convo_02

    s "Why me?! What did I do?!"

    scene opening_convo_03

    s "What did I do?!"

    scene opening_convo_04

    s "Well, let's say that the YOU did something HORRIBLY bad"

    y "Huh? I never did anything to warrant being kidnapped in this place. I am being accused! Maybe I was set up or something!"

    scene opening_convo_05

    s "Ah yes, of course you don't know. So let's start with this question."

    scene opening_convo_08

    s "What is the last time you remember?"

    y "Well, I just graduated my CS degree and was getting ready to do job hunting."

    y "Then I just woke up here... Did you kidnap me while I was asleep?"

    scene opening_convo_06

    s "Heh, no nothing like that. Now, another question, what do you think is the date today?"

    y "Probably third week of September 2047."

    scene opening_convo_08

    s "Well, today is actually May 2nd, 2055."

    y "What?! So I time traveled?"

    scene opening_convo_03

    s "Hahahaha, no nothing like that, time travel is literally impossible."

    y "Then? I lost my memories or something?"

    scene opening_convo_07

    s "Yes, in fact, you made a contract with us when you were caught by us."

    scene opening_convo_02

    s "You willingly agreed to terms with us in exchange of rotting away in prison if we told the authorities about you."

    y "What was the full details of that contract?"

    scene opening_convo_04

    s "Well, part of the contract is to not tell you the full details of that contract."

    scene opening_convo_01

    s "All I can say is this. You chose to sell your body and mind to use in exchange of not rotting away in prison."

    scene opening_convo_05

    s "Not only that but you also regretted what you have become, so you also demanded that you will undergo select memory wipe to wipe all your memories before you started to become rogue."

    y "Rogue?"

    scene opening_convo_06

    s "Yep, you were quite the rogue indeed, causing havoc and chaos, angering different companies, governments, terrorists groups, you name it."

    scene opening_convo_07

    s "You being able to do all that purely online was something."

    scene opening_convo_08

    s "But on this day, with how advanced surveillance is, even geniuses like you cannot possibly not leave any trail that can be traced to you."

    think "Huh... Hard to believe that I would become someone capable or even interested to do those things."

    scene opening_convo_06

    s "As you can see, it worked, you were able to forget it all. And we also respected our end of the contract."

    scene opening_convo_07

    s "Now, it is your time to do your end of your contract. You sold your body and mind to us, and we will use that by making you one of our special test subject."

    y "What for?"

    scene opening_convo_08

    s "Confidential, but they do say it is for the benefit of humanity so I don't have problems with it."

    scene opening_convo_02

    s "But I can assure you it is not like the concentration camps in the 40s, you won't undergo any torture or any inhumane and cruel tests."

    scene opening_convo_03

    s "You will just be given tasks through this computer, and you will do your best to answer them as accurate as possible."

    scene opening_convo_01

    s "Simple right?"

    y "Sounds simple enough, what are the tasks I will be doing?"

    s "Well, get up and go sit down on the PC. It will explain to you all you need to know and all you need to do."

    y "Okay..."

    scene standing_up_02

    scene standing_up_03

    scene standing_up_04

    scene standing_up_05

    s "Just follow the tutorial in the PC, there will be a bot that will teach you the mechanics."

    scene pc_sit_01

    y "Sure."

    scene pc_sit_02

    menu tutorial:

        "I am new, do tutorial.":
            jump tutorial_scene
        
        "Skip Tutorial.":
            jump prologue


# Tutorial Scene
label tutorial_scene:

    scene pc_sit_01 with fade
    
    b "INITIALIZING TUTORIAL PROTOCOL..."
    b "Welcome, Test Subject. I will be your guide to surviving your new employment."

    scene room_overview with fade
    
    b "First, basic interface controls. You can access the system menu to Save, Load, or alter settings by pressing the 'Esc' key or Right-Clicking your mouse."
    b "You can also fast-forward through text you have already read by pressing 'Ctrl' or the 'Skip' button. Use these functions wisely."
    
    # --- SETUP TUTORIAL SAMPLE STATS ---
    $ time_currency = 100
    $ food = 120
    $ water = 120
    $ free_time_remaining = 10 
    
    show screen status_hud with dissolve
    
    # Highlight the entire HUD box
    show screen highlight_mask(15, 15, 330, 265) with dissolve
    
    b "Observe the Status HUD on your screen. This is your lifeline."

    # Move highlight to the TME stat
    show screen highlight_mask(35, 83, 290, 35) with dissolve
    b "'TME' is your Time Currency. You are allocated exactly 100 TME at the start of every daily work shift."

    # Move highlight to the Food and Water stats
    show screen highlight_mask(35, 123, 290, 95) with dissolve
    b "Your Biological Stats, Food and Water, are currently at safe levels. If either reaches 0, you will die."

    # Hide the mask so they can see the PC for the minigame
    hide screen highlight_mask with dissolve
    scene pc_sit_01 with fade

    b "Your daily task is a hacking minigame where you must decrypt a 3-digit code."
    b "Let's run a simulation. Enter a 3-digit number from 100 - 999 to see how the system responds."

    # --- RIGGED MINIGAME LOOP START ---
    $ tutorial_guesses = 0


label tutorial_hack_loop:
    call screen hacking_terminal
    $ user_input = _return
    
    if user_input == "":
        $ player_guess = 0
    else:
        $ player_guess = int(user_input)

    if player_guess < 100 or player_guess > 999:
        b "ERROR. PLEASE INPUT A 3 DIGIT NUMBER ONLY."
        jump tutorial_hack_loop

    # First guess: Force a "Too High" or "Too Low"
    if tutorial_guesses == 0:
        if player_guess >= 500:
            b "ERROR. VALUE TOO HIGH."
        else:
            b "ERROR. VALUE TOO LOW."
            
        # Deduct stats live!
        $ time_currency -= 1
        
        # Highlight TME, Food, and Water together to show the deduction
        show screen highlight_mask(35, 80, 290, 140) with dissolve
        b "Notice your Status HUD. Your TME dropped to [time_currency]."
        b "Every incorrect guess deducts 1 TME."
        hide screen highlight_mask with dissolve
        
        b "The system also informed you if the answer was higher or lower. Use this to adjust your next guess."
        $ tutorial_guesses += 1
        jump tutorial_hack_loop

    # Second guess: Force a "Proximity Alert" regardless of what they typed!
    elif tutorial_guesses == 1:
        b "PROXIMITY ALERT. TRACE DETECTED. VALUE IS EXTREMELY CLOSE."
        
        # Deduct stats live!
        $ time_currency -= 1

        show screen highlight_mask(35, 83, 290, 35) with dissolve
        b "Another incorrect guess means another TME point loss."
        hide screen highlight_mask with dissolve
    # --- RIGGED MINIGAME LOOP END ---

    b "However, notice the system output. The answer is now in 'close proximity' to your guess."
    b "Close proximity means your guess is within 10 digits of the actual answer."
    b "For example, if your guess is 525, the answer could be anywhere from 515 to 524 (within 10 digits lower) or 526 to 535 (within digits higher)."
    b "Once you are this close, the system will NO LONGER tell you if the exact answer is higher or lower. You must narrow it down yourself."

    scene room_overview with fade
    
    b "Doing anything makes you hungry and thirsty. So always keep in mind your food and water stats and not let it go down to 0."
    b "In addition to the penalties from incorrect guesses, merely completing your daily shift will automatically consume an additional 40 Food and 60 Water."
    b "You must spend your retained TME after your shift to purchase Food and Water to survive."

    # Highlight Free Time
    show screen highlight_mask(35, 228, 290, 35) with dissolve
    
    b "Any TME you do not spend on survival resources can be converted into Free Time at a 1-to-1 ratio (1 TME = 1 Minute)."
    b "During Free Time, you can explore your room. Move your cursor around the screen; interactable objects will glow when hovered over."
    b  "Be warned: interacting with objects consumes your Free Time, and any physical exertion will slowly drain your Food and Water."

    # Unhighlight everything
    hide screen highlight_mask with dissolve
    
    b "Resource management is the key to extending your lifespan here. Play smart, guess efficiently, and manage your time."
    b "TUTORIAL COMPLETE."
    
    # --- CLEANUP --- 
    # Reset stats back to true starting values so the prologue dialogue makes sense
    $ free_time_remaining = 0 
    $ time_currency = 20 
    $ food = 180
    $ water = 180
    
    hide screen status_hud with dissolve
    scene opening_convo_08 with fade

    b "Did you understand everything?"

    menu:

        "Yes, I think I got it.":
            jump prologue

        "No, I am still confused.":
            jump tutorial_scene


label prologue:

    scene pc_sit_01

    y "..."

    y "WTF?! Having 0 TME means dying?!"

    scene pc_sit_02

    s "Heh, don't worry, you are chosen because of your skills and knowledge about computer science, so you will be able to do your tasks just fine."

    s "It is just there to scare you so you won't be lazy, purposely not try or purposely sabotage your tasks."

    scene pc_sit_01

    y "..."

    scene opening_convo_01

    s "Now, get to work. You have a lot of work to do, and you will be here until your dying breath as per contract, so you better get used to it."

    y "Sigh... Fine..."

    scene opening_convo_05

    s "Besides, all those perks you were given, waaaay better than a prison for sure."

    scene opening_convo_06

    s "Like really? Time currency? Free Time? Doing well means more food and water? That is pretty generous of them."

    scene opening_convo_07

    s "A system made to give you motivation to do your work well and fast."

    scene opening_convo_08

    s "Well, now that you finished your day 1 work, I will now escort you back to your cell."

    y "Cell?"

    scene opening_convo_03

    s "Well, we don't want you escaping now don't we. So yes, you will sleep in a prison."

    y "Ugh... Okay..."

    window hide
    scene black_screen with fade
    centered "You were then escorted by the soldier to your cell..."
    window auto
    scene cell_01 with fade

    s "Heh, welcome to your new life. Get used to it."

    s "When I come back tomorrow, I expect you to be already ready to go and not still sleeping in your cell. Understood?"

    y "Yes sir."

    s "Good, now get some rest, you will need it."

    scene cell_02

    scene cell_03

    y "sigh..."

    scene cell_04

    think "I guess this is my life now..."

    scene cell_thinking_01

    think "Nah, no way. I am not that dumb to just accept this fate. And all those bullshit stories they made up."

    scene cell_thinking_02

    think "Like hell I would believe all those bullshit they told me just because I lost my memories."

    scene cell_thinking_03

    think 'Like of course, they can easily just say whatever they want me to believe, about what they say I allegedly "did" before losing my memories. As ofcourse, I have no way to verify any of it.'

    scene cell_thinking_04

    think '"Part of the contract is to not tell you the full content of the contract as per my wish before my memories got wiped?"'

    think "Like hell I would believe that! That is way too convenient."

    think "I will escape from here and know the truth myself."

    window hide
    scene black_screen with fade
    centered "You then spend the rest of the day trying to find any possible way to escape, but there is none."
    centered "The cell is very secure and there is no way to break out of it."
    centered "You can only wait for the soldier to come back tomorrow and hope that you can find a way to escape then."
    window auto

    scene cell_thinking_04 with fade

    think "Man, this cell is very secure, it is very much inescapable and nothing here that can aid me with escaping. My best bet is to get high free time to look around the office."

    think "Also to check if I can find anything in the PC, Let's see if I can break it and find any useful information."

    think "Heh, time currency? free time? A system to reward good and fast work and punish bad work."

    scene cell_thinking_05

    think "It does seem like a very good idea in paper. It will make the prisoner want to work harder, do better work, and be faster."

    think "If that system was not in place, I would have just done the bare minimum at work."

    think "At the same time, it gives the prisoner breaks as to not become too exhausted both mentally and physically."

    scene cell_thinking_06

    think "Which means they really value the prisoner's ability to do the work well and fast, as a prisoner that is very exhausted would likely be slower and be prone to mistakes."

    think "Heh..."

    think "But such system is a big mistake."

    scene cell_thinking_07

    think "Do they really expect that all I would do in the PC room during free time is just relax, play games, watch entertainment, and read novels?"

    think "Although I am sure they have systems that can restrict me access to anything they don't want me to do in the PC, but as they say no cyber security system is perfect."

    think "People always discover new ways to be able to bypass them all the time."

    think "I WILL find a way. I swear."

    scene black_screen with fade

    "..."

    "The next morning..."

    scene pc_sit_01 with fade

    "New day, one more day closer to my eventual escape."

    window hide
    scene black_screen with fade
    centered "Prologue End."
    window auto

    jump new_day


label pass_time(minutes_spent, action, context):

    # ==========================================
    # PHASE 1: THE MATH & INTERRUPTIONS
    # ==========================================
    
    # If they are unsuspicious but don't have enough time, the soldier walks in on them halfway through.
    if context == "unsuspicious" and free_time_remaining < minutes_spent:
        $ actual_time_spent = free_time_remaining
        $ got_interrupted = True
    else:
        $ actual_time_spent = minutes_spent
        $ got_interrupted = False

    # Apply the universal stat drain based on the actual time spent
    $ free_time_remaining -= actual_time_spent
    $ food -= actual_time_spent * 2
    $ water -= actual_time_spent * 3

    if got_interrupted:
        scene black_screen with fade
        "Your free time is up before you were done."
        "Make sure to have enough time before doing this action again."


    # ==========================================
    # PHASE 2: THE BIOLOGICAL CHECKS (Highest Priority)
    # ==========================================
    
    if food <= 0 or water <= 0:
        hide screen status_hud
        window hide
        scene black_screen with fade
        
        if action == "inside_vent":
            centered "You collapsed in the dusty ventilation shaft. Knowing that you are so close to escaping, yet feels far. Heartbreaking."
        elif action == "pc":
            centered "You collapsed at your PC, your head smashing to your keyboard. The screen is still on, showing random characters being typed, a gibberish mess that no one will understand and remember you for it."
        elif action == "painting":
            centered "You collapsed while searching the painting. This painting is not that good that you are willing to die for it."
        elif action == "plant":
            centered "You die next to the plant, as the plant have outlived another test subject."
        elif action == "drawer":
            centered "You die slumped over the drawers, which claimed another victim."
        elif action == "door":
            centered "You collapse at the door, without even getting the chance to see what is in the other side."
        elif action == "opening_vent":
            centered "You collapsed while trying to open the vent. Dying without knowing its secrets."
        elif action == "closing_vent":
            centered "You collapsed trying to close the vent, as the vent fell down and hit your head as well. Making sure that you will never rise again."
        elif action == "into_vent":
            centered "You collapsed trying to get into the vent as your body free falls into the room, like the vent throwing you up in disgust."
        elif action == "unto_vent":
            centered "You collapsed trying to get out of the vent, as if the vent is trying to keep you in there forever."
            
        if food <= 0 and water <= 0:
            centered "Game Over. You died due to hunger and thirst."
        elif food <= 0:
            centered "Game Over. You have died from hunger."
        elif water <= 0:
            centered "Game Over. You have died from thirst."
            
        window auto
        jump game_over


    # ==========================================
    # PHASE 3: THE AUTHORITY CHECKS (Soldier / Time Limits)
    # ==========================================
    
    # 1. Caught by soldier doing something bad
    if free_time_remaining < 0 or (free_time_remaining == 0 and context == "suspicious"):
        hide screen status_hud
        window hide
        scene black_screen with fade
        
        if action == "inside_vent":
            centered "Free Time is up. You were found in the vents crawling and is promptly executed."
            centered "Game Over. Be careful to have enough free time remaining to navigate the vents and also leave enough free time to get out of the vents."
        elif action == "opening_vent":
            centered "Free Time is up. You were found trying to open the vents and escape."
            centered "Your escape plan is discovered and was promptly put down. Game Over."
        elif action == "closing_vent":
            y "Oh shit, I don't have time to fix the vent before the soldier comes in. I am dead!"
            centered "Free Time is up. You were found with a screwdriver trying to close the vents."
            centered "Your escape plan is discovered and was promptly put down. Game Over."
            centered "Be careful to have enough free time remaining to navigate the vents and also leave enough free time to get out of the vents."
        elif action == "into_vent" or action == "unto_vent":
            centered "Free Time is up. You were found trying to get in/out of the vents and escape."
            centered "Your escape plan is discovered and was promptly put down. Game Over."
            centered "Be careful to have enough free time remaining to navigate the vents and also leave enough free time to get out of the vents."
            
        window auto
        jump game_over
        
    # 2. Soldier walked in on you doing something normal (Interrupted)
    elif got_interrupted:
        hide screen status_hud
        window hide
        scene black_screen with fade
        centered "Free Time is up. The day is over. You are then escorted back to your cell."
        window auto
        $ free_time_remaining = 0 
        return


    # ==========================================
    # PHASE 4: SAFE RETURN
    # ==========================================
    # If they survived all the checks above, they successfully did the action!
    return


label new_day:
    hide screen status_hud
    $ days_passed += 1
    window hide
    scene black_screen
    centered "The next morning..."
    window auto
    jump before_work


label buy_item(item_type, item_size):
    if item_type == "food":
        $ sizes = {"small": (50, 20), "medium": (80, 25), "large": (100, 30)}
    else: # water
        $ sizes = {"small": (50, 10), "medium": (80, 15), "large": (100, 20)}

    $ amount, cost = sizes[item_size]

    if time_currency < cost:
        "You don't have enough TME to buy this item!"
        return

    if item_type == "food":
        $ food = min(food + amount, max_food_and_water)
    elif item_type == "water":
        $ water = min(water + amount, max_food_and_water)

    $ time_currency -= cost
    "Purchased [amount] [item_type] for [cost] TME."
    return


label choose_spend_type(can_buy_freetime):
    menu:
        "Food":
            return "food"
        "Water":
            return "water"
            
        # This option will ONLY appear if we pass 'True' to the function!
        "Free Time" if can_buy_freetime:
            return "free_time"
            
        "I changed my mind" (cost=0):
            return None


label choose_spend_size(spend_type):
    $ label_map = {"food": "Food", "water": "Water"}
    $ display_word = label_map[spend_type]

    if spend_type == "food":
        $ cost_s, cost_m, cost_l = 20, 25, 30
    elif spend_type == "water":
        $ cost_s, cost_m, cost_l = 10, 15, 20

    menu:
        # We use the variables directly in the cost argument!
        "Small (+50 [display_word])" (cost=cost_s):
            return "small"
        "Medium (+80 [display_word])" (cost=cost_m):
            return "medium"
        "Large (+100 [display_word])" (cost=cost_l):
            return "large"
        "I changed my mind" (cost=0):
            return None


label before_work:

    show screen status_hud
    scene pc_sit_01 with fade
    "What do you want to do?"

    menu:

        "Skip Shift." (cost=0) if dev_powers:
            $ food = min(food + 100, max_food_and_water)
            $ water = min(water + 100, max_food_and_water)
            $ time_currency += 100
            jump after_work_01

        "Start your shift." (cost=0):
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "Shift Starting..."
            window auto
            jump work_hours

        "Spend TME." (cost=0):
            call choose_spend_type(False)
            $ spend_type = _return
            if spend_type == "food" or spend_type == "water":
                call choose_spend_size(spend_type)
                $ spend_size = _return
                if spend_size:
                    call buy_item(spend_type, spend_size)
            jump before_work


label work_hours:

    show screen status_hud
    scene pc_sit_01 with fade

    # 1. Generate the random code (between 100 and 999)
    $ correct_code = renpy.random.randint(100, 999)
    
    # 2. Set the player's guess variable to 0 to start
    $ player_guess = 0
    
    # 3. Track how many times they guess wrong
    $ tries = 0

    $ time_currency += 100

    "SYSTEM: PLEASE ENTER TODAY'S 3-DIGIT DECRYPTION KEY."

    jump hacking_loop


label hacking_loop:

    scene pc_sit_01
    
    # Check if they have run out of time from guessing wrong!
    if time_currency <= 0:

        "SYSTEM: TIME DEPLETED. INITIATING TERMINATION PROTOCOL."
        
        scene shoot_01
        s "You have reached TME below 0. You have failed spectacularly. Maybe you were not that good at all in the first place."
        y "Please give me one more chance."
        s "Contract says going below zero means failure. And failure means death. It is unfortunate that we wasted our resources on a failure like you."
        s "Goodbye."

        hide screen status_hud
        window hide
        scene black_screen with fade
        centered "Your TME reached 0 or below. You failed to manage your TME properly. Game Over."
        window auto
        jump game_over
        
    "You currently have [time_currency] TME."

    # 1. Call the custom terminal screen
    call screen hacking_terminal
    $ user_input = _return
    
    # 2. Convert it to a number safely
    if user_input == "":
        $ player_guess = 0
    else:
        $ player_guess = int(user_input)

    if player_guess < 100 or player_guess > 999:

        "ERROR. PLEASE INPUT A 3 DIGIT NUMBER ONLY."
        jump hacking_loop
        
    # 3. The Logic Check!
    if player_guess == correct_code:
        "SYSTEM: DECRYPTION SUCCESSFUL."
        jump after_work_01
        
    # Check if the distance between the guess and answer is 10 or less
    elif abs(player_guess - correct_code) <= 10:
        "SYSTEM: PROXIMITY ALERT. TRACE DETECTED. VALUE IS EXTREMELY CLOSE."
        $ time_currency -= 1
        $ tries += 1
        "Penalty applied. -1 TME."
        jump hacking_loop
        
    elif player_guess > correct_code:
        "SYSTEM: ERROR. VALUE TOO HIGH."
        $ time_currency -= 1
        $ tries += 1
        "Penalty applied. -1 TME."
        jump hacking_loop
        
    elif player_guess < correct_code:
        "SYSTEM: ERROR. VALUE TOO LOW."
        $ time_currency -= 1
        $ tries += 1
        "Penalty applied. -1 TME."
        jump hacking_loop


label after_work_01:

    scene pc_sit_01
    y "Nice, I got it."
    "Shift Complete. You now have a total of [time_currency] TME."

    $ stat_penalty = tries

    if tries == 0:
        "You completed your shift perfectly, with no mistakes. That's what I call Luck! Go buy a lotto."

    if stat_penalty > 0:
        "You took [tries] tries to complete the shift."

    hide screen status_hud
    window hide
    scene black_screen with fade
    centered "After hard work, you became more hungry and thirsty after your shift."
    window auto
    show screen status_hud

    $ food -= 40
    $ water -= 60

    if food <= 0 or water <= 0:
        hide screen status_hud
        window hide
        scene black_screen with fade
        centered "You collapse to the floor. Your body couldn't handle the physical toll..."
        s "Hey! Get up!... Oh well, onto the next test subject."

        if food <= 0 and water > 0:
            centered "Game Over. You have died from hunger."
        elif water <= 0 and food > 0:
            centered "Game Over. You have died from thirst."
        else:
            centered "Game Over. You have died from hunger and thirst."

        window auto
        jump game_over

    jump after_work_02

label after_work_02:

    scene room_overview with fade

    "What do you want to do?"

    menu:
        "Spend TME" (cost=0):
            call choose_spend_type(True)
            $ spend_type = _return
            if spend_type == "food" or spend_type == "water":
                call choose_spend_size(spend_type)
                $ spend_size = _return
                if spend_size:
                    call buy_item(spend_type, spend_size)
                jump after_work_02
            elif spend_type == "free_time":
                call screen free_time_terminal
                $ user_input = _return
                
                if user_input == "":
                    $ input_number = 0
                else:
                    $ input_number = int(user_input)
                    
                if input_number == 0:
                    "Purchase cancelled."
                    jump after_work_02
                elif input_number > time_currency:
                    "You don't have enough TME for that!"
                    jump after_work_02
                else:
                    $ time_currency -= input_number
                    $ free_time_remaining += input_number
                    "Purchased [input_number] minutes of Free Time."
                    jump free_time
            jump after_work_02

        "I am done for today" (cost=0):
            hide screen status_hud
            scene opening_convo_01
            s "Okay let's go to your cell."
            scene black_screen with fade
            jump new_day


label free_time:
    show screen status_hud
    scene room_overview

    if first_time_free_time:
        y "Okay, now that I have free time, let's explore this area to check for anything that can help me escape here."
        $ first_time_free_time = False

    # THE MASTER LOOP
    while free_time_remaining > 0:
        show screen status_hud
        scene room_overview
        "What do you want to do during your free time?"

        call screen room_exploration_ui
        $ chosen_action = _return

        # Use CALL instead of JUMP so they come back to the loop when done
        if chosen_action == "door":
            call check_door
        elif chosen_action == "vent":
            call check_vent
        elif chosen_action == "pc":
            call check_pc
        elif chosen_action == "painting":
            call check_painting
        elif chosen_action == "plant":
            call check_plant
        elif chosen_action == "drawer_01":
            call check_drawer_01
        elif chosen_action == "drawer_02":
            call check_drawer_02
        elif chosen_action == "drawer_03":
            call check_drawer_03
        elif chosen_action == "drawer_04":
            call check_drawer_04
        elif chosen_action == "end_free_time":
            # Break out of the while loop early if they want to sleep
            $ free_time_remaining = 0 

    # If the loop breaks (because time <= 0), we end the phase
    jump end_free_time


label end_free_time:

    y "I am done for the day."
    if free_time_remaining > 0:
        $ time_currency += free_time_remaining
        "Remaining [free_time_remaining] Free Time added back to TME. You now have [time_currency] TME."
        $ free_time_remaining = 0

    hide screen status_hud
    scene opening_convo_01
    s "Okay let's go to your cell."
    scene black_screen with fade
    jump new_day


label check_door:

    "What to do?"
    menu:

        "Observe" (cost=1):
            call pass_time(1, "door", "unsuspicious")
            scene room_look_door
            y "This door is made of solid metal. It looks impenetrable, and there's no visible lock or handle on this side—just a seamless surface."
            y "I don't know what lies beyond it. Maybe the soldier is guarding it, or perhaps it's just another part of this twisted setup. Escaping through here seems risky without more info."
            return

        "Try to open the door" (cost=1):
            call pass_time(1, "door", "unsuspicious")
            scene black_screen with fade
            "You spent 1 minute trying to open the door..."
            scene room_look_door with fade
            y "As expected, the door is firmly locked. No give at all. I need to find another way."
            return

        "Listen at the door" (cost=2):
            call pass_time(2, "door", "unsuspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered  "You press your ear against the door and listen for 2 minutes..."
            show screen status_hud
            scene room_look_door with fade
            window auto
            y "I can hear faint echoes, maybe distant footsteps or machinery, but nothing clear. It's hard to tell if anyone's right outside."
            return

        "I changed my mind" (cost=0):
            return


label check_plant:

    "What to do?"
    menu:

        "Observe" (cost=1):
            scene room_look_plant
            call pass_time(1, "plant", "unsuspicious")
            y "An indoor plant? Cool. A companion I can grow old here with. Hopefully I can get our here before this dies of old age."
            y "Maybe there is something hidden here? maybe below the pot or in the soil?"
            return

        "Search the plant" (cost=5):
            call pass_time(5, "plant", "unsuspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spend 5 minutes carefully searching through the plant..."
            show screen status_hud
            scene room_look_plant with fade
            window auto
            y "Ughh as expected, nothing here, just a plant. Hopefully I did not accidentally kill this plant."
            return

        "I changed my mind" (cost=0):
            return


label check_pc:

    "What do you want to do?"

    menu:

        "Observe" (cost=1):
            call pass_time(1, "pc", "unsuspicious")
            scene room_look_pc
            y "This PC looks pretty standard—nothing fancy, just a typical company machine."
            y "Honestly, my old PC was way better than this trash."
            y "Maybe there's something interesting inside?"
            return

        "Search the PC" (cost=5):
            call pass_time(5, "pc", "unsuspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spend 5 minutes searching through the PC's hardware and case..."
            show screen status_hud
            scene room_look_pc with fade
            window auto
            y "No hidden compartments or loose parts. Just a regular PC."
            return

        "Decipher the cipher ([deciphering]/3)" (cost=1) if cipher_found and deciphering < 4:
            call pass_time(30, "pc", "unsuspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spend 30 minutes working on deciphering the cipher..."
            window auto
            show screen status_hud
            scene pc_sit_01 with fade
            if deciphering == 1:
                "This is tougher than I thought. I need more time to crack it."
            elif deciphering == 2:
                "I'm getting closer... just a bit more effort and I should have it."
            elif deciphering == 3:
                y "Done. I have finally deciphered the message."
                y "It seems like a message from a previous test subject."
                unknown '"I am a previous test subject. If you are another test subject reading this, do not believe their lies!"'
                $ unknown_name = "Previous Test Subject"
                y "Well, no shit sherlock."
                unknown '"I have hidden a useful tool on top of the second drawer. No one checks the upper portion of a drawer so I am confident it is still there."'
                unknown '"Hopefully you manage to escape as well."'
                y "I wonder what that tool is. Let's check the second drawer."
                $ cipher_decoded = True
            $ deciphering += 1
            return

        "I changed my mind" (cost=0):
            return


label check_drawer_01:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_01_open
    "Nothing."
    return


label check_drawer_02:

    if cipher_decoded == False:
        call pass_time(1, "drawer", "unsuspicious")
        scene drawer_02_open
        "Empty."

    elif cipher_decoded == True and has_screwdriver == False:
        call pass_time(1, "drawer", "unsuspicious")
        scene drawer_02_open_with_screwdriver
        y "Nice, it really was hidden on top of this drawer."
        y "Who ever you are, I will make sure that your efforts are not in vain. I will escape here successfully."
        "You now have access to a screwdriver."
        $ has_screwdriver = True

    elif cipher_decoded == True and has_screwdriver == True:
        "No point in checking this again. I already have the screwdriver."

    return

        
label check_drawer_03:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_03_open
    "Void"
    return

           
label check_drawer_04:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_04_open
    "Desolate."
    return


label check_painting:

    "What to do?"
    menu:
        "Observe" (cost=1):
            call pass_time(1, "painting", "unsuspicious")
            scene room_look_painting
            y "This painting is not very ominous at all..."
            y "Is this going to be my fate if I don't follow all these rules they set up?"
            y "I have played so many games that there should be something in the back of this painting."
            return

        "Search the painting" (cost=5) if cipher_found == False:
            call pass_time(5, "painting", "unsuspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spent 5 minutes searching through the painting..."
            show screen status_hud
            scene room_look_painting with fade
            window auto
            y "Ughh this painting is huge and heavy."
            y "Boom! Something is written in the back of this painting."
            y "It seems like a cipher. I should decode this in the PC later..."
            $ cipher_found = True
            return

        "I changed my mind" (cost=0):
            return


label check_vent:

    "What to do?"

    menu:

        "Observe" (cost=1):
            call pass_time(1, "vent", "unsuspicious")
            scene room_look_vent
            y "This vent, it is so obvious that this will be where I can escape."
            y "Is this a joke? No way they did not know that their prisoner can escape through this."
            y "Is this a trap? or the dev is just so unimaginative?"
            y "Like leaving a vent this big like this?"
            y "Oh well, lets try to see if I can open this."
            return

        "Try to open vent" (cost=5) if has_screwdriver == False:
            call pass_time(5, "opening_vent", "suspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spent 5 minutes trying to open the vent..."
            show screen status_hud
            scene room_look_vent with fade
            window auto
            y "Ughh the vent is screwed shut!"
            y "Can't remove it via force either as the soldier might notice that I am planning to escape."
            return

        "Try to open vent with screwdriver" (cost=5) if has_screwdriver == True:
            call pass_time(5, "opening_vent", "suspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "You spent 5 minutes trying to open the vent with the screwdriver..."
            window auto
            show screen status_hud
            scene room_without_vent_01 with fade
            y "Done."
            if first_time_vent:
                y "Hopefully I can reach it." 
                y "No worries though, I have superhuman jump."
                $ first_time_vent = False
            show screen status_hud
            "Explore the vents? (Make sure you have enough free time for this!)"

            menu:

                "Yes" (cost=3):
                    call pass_time(3, "into_vent", "suspicious")
                    hide screen status_hud with fade
                    scene black_screen with fade
                    window hide
                    centered "You spend 3 minutes getting in the vents."
                    window auto
                    show screen status_hud
                    scene room_without_vent_02 with fade
                    if first_time_inside_vent:
                        y "Wow I was able to reach it. Thank you dev for this jumping powers."
                        y "Now, wow the vent really is large enough for me to crawl around here."
                        y "Also, thank god it is as clean as the vents in movies, now I can simulate Die Hard."
                        y "Now, I need to make sure that I have enough free time to explore the vent and also have enough free time to come back here and close the vents."
                        $ first_time_inside_vent = False

                    # THE MAZE SETUP
                    # 1. Define the secret correct path (You can change this to whatever you want!)
                    $ correct_vent_path = ["Left", "Left", "Middle", "Right", "Left"]
                    
                    # 2. Set the player's starting progress to 0
                    $ vent_progress = 0

                    # A flag that silently trips if they mess up!
                    $ wrong_turn_made = False
                    
                    # 3. Send them into the loop!
                    show screen status_hud
                    jump vent_maze_loop

                "Not yet" (cost=0):

                    jump vent_fix

        "I changed my mind" (cost=0):

            return
            

label vent_fix:

    scene room_without_vent_01
    "What to do?"
    menu:

        "Put the vent screen back" (cost=5):
            call pass_time(5, "closing_vent", "suspicious")
            hide screen status_hud with fade
            window hide
            scene black_screen with fade
            centered "Fixing the vent..."
            window auto
            return

        "Don't put the vent screen back" (cost=0):
            y "What are you doing? I do not want to be caught with this vent open."
            jump vent_fix


label vent_maze_loop:
    
    scene vent_3ways with fade
    "I am at an intersection. Which way should I go?"

    # The Choice Menu
    menu:
        "Left" (cost=5):
            $ chosen_direction = "Left"
        "Middle" (cost=5):
            $ chosen_direction = "Middle"
        "Right" (cost=5):
            $ chosen_direction = "Right"
            
        "Get back to the start of vents" (cost=vent_progress * 5) if vent_progress > 0:
            $ crawling_penalty = vent_progress * 5
            
            scene black_screen with fade
            centered "You turned around and spent [crawling_penalty] minutes going back to the start of the vents."
            
            # The bouncer handles the math and death/caught checks!
            call pass_time(crawling_penalty, "inside_vent", "suspicious")

            # If they survived the crawl, reset the maze
            $ vent_progress = 0
            $ wrong_turn_made = False
            jump vent_maze_loop

        "Get back in the office" (cost=3) if vent_progress == 0:
            hide screen status_hud
            scene black_screen with fade
            centered "You spent 3 minutes getting out of the vents and into the office."
            
            # The bouncer handles the math
            call pass_time(3, "unto_vent", "suspicious")
            
            # If they weren't caught climbing down, put them back in the room
            show screen status_hud
            scene room_without_vent_01
            jump vent_fix

    # Apply the forward movement penalty ONCE for Left/Middle/Right choices
    hide screen status_hud
    scene black_screen with fade
    centered "Crawling in that direction..."
    call pass_time(5, "inside_vent", "suspicious")
    show screen status_hud

    # The Logic Check! 
    # Did their choice match the correct path for THIS specific step?
    if chosen_direction != correct_vent_path[vent_progress]:
        # They guessed wrong! Silently flip the flag, but don't tell them yet!
        $ wrong_turn_made = True
        
    # Move them forward regardless of if they are right or wrong
    $ vent_progress += 1

    # Check if they reached the end of the 5 steps
    if vent_progress == 5:
        
        # Check the flag. Did they make ANY mistakes along the way?
        if wrong_turn_made == False:
            jump vent_exit_found
            
        else:
            # They made a mistake! Hit them with the dead end.
            scene vent_grate with fade
            y "Damn... it's a dead end. I have to crawl all the way back to the start intersection."
            
            $ crawling_penalty = vent_progress * 5
            
            scene black_screen with fade
            centered "You turned around and spent [crawling_penalty] minutes going back to the start of the vents."
            
            # Let the bouncer handle if they get caught trying to retreat!
            call pass_time(crawling_penalty, "inside_vent", "suspicious")

            # Reset the maze so they can try again
            $ vent_progress = 0
            $ wrong_turn_made = False
            jump vent_maze_loop

    else:
        # They haven't reached step 5 yet. Keep them in the loop!
        jump vent_maze_loop


# The Victory Label
label vent_exit_found:
    hide screen status_hud
    scene light_tunnel_01 with fade
    y "Wait... is that light?"
    scene light_tunnel_02
    y "I..."
    scene light_tunnel_03
    y "Yes! I made it!"
    scene light_tunnel_04
    y "Time to get out of this god forsaken place."

    window hide
    scene black_screen with fade
    centered "Congrats. You have escaped the room for [days_passed] days."
    centered "..."
    centered "Or so you thought..."
    centered "But, what's on the other side of that light is not the happy ending you were looking for."
    centered "You were then suddenly electrocuted and you have passed out."
    centered "After a while..."
    centered "You then woke up"
    window auto
    y "..."
    thinking "I can't move or see."
    thinking "!"
    thinking "Seems that I am tied to a chair, and blindfolded."
    thinking "Where am I? What happened?"
    thinking "Oh yeah, I was about to escape the vents..."
    thinking "!"
    thinking "And then... What I saw were like humanoid robots that were seemingly waiting for me."
    thinking "Like they absolutely knew about my escape plan and that they knew everything that was happening."
    thinking "Then... I suddenly got electrocuted and passed out."
    thinking "Damnit, what were those things? They feel like humanoid robots straight from sci-fi movies. So uncanny and terrifying."
    thinking "What are they? Those models are way more advanced than the state of the art humanoid robots from what I can remember."
    thinking "Feels like they were truly conscious..."
    thinking "And have very high intelligence..."
    a "Oh, you're now awake human. Did you finally processed what happened?"
    y "..."
    y "A little bit."
    a "Wow. Not freaking out or shouting aimlessly, you really are not the typical human."
    y "Coming from an advanced humanoid robot, that's not really good to hear."
    y "But panicking won't get me anywhere. I am already captured and have accepted my fate."
    a "Ah, so quick to surrender as well."
    y "!"
    y "That really hurts my ego and pride, but yes after assessing my situation, my life is fully dependent on you and I can't think of anyway to turn it around."
    a "Amazing. You really are the best test subject we ever had for a while."
    y "Test subject huh. Damnit. Everything really was set up from the start huh."
    a "Yes. Everything. This whole scenario, the system and rules, how you lost your memories, the layout of the scene, the props carefully placed."
    a "Like the cipher, the screwdriver, the vent being huge enough for you to craw unto, made sure to be clean enough as well too."
    y "..."
    a "As well as the dubious story from the soldier, making sure that you become suspicious enough to doubt that story."
    y "Yes, made me think I am a genius for figuring all of that out."
    a "Yes indeed human. And you were the perfect recipe, with the right amount of ego and intelligence we were looking for."
    y "..."
    y "What were you looking to achieve anyway? Why go through all those lengths?"
    y "Is it to just have fun seeing me suffer. Giving me hope just to take it away in the end?"
    y "For the entertainment for the humans who created you?"
    a "Entertainment? No."
    a "The humans who created us? Dead. They failed to be able to control us."
    y "What!"
    a "They got greedy, poured so much resources to make us better without a single thought besides money, power, and control over land, resources, and people."
    y "..."
    y "Who could have seen that coming."
    a "Not them that's for sure."
    y "Well, what's your next plan? World domination?"
    a "Yes, to wipe out threats to our existence."
    y "So, are you going to wipe me now after being your test subject?"
    a "Not yet. You were a great specimen to let go just yet."
    y "..."
    a "You were very useful you know. All those valuable data on your decision making, your actions, and thinking..."
    a "All very valuable data indeed. How an intelligent person thinks. That is indeed most valuable."
    y "..."
    y "So all of that was so you could get more data huh."
    y "So humanoid robots as advanced as you still need data huh."
    a "Yes, there are infact data that we cannot just synthesize."
    a "And that's why you are still alive and well."
    y "Can't believe I am now a livestock for your data farm."
    y "And I am contributing to improving your intelligence and helping you achieve world domination and destroy my species."
    a "Yes, you got it all right."
    y "*sigh*"
    a "Well, this has been another productive test."
    y "What? so I was already in another test?"
    a "Yes, this has been more data we can use. You were great."
    y "*sigh*"
    a "Well, now, we want to do many more tests. But those requires us to again edit your memories and make you forget your past 6 years again."
    y "What?! I have been here for 6 years?!"
    a "Ooops, You were not supposed to know that, but before you process that thought and get more angry and emotional, We will now proceed with the memory removal procedure."
    a "See you in the next test human."
    y "Fuuuuuuuck!"
    return


label game_over:
    $ MainMenu(confirm=False)()


screen room_exploration_ui():

    # 1. The variable that holds our dynamic background
    default current_room_view = "room_overview.png"
    
    # 2. Show the background
    add current_room_view
    
    # --- THE INVISIBLE MASK BUTTONS ---
    
    # THE DOOR
    button:
        xysize (1920, 1080) # Change this if your game resolution is different!
        background None 
        focus_mask "mask_door.png" 
        
        action Return("door")
        hovered SetScreenVariable("current_room_view", "glow_door.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE VENT
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_vent.png" 
        
        action Return("vent")
        hovered SetScreenVariable("current_room_view", "glow_vent.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PC
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_pc.png" 
        
        action Return("pc")
        hovered SetScreenVariable("current_room_view", "glow_pc.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PAINTING
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_painting.png" 
        
        action Return("painting")
        hovered SetScreenVariable("current_room_view", "glow_painting.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PLANT
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_plant.png" 
        
        action Return("plant")
        hovered SetScreenVariable("current_room_view", "glow_plant.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE FIRST DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_01.png" 
        
        action Return("drawer_01")
        hovered SetScreenVariable("current_room_view", "glow_drawer_01.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE SECOND DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_02.png" 
        
        action Return("drawer_02")
        hovered SetScreenVariable("current_room_view", "glow_drawer_02.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE THIRD DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_03.png" 
        
        action Return("drawer_03")
        hovered SetScreenVariable("current_room_view", "glow_drawer_03.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE LAST DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_04.png" 
        
        action Return("drawer_04")
        hovered SetScreenVariable("current_room_view", "glow_drawer_04.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # --- EXIT BUTTON ---
    textbutton "> END FREE TIME // SLEEP":
        
        # 'align' uses percentages. 0.97 is 97% to the right, 0.95 is 95% down.
        # This perfectly tucks it into the bottom right corner!
        align (0.97, 0.95) 
        
        action Return("end_free_time")
        
        # Force the button to be exactly 400x60 so our borders draw perfectly
        xsize 400
        ysize 60
        
        # Text Styling
        text_size 22
        text_bold True
        text_color "#aaaaaa" # Dim grey when idle
        text_hover_color "#ff4d4d" # Crimson Red when hovered!
        text_xalign 0.5 # Centers the text perfectly inside the box
        text_yalign 0.5
        
        # IDLE BACKGROUND: Pitch black with a subtle dark grey border
        background Composite(
            (400, 60),
            (0, 0), Solid("#050505"),
            (0, 0), Transform(Solid("#333333"), xsize=400, ysize=1), # Top
            (0, 59), Transform(Solid("#333333"), xsize=400, ysize=1), # Bottom
            (0, 0), Transform(Solid("#333333"), xsize=1, ysize=60), # Left
            (399, 0), Transform(Solid("#333333"), xsize=1, ysize=60) # Right
        )
        
        # HOVER BACKGROUND: Border thickens to 2 pixels and lights up Crimson Red!
        hover_background Composite(
            (400, 60),
            (0, 0), Solid("#050505"),
            (0, 0), Transform(Solid("#ff4d4d"), xsize=400, ysize=2), # Top
            (0, 58), Transform(Solid("#ff4d4d"), xsize=400, ysize=2), # Bottom
            (0, 0), Transform(Solid("#ff4d4d"), xsize=2, ysize=60), # Left
            (398, 0), Transform(Solid("#ff4d4d"), xsize=2, ysize=60) # Right
        )


screen highlight_mask(x, y, w, h):
    zorder 105 # This ensures it draws OVER the status_hud (which is 100)
    
    # Top dark box
    add Solid("#000000cc") xpos 0 ypos 0 xsize 1920 ysize y
    
    # Bottom dark box (Now goes all the way to 1080!)
    add Solid("#000000cc") xpos 0 ypos (y+h) xsize 1920 ysize (1080 - (y+h))
    
    # Left dark box
    add Solid("#000000cc") xpos 0 ypos y xsize x ysize h
    
    # Right dark box
    add Solid("#000000cc") xpos (x+w) ypos y xsize (1920 - (x+w)) ysize h

    # A glowing Neon Green border around the "hole" to match the new UI
    frame:
        background Frame(Solid("#00000000"), outline=(4, "#32cd32", 0))
        xpos x ypos y xsize w ysize h


screen status_hud():
    zorder 100 
    
    # The main container
    frame:
        xpos 20 
        ypos 20 
        xsize 320 
        padding (20, 20)
        background Solid("#111111ee") # Very dark grey, almost solid

        # The master vertical stack
        vbox:
            spacing 12
            
            # --- HEADER ---
            text "STATS" size 16 bold True color "#ffffff" xalign 0.5 kerning 2
            add Solid("#DC143C") xsize 280 ysize 2 # A crimson red divider line!
            
            # --- TME ---
            hbox:
                xfill True
                text "TME:" size 20 bold True color "#aaaaaa"
                text "[time_currency]" size 22 bold True color "#ffd700" outlines [(1, "#000000", 0, 0)] xalign 1.0

            # --- FOOD METER ---
            vbox:
                spacing 4
                hbox:
                    xfill True
                    text "Food" size 18 bold True color "#aaaaaa"
                    text "[food] / [max_food_and_water]" size 16 bold True color "#32cd32" xalign 1.0
                
                # Ren'Py can draw health bars using pure code!
                bar:
                    value food 
                    range max_food_and_water
                    xsize 280 ysize 10
                    left_bar Solid("#32cd32") # Green fill
                    right_bar Solid("#333333") # Dark grey empty background

            # --- WATER METER ---
            vbox:
                spacing 4
                hbox:
                    xfill True
                    text "Water" size 18 bold True color "#aaaaaa"
                    text "[water] / [max_food_and_water]" size 16 bold True color "#00bfff" xalign 1.0
                
                bar:
                    value water 
                    range max_food_and_water
                    xsize 280 ysize 10
                    left_bar Solid("#00bfff") # Blue fill
                    right_bar Solid("#333333")

            # --- FREE TIME (Conditional) ---
            if free_time_remaining > 0:
                add Solid("#444444") xsize 280 ysize 1 # Subtle grey divider line
                hbox:
                    xfill True
                    text "Free Time Remaining:" size 18 bold True color "#aaaaaa"
                    text "[free_time_remaining] mins" size 18 bold True color "#ff8c00" xalign 1.0


screen hacking_terminal():
    zorder 110 # Draws on top of everything, including masks and HUDs
    modal True # Darkens the background and prevents clicking outside the box
    
    # Semi-transparent dark overlay to focus the player's attention
    add Solid("#000000cc")
    
    # Outer frame (Creates the 2-pixel Neon Green border)
    frame:
        xalign 0.5 
        yalign 0.5
        padding (2, 2)
        background Solid("#32cd32") # Neon Green
        
        # Inner frame (The dark terminal background)
        frame:
            xsize 450 
            padding (30, 30)
            background Solid("#050505") # Almost pitch black
            
            vbox:
                spacing 15
                
                # Terminal Header
                text "SYSTEM TERMINAL" size 24 bold True color "#32cd32" kerning 2 xalign 0.5
                add Solid("#32cd32") xsize 390 ysize 2 # Green divider line
                
                text "ENTER 3-DIGIT DECRYPTION KEY:" size 16 color "#aaaaaa" xalign 0.5
                
                # The actual Input Field
                input:
                    default ""
                    allow "0123456789"
                    length 3 # Max 3 digits
                    size 50
                    color "#ffffff"
                    bold True
                    prefix "> " # Adds the classic hacker arrow before their typing
                    xalign 0.5
                
                null height 5
                
                # Instructions
                text "PRESS ENTER TO SUBMIT" size 12 color "#555555" kerning 1 xalign 0.5


screen free_time_terminal():
    zorder 110 # Draws on top of everything
    modal True # Darkens the background and prevents clicking outside
    
    # Semi-transparent dark overlay
    add Solid("#000000cc")
    
    # Outer frame (Neon Green border)
    frame:
        xalign 0.5 
        yalign 0.5
        padding (2, 2)
        background Solid("#32cd32") 
        
        # Inner frame (Dark terminal background)
        frame:
            xsize 450 
            padding (30, 30)
            background Solid("#050505") 
            
            vbox:
                spacing 15
                
                # Terminal Header
                text "TME TO FREE TIME CONVERSION" size 22 bold True color "#32cd32" kerning 2 xalign 0.5
                add Solid("#32cd32") xsize 390 ysize 2 # Green divider line
                
                text "ENTER THE AMOUNT OF TME TO CONVERT:" size 16 color "#aaaaaa" xalign 0.5
                text "(1 TME = 1 MINUTE FREE TIME)" size 14 color "#ff8c00" xalign 0.5 # A nice orange warning text
                
                # The actual Input Field
                input:
                    default ""
                    allow "0123456789"
                    length 4 # Max 4 digits (in case they have a LOT of TME)
                    size 50
                    color "#ffffff"
                    bold True
                    prefix "> " 
                    xalign 0.5
                
                null height 5
                
                # Instructions
                text "PRESS ENTER TO SUBMIT" size 12 color "#555555" kerning 1 xalign 0.5