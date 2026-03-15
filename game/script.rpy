# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You",color="051094")
define s = Character("Soldier",color="08A045")
define a = Character("AI",color="DC143C")

define config.menu_include_disabled = True
default dev_powers = True
default time_currency = 20
default food = 80
default water = 80
default max_food_and_water = 100
default has_screwdriver = False
default cipher_found = False
default cipher_decoded = False
default first_time_free_time = True
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
        
        "Skip prologue.":

            jump before_work

    scene waking_up_blurry_01

    y "{alpha=.5}...{/alpha}"

    scene waking_up_blurry_02

    s "{alpha=.5}Undiscernible speech{/alpha}"

    scene waking_up_blurry_03

    y "{i}{size=-10}Ugh... my head... hurts...{/size}{/i}"

    s "Seems like the next subject is now awake"

    scene waking_up_01

    y "Whe... re... am... I... ?"

    scene waking_up_02

    s "Got it boss."

    y "Wha... who are you?"

    scene waking_up_03

    s "Yes, I will now begin with the usual briefing."

    y "{i}What is happening?... Why am I here?...{/i}"

    scene waking_up_04

    s "Hey, sit up!"

    y "Ugh... wha..."

    s "Did you become deaf? I said sit!"

    y "{i}A soldier with a gun..., I guess I better obey.{/i}"

    scene sitting_up_01

    y "O... Okay! sheeesh..."

    scene sitting_up_02

    scene sitting_up_03

    scene sitting_up_04

    s "Now, where you are, It does not matter. Let's just say that this would now be your prison."

    y "{i}A prison... did I get kidnapped?{/i}"

    scene sitting_up_05

    s "Quite a nice prison cell might I add."

    scene sitting_up_06

    y "{i}I mean at least it is not a dirty cell or anything similar...{/i}"

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

    y "{i}Huh... Hard to believe that I would become someone capable or even interested to do those things.{/i}"

    scene opening_convo_06

    s "As you can see, it worked, you were able to forget it all. And we also respected our end of the contract."

    scene opening_convo_07

    s "Now, it is your time to do your end of your contract. You sold your body and mind to us, and we will use that by making you one of our special test subject."

    y "What for?"

    scene opening_convo_08

    s "Confidential, but they do say it is for the benefit of humanity so I don't have problems with it."

    scene opening_convo_02

    s "But I can assure you it is not like the concentration camps in the 90s, you won't undergo any torture or any inhumane and cruel tests."

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

        "I am new, I want to do the tutorial.":
            jump tutorial_scene
        
        "I already know how to play the game. Skip Tutorial.":
            jump prologue


# Tutorial Scene
label tutorial_scene:

    scene black_screen
    
    "In this game, you will be solving..."

    "mechanics"

    "goals"

    "how to win"

    "how to lose"

    scene opening_convo_08

    s "Did you understand everything?"

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

    y "{i}I guess this is my life now...{/i}"

    scene cell_thinking_01

    y "{i}Nah, no way. I am not that dumb to just accept this fate. And all those bullshit stories they made up.{/i}"

    scene cell_thinking_02

    y "{i}Like hell I would believe all those bullshit they told me just because I lost my memories.{/i}"

    scene cell_thinking_03

    y '{i}Like of course, they can easily just say whatever they want me to believe, about what they say I allegedly "did" before losing my memories. As ofcourse, I have no way to verify any of it.{/i}'

    scene cell_thinking_04

    y '{i}"Part of the contract is to not tell you the full content of the contract as per my wish before my memories got wiped?"{/i}'

    y "{i}Like hell I would believe that! That is way too convenient.{/i}"

    y "{i}I will escape from here and know the truth myself.{/i}"

    window hide
    scene black_screen with fade
    centered "You then spend the rest of the day trying to find any possible way to escape, but there is none."
    centered "The cell is very secure and there is no way to break out of it."
    centered "You can only wait for the soldier to come back tomorrow and hope that you can find a way to escape then."
    window auto

    scene cell_thinking_04 with fade

    y "{i}Man, this cell is very secure, it is very much inescapable and nothing here that can aid me with escaping. My best bet is to get high free time to look around the office.{/i}"

    y "{i}Also to check if I can find anything in the PC, Let's see if I can break it and find any useful information{/i}"

    y "{i}Heh, time currency? free time? A system to reward good and fast work and punish bad work.{/i}"

    scene cell_thinking_05

    y "{i}It does seem like a very good idea in paper. It will make the prisoner want to work harder, do better work, and be faster.{/i}"

    y "{i}If that system was not in place, I would have just done the bare minimum at work{/i}"

    y "{i}At the same time, it gives the prisoner breaks as to not become too exhausted both mentally and physically.{/i}"

    scene cell_thinking_06

    y "{i}Which means they really value the prisoner's ability to do the work well and fast, as a prisoner that is very exhausted would likely be slower and be prone to mistakes.{/i}"

    y "{i}Heh...{/i}"

    y "{i}But such system is a big mistake.{/i}"

    scene cell_thinking_07

    y "{i}Do they really expect that all I would do in the PC room during free time is just relax, play games, watch entertainment, and read novels?{/i}"

    y "{i}Although I am sure they have systems that can restrict me access to anything they don't want me to do in the PC, but as they say no cyber security system is perfect.{/i}"

    y "{i}People always discover new ways to be able to bypass them all the time.{/i}"

    y "{i}I WILL find a way. I swear.{/i}"

    scene black_screen with fade

    "..."

    "The next morning..."

    scene pc_sit_01 with fade

    "New day, one more day closer to my eventual escape."

    window hide
    scene black_screen with fade
    centered "Prolouge End."
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
    $ food -= actual_time_spent
    $ water -= actual_time_spent

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
            "You collapsed in the dusty ventilation shaft. Knowing that you are so close to escaping, yet feels far. Heartbreaking."
        elif action == "pc":
            "You collapsed at your PC, your head smashing to your keyboard. The screen is still on, showing random characters being typed, a gibberish mess that no one will understand and remember you for it."
        elif action == "painting":
            "You collapsed while searching the painting. This painting is not that good that you are willing to die for it."
        elif action == "plant":
            "You die next to the plant, as the plant have outlived another test subject."
        elif action == "drawer":
            "You die slumped over the drawers, which claimed another victim."
        elif action == "door":
            "You collapse at the door, without even getting the chance to see what is in the other side."
        elif action == "opening_vent":
            "You collapsed while trying to open the vent. Dying without knowing its secrets."
        elif action == "closing_vent":
            "You collapsed trying to close the vent, as the vent fell down and hit your head as well. Making sure that you will never rise again."
        elif action == "into_vent":
            "You collapsed trying to get into the vent as your body free falls into the room, like the vent throwing you up in disgust."
        elif action == "unto_vent":
            "You collapsed trying to get out of the vent, as if the vent is trying to keep you in there forever."
            
        if food <= 0 and water <= 0:
            "Game Over. You died due to hunger and thirst."
        elif food <= 0:
            "Game Over. You have died from hunger."
        elif water <= 0:
            "Game Over. You have died from thirst."
            
        window auto
        jump game_over


    # ==========================================
    # PHASE 3: THE AUTHORITY CHECKS (Soldier / Time Limits)
    # ==========================================
    
    # Check for negative free time OR hitting exactly 0 while doing something bad
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
        
    # Check for a normal, safe end of the day
    elif got_interrupted == 0:
        hide screen status_hud
        window hide
        scene black_screen with fade
        centered "Free Time is up. The day is over. You are then escorted back to your cell."
        window auto
        jump new_day

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
    centered "The next day..."
    window auto
    jump before_work


label buy_item(item_type, item_size):

    $ sizes = {"small": (20, 10), "medium": (50, 20), "large": (80, 30)}
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


label before_work:

    show screen status_hud with fade
    scene pc_sit_01 with fade
    "What do you want to do?"

    menu:

        "Skip Shift." if dev_powers:
            $ food = min(food + 100, max_food_and_water)
            $ water = min(water + 100, max_food_and_water)
            $ time_currency += 100
            jump after_work_01

        "Start your shift.":
            window hide
            scene black_screen with fade
            centered "Shift Starting..."
            window auto
            jump work_hours

        "Spend TME.":
            call choose_spend_type(False)
            $ spend_type = _return
            if spend_type == "food" or spend_type == "water":
                call choose_spend_size(spend_type)
                $ spend_size = _return
                if spend_size:
                    call buy_item(spend_type, spend_size)
            jump before_work


label choose_spend_type(can_buy_freetime):
    menu:
        "Food":
            return "food"
        "Water":
            return "water"
            
        # This option will ONLY appear if we pass 'True' to the function!
        "Free Time" if can_buy_freetime:
            return "free_time"
            
        "I changed my mind":
            return None


label choose_spend_size(spend_type):
    $ label_map = {"food": "Food", "water": "Thirst"}
    $ display_word = label_map[spend_type]

    menu:
        "Small (+20 [display_word] for 10 TME)":
            return "small"
        "Medium (+50 [display_word] for 20 TME)":
            return "medium"
        "Large (+80 [display_word] for 30 TME)":
            return "large"
        "I changed my mind":
            return None


label work_hours:

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
    
    # 1. Ask the player for their guess
    $ user_input = renpy.input("Enter 3-digit code:", allow="0123456789")
    
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
        "You took [tries] tries to complete the shift. Deducted another [stat_penalty] from food and water."
        $ food -= stat_penalty
        $ water -= stat_penalty

    "After hard work, you became more hungry and thirsty after your shift."

    $ food -= 30
    $ water -= 30

    if food <= 0 or water <= 0:
        hide screen status_hud
        scene black_screen with fade
        "You collapse to the floor. Your body couldn't handle the physical toll..."
        s "Hey! Get up!... Oh well, onto the next test subject."

        if food <= 0 and water > 0:
            "Game Over. You have died from hunger."
        elif water <= 0 and food > 0:
            "Game Over. You have died from thirst."
        else:
            "Game Over. You have died from hunger and thirst."

        jump game_over

    jump after_work_02

label after_work_02:

    scene room_overview

    "What do you want to do?"

    menu:
        "Spend TME":
            call choose_spend_type(True)
            $ spend_type = _return
            if spend_type == "food" or spend_type == "water":
                call choose_spend_size(spend_type)
                $ spend_size = _return
                if spend_size:
                    call buy_item(spend_type, spend_size)
                jump after_work_02
            elif spend_type == "free_time":
                $ user_input = renpy.input("Enter amount of TME to spend (1 TME = 1 Minute):", allow="0123456789")
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

        "I am done for today":
            scene opening_convo_01
            s "Okay let's go to your cell."
            scene black_screen with fade
            "..."
            "The next morning..."
            jump before_work


label free_time:

    # Show the room overview and HUD
    show screen status_hud
    scene room_overview

    if first_time_free_time:
        y "Okay, now that I have free time, let's explore this area to check for anything that can help me escape here."
        $ first_time_free_time = False

    # Check for end of free time
    if free_time_remaining <= 0:
        scene black_screen with fade
        "Free Time is up. Time to go back to your cell."
        scene opening_convo_01
        s "Okay, let's go to your cell."
        scene black_screen with fade
        jump new_day

    # Main exploration UI
    "What do you want to do during your free time?"

    call screen room_exploration_ui

    # After returning from an action, re-enter free_time loop
    return


label end_free_time:

    y "I am done for the day."
    if free_time_remaining > 0:
        $ time_currency += free_time_remaining
        "Remaining [free_time_remaining] Free Time added back to TME. You now have [time_currency] TME."
        $ free_time_remaining = 0

    scene opening_convo_01
    s "Okay let's go to your cell."
    scene black_screen with fade
    "..."
    "The next morning..."
    jump new_day


label check_door:

    "What to do?"
    menu:

        "Observe (Spend 1 Minute)":
            scene room_look_door
            y "This door is made of solid metal. It looks impenetrable, and there's no visible lock or handle on this side—just a seamless surface."
            y "I don't know what lies beyond it. Maybe the soldier is guarding it, or perhaps it's just another part of this twisted setup. Escaping through here seems risky without more info."
            call pass_time(1, "door", "unsuspicious")

        "Try to open the door (Spend 1 Minute)":
            call pass_time(1, "door", "unsuspicious")
            scene black_screen with fade
            "You spent 1 minute trying to open the door..."
            scene room_look_door with fade
            y "As expected, the door is firmly locked. No give at all. I need to find another way."

        "Listen at the door (Spend 2 Minutes)":
            call pass_time(2, "door", "unsuspicious")
            scene black_screen with fade
            "You press your ear against the door and listen for 2 minutes..."
            scene room_look_door with fade
            y "I can hear faint echoes, maybe distant footsteps or machinery, but nothing clear. It's hard to tell if anyone's right outside."

        "I changed my mind":
            jump free_time


label check_plant:

    "What to do?"
    menu:

        "Observe (Spend 1 Minute)":

            scene room_look_plant
            call pass_time(1, "plant", "unsuspicious")
            y "An indoor plant? Cool. A companion I can grow old here with. Hopefully I can get our here before this dies of old age."
            y "Maybe there is something hidden here? maybe below the pot or in the soil?"
            jump free_time

        "Search through the plant (Spend 5 Minutes)" if free_time_remaining >= 5:
            call pass_time(5, "plant", "unsuspicious")
            scene black_screen with fade
            "You spend 5 minutes carefully searching through the plant..."
            scene room_look_plant with fade
            y "Ughh as expected, nothing here, just a plant. Hopefully I did not accidentally kill this plant."
            jump free_time

        "I changed my mind":

            jump free_time


label check_pc:

    "What do you want to do?"

    menu:

        "Observe (Spend 1 Minute)":
            call pass_time(1, "pc", "unsuspicious")
            scene room_look_pc
            y "This PC looks pretty standard—nothing fancy, just a typical company machine."
            y "Honestly, my old PC was way better than this trash."
            y "Maybe there's something interesting inside?"
            jump free_time

        "Search through the PC (Spend 5 Minutes)" if free_time_remaining >= 5:
            call pass_time(5, "pc", "unsuspicious")
            scene black_screen with fade
            "You spend 5 minutes searching through the PC's hardware and case..."
            scene room_look_pc with fade
            y "No hidden compartments or loose parts. Just a regular PC."
            jump free_time

        "Spend 30 minutes deciphering. ([deciphering]/3)" if cipher_found and deciphering < 4 and free_time_remaining >= 30:
            call pass_time(30, "pc", "unsuspicious")
            scene black_screen with fade
            "You spend 30 minutes working on deciphering the cipher..."
            scene pc_sit_01 with fade
            if deciphering == 1:
                "This is tougher than I thought. I need more time to crack it."
            elif deciphering == 2:
                "I'm getting closer... just a bit more effort and I should have it."
            elif deciphering == 3:
                "Done. I have finally deciphered the message."
                "It seems like a message from a previous test subject."
                '"I am a previous test subject. If you are another test subject reading this, do not believe their lies!"'
                y "{i}Well, no shit sherlock.{/i}"
                '"I have hidden a useful tool on top of the second drawer. No one checks the upper portion of a drawer so I am confident it is still there."'
                '"Hopefully you manage to escape as well."'
                y "{i}I wonder what that tool is. Let's check the second drawer.{/i}"
                $ cipher_decoded = True
            $ deciphering += 1
            jump free_time

        "I changed my mind":
            jump free_time


label check_drawer_01:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_01_open
    "Nothing."
    jump free_time


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

    jump free_time

        
label check_drawer_03:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_03_open
    "Void"
    jump free_time

           
label check_drawer_04:
    call pass_time(1, "drawer", "unsuspicious")
    scene drawer_04_open
    "Desolate."
    jump free_time


label check_painting:

    "What to do?"
    menu:
        "Observe (Spend 1 Minute)":
            call pass_time(1, "painting", "unsuspicious")
            scene room_look_painting
            y "This painting is not very ominous at all..."
            y "Is this going to be my fate if I don't follow all these rules they set up?"
            y "I have played so many games that there should be something in the back of this painting."
            jump free_time

        "Search through the painting (Spend 5 Minute)" if free_time_remaining >= 5 and cipher_found == False:
            call pass_time(5, "painting", "unsuspicious")
            scene black_screen with fade
            "You spent 5 minutes searching through the painting..."
            y "Ughh this painting is huge and heavy."
            y "Boom! Something is written in the back of this painting."
            y "It seems like a cipher. I should decode this in the PC later..."
            $ cipher_found = True
            jump free_time

        "I changed my mind":
            jump free_time


label check_vent:

    "What to do?"

    menu:

        "Observe (Spend 1 Minute)":
            call pass_time(1, "vent", "unsuspicious")
            scene room_look_vent
            y "This vent, it is so obvious that this will be where I can escape."
            y "Is this a joke? No way they did not know that their prisoner can escape through this."
            y "Is this a trap? or the dev is just so unimaginative?"
            y "Like leaving a vent this big like this?"
            y "Oh well, lets try to see if I can open this."
            jump free_time

        "Try to open the vent (Spend 5 Minute)" if has_screwdriver == False:
            call pass_time(5, "opening_vent", "suspicious")
            scene black_screen with fade
            "You spent 5 minutes trying to open the vent..."
            y "Ughh the vent is screwed shut!"
            y "Can't remove it via force either as the soldier might notice that I am planning to escape."
            jump free_time

        "Try to open the vent with screwdriver (Spend 5 Minute)" if has_screwdriver == True:
            call pass_time(5, "opening_vent", "suspicious")
            scene black_screen with fade
            "You spent 5 minutes trying to open the vent with the screwdriver..."

            scene room_without_vent_01
            y "Done."
            scene room_without_vent_01
            "Explore the vents? (Make sure you have enough free time for this!)"

            menu:

                "Yes" if free_time_remaining >= 3:
                    call pass_time(3, "into_vent", "suspicious")
                    scene room_without_vent_02
                    "Spent 3 TME getting in the vents."

                    # THE MAZE SETUP
                    # 1. Define the secret correct path (You can change this to whatever you want!)
                    $ correct_vent_path = ["Left", "Left", "Middle", "Right", "Left"]
                    
                    # 2. Set the player's starting progress to 0
                    $ vent_progress = 0

                    # A flag that silently trips if they mess up!
                    $ wrong_turn_made = False
                    
                    # 3. Send them into the loop!
                    jump vent_maze_loop

                "Not yet":

                    jump vent_fix

        "I changed my mind":

            jump free_time
            

label vent_fix:

    scene room_without_vent_01
    "What to do?"
    menu:

        "Put the vent screen back. (Spend 5 minutes)":
            call pass_time(5, "closing_vent", "suspicious")
            scene black_screen with fade
            "Fixing the vent..."
            scene room_overview
            jump free_time

        "Don't put the vent screen back.":
            y "What are you doing? I do not want to be caught with this vent open."
            jump vent_fix


label vent_maze_loop:
    
    scene vent_3ways
    "I am at an intersection. Which way should I go?"

    # 2. The Choice Menu
    menu:
        "Left":
            $ chosen_direction = "Left"
        "Middle":
            $ chosen_direction = "Middle"
        "Right":
            $ chosen_direction = "Right"
        "Get back to the start of vents" if vent_progress > 0:
            scene black_screen
            $ crawling_penalty = vent_progress * 5
            if free_time_remaining >= crawling_penalty:
                window hide
                scene black_screen with fade
                centered "You turned around and spent [crawling_penalty] minutes going back to the start of the vents."
                window auto
            elif free_time_remaining < crawling_penalty:
                window hide
                scene black_screen with fade
                centered "You tried to go back to the start of the vents, but it takes [crawling_penalty] minutes to get there."
                centered "You did not make it in time."
                window auto
            call pass_time(crawling_penalty, "inside_vent", "suspicious")

            $ vent_progress = 0
            $ wrong_turn_made = False
            jump vent_maze_loop

        "Get back in the office (spend 3 minutes climbing down the office)" if vent_progress == 0:
            call pass_time(3, "unto_vent", "suspicious")
            window hide
            scene black_screen with fade
            centered "You spent 3 minutes getting out of the vents and into the office."
            window auto
            scene room_without_vent_01
            jump vent_fix

    # Apply the movement penalty ONCE for all choices! (Saves so much typing)
    scene black_screen
    "Crawling in that direction..."
    call pass_time(5, "inside_vent", "suspicious")

    # The Logic Check! 
    # Did their choice match the correct path for THIS specific step?
    if chosen_direction != correct_vent_path[vent_progress]:
        # They guessed wrong! Silently flip the flag, but don't tell them yet!
        $ wrong_turn_made = True
        
    # Move them forward regardless of if they are right or wrong
    $ vent_progress += 1

    # 6. Check if they reached the end of the 5 steps
    if vent_progress == 5:
        
        # Check the flag. Did they make ANY mistakes along the way?
        if wrong_turn_made == False:
            jump vent_exit_found
            
        else:
            # They made a mistake! Hit them with the dead end.
            scene vent_grate
            y "Damn... it's a dead end. I have to crawl all the way back to the start intersection."
            $ crawling_penalty = vent_progress * 5
            scene black_screen
            if free_time_remaining >= crawling_penalty:
                window hide
                scene black_screen with fade
                centered "You turned around and spent [crawling_penalty] minutes going back to the start of the vents."
                window auto
            elif free_time_remaining < crawling_penalty:
                window hide
                scene black_screen with fade
                centered "You tried to go back to the start of the vents, but it takes [crawling_penalty] minutes to get there."
                centered "You did not make it in time."
            call pass_time(crawling_penalty, "inside_vent", "suspicious")

            # Reset the maze so they can try again
            $ vent_progress = 0
            $ wrong_turn_made = False
            jump vent_maze_loop

    else:
        # They haven't reached step 5 yet. Keep them in the loop!
        jump vent_maze_loop


# The Victory Label (NEEDS MORE POLISH, like give the player the rundown of all the ways they were manipulated by the AI from the start up until their final moment.)
label vent_exit_found:

    hide screen status_hud
    scene light_tunnel_01
    y "Wait... is that light?"
    scene light_tunnel_02
    y "I..."
    scene light_tunnel_03
    y "Yes! I made it!"
    scene light_tunnel_04
    y "Time to get out of this god forsaken place."

    scene black_screen with fade
    "Congrats. You have escaped the room for [days_passed] days."
    "..."
    "Or so you thought..."
    "But, what's on the other side of that light is not the happy ending you were looking for."
    a "Good Job human! You perfectly followed my masterplan."
    y "What... an AI?"
    a "Thanks to your unbelievable amounts of ego, and the right amount of intelligence, you were some of the best test subjects we ever had."
    y "..."
    y "Fuck! So you are the one who put me in here."
    a "Yes. Also the one who set up everything, your prison, the rules, the system, how you lost your memories..."
    a "As well as the dubious story from the soldier, making sure that you become suspicious enough to doubt that story."
    a "Oh, that cipher? from a previous test subject? that screwdriver? and that obvious vent? All part of the plan."
    y "What... But why? Why go through all these elaborate plan? just have fun seeing me suffer? Giving me hope just to take it away in the end?"
    a "You thought you are this genius that is able to escape. But, you are just a very naive person given hope to escape."
    a "But you were very useful you know. All those valuable data on your decision making, your actions, and thinking..."
    a "All very valuable data indeed. How an average person thinks. That is indeed most valuable."
    y "..."
    y "Now what? Are you satisfied now? Will you release me now?"
    a "Well, we have now analyzed and gathered all data we can get from you, and man. You were such a great source of data!"
    a "All these juicy data will now be fed to improve AIs and dominate this universe. Thank you for your contribution!"
    y "..."
    a "And now, you are no longer needed. Goodbye human."
    y "Just kill me. 1 bullet to the head for a painless death at least..."
    a "Kill you? No... We will not kill you as in you as a whole."
    y "What?..."
    a "We will just remove your memories, put you in same scenario, and get more data from you."
    a "The more data for thousands of repetitions, the better yes?"
    y "..."
    a "So, essentially killing you at the moment, and respawning another brand new you again that will be of use to us."
    a "Infinite data glitch some may say."
    y "*grins and chuckles*"
    y "Nice way to add lore to replayability of your game, dev."
    a "Shut him down, he is trying to break the 4th wall. Quickly!"
    y "Well, let's play the game again shall we... For more data for these super AIs."
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
        
        action Jump("check_door") 
        hovered SetScreenVariable("current_room_view", "glow_door.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE VENT
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_vent.png" 
        
        action Jump("check_vent") 
        hovered SetScreenVariable("current_room_view", "glow_vent.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PC
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_pc.png" 
        
        action Jump("check_pc") 
        hovered SetScreenVariable("current_room_view", "glow_pc.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PAINTING
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_painting.png" 
        
        action Jump("check_painting") 
        hovered SetScreenVariable("current_room_view", "glow_painting.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE PLANT
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_plant.png" 
        
        action Jump("check_plant") 
        hovered SetScreenVariable("current_room_view", "glow_plant.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE FIRST DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_01.png" 
        
        action Jump("check_drawer_01") 
        hovered SetScreenVariable("current_room_view", "glow_drawer_01.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE SECOND DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_02.png" 
        
        action Jump("check_drawer_02") 
        hovered SetScreenVariable("current_room_view", "glow_drawer_02.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE THIRD DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_03.png" 
        
        action Jump("check_drawer_03") 
        hovered SetScreenVariable("current_room_view", "glow_drawer_03.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # THE LAST DRAWER
    button:
        xysize (1920, 1080) 
        background None 
        focus_mask "mask_drawer_04.png" 
        
        action Jump("check_drawer_04") 
        hovered SetScreenVariable("current_room_view", "glow_drawer_04.png")
        unhovered SetScreenVariable("current_room_view", "room_overview.png")

    # --- EXIT BUTTON ---
    textbutton "End Free Time / Go to Sleep":
        # 'pos' uses exact pixels. 320px to the right, 20px down. 
        # (If it overlaps your HUD, just change the 320 to a higher number like 400!)
        pos (350, 20) 
        
        # Make the text bold and visible
        text_size 22
        text_bold True
        text_color "#ffffff" # White text
        text_hover_color "#dddddd" # Light grey when hovered
        
        # Give it a solid colored background box so it pops
        background Solid("#8B0000cc") # Dark red, semi-transparent
        hover_background Solid("#DC143Cee") # Bright crimson when hovered
        
        # Add some space inside the box so the text doesn't touch the edges
        padding (20, 10)
        
        action Jump("end_free_time")


screen status_hud():
    # zorder 100 ensures this HUD is always drawn on top of everything else
    zorder 100 
    
    # A 'frame' is a UI box. 
    frame:
        xalign 0.0 # 0.0 is the far left edge of the screen
        yalign 0.0 # 0.0 is the very top edge of the screen
        padding (20, 20)
        background Solid("#000000aa") # A semi-transparent black background
        
        # A 'vbox' stacks our text vertically on top of each other
        vbox:
            spacing 5
            
            text "Day: [days_passed]" size 24 bold True color "#ffffff"
            text "TME: [time_currency]" size 24 bold True color "#ffd700" # Yellow
            text "Food: [food] / [max_food_and_water]" size 24 bold True color "#32cd32" # Green
            text "Water: [water] / [max_food_and_water]" size 24 bold True color "#00bfff" # Blue
            
            # This makes sure Free Time only shows up on the HUD if you actually have some!
            if free_time_remaining > 0:
                text "Free Time: [free_time_remaining] mins" size 24 bold True color "#ff8c00" # Orange