import os
import sys
import time
import random
import threading
import queue

# Preserve original print and input functions
ns_print, ns_input = print, input
skip_flag = False

# OS-Specific Input Handling
if os.name == 'nt':
    import msvcrt

    # Detect any keypress on Windows in a background thread
    def listen_for_input(input_queue):
        global skip_flag
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try: key = key.decode()
            except: key = str(key)
            input_queue.put(key); skip_flag = True

    # Check once for any keypress on Windows
    def check_for_input(input_queue):
        global skip_flag
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try: key = key.decode()
            except: key = str(key)
            input_queue.put(key); skip_flag = True

    # Discard any pending keypresses on Windows
    def flush_input():
        while msvcrt.kbhit():
            msvcrt.getch()

else:
    import termios, tty, select

    # Detect any keypress on Unix in a background thread
    def listen_for_input(input_queue):
        global skip_flag
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)
                input_queue.put(key); skip_flag = True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    # Check once for any keypress on Unix
    def check_for_input(input_queue):
        global skip_flag
        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            input_queue.put(key); skip_flag = True

    # Discard any pending keypresses on Unix
    def flush_input():
        termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)


# Print text slowly and allow skipping with any key
def slow_print(text, delay=0.05):
    global skip_flag
    flush_input()           # Discard any keystrokes pressed before printing
    skip_flag = False
    ns_print()
    q = queue.Queue()
    threading.Thread(target=listen_for_input, args=(q,), daemon=True).start()
    for i, ch in enumerate(text):
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(delay)
        check_for_input(q)
        if skip_flag:
            sys.stdout.write(text[i+1:]); break
    flush_input()
    ns_print()


# Prompt for input slowly and allow skipping with any key
def slow_input(prompt, delay=0.05):
    global skip_flag
    flush_input()           # Discard any keystrokes pressed before prompting
    skip_flag = False
    ns_print()
    q = queue.Queue()
    threading.Thread(target=listen_for_input, args=(q,), daemon=True).start()
    for i, ch in enumerate(prompt):
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(delay)
        check_for_input(q)
        if skip_flag:
            sys.stdout.write(prompt[i+1:]); break
    flush_input()
    ns_print()
    return ns_input("> ")


# Override built-in print and input
print, input = slow_print, slow_input

# This is where the fun begins...

# Title menu
ns_print("""
                                                                                                                                                                                  
       █████         ██████████████  ██████████████  ██████████████      ████████████    █████████████    ███        ███    ████████████    ██████████████   ████        █████       
      ███████       ████                  ████       ████       █████  ████        ████  ███        ████  ███        ███  ████        ████  ████       ████  ████       ███████      
    ████   ████      █████████████        ████       ████       ████   ███          ███  ███        ████  ██████████████  ███          ███  ██████████████   ████     ████   ████    
   █████████████               ████       ████       █████████████     ████        ████  ███ █████████    ███        ███  ████        ████  ████        ███  ████    █████████████   
 ████         ████  ██████████████        ████       ████       █████    ████████████    ███              ███        ███    ████████████    ██████████████   ████  ████         ████ 
                                                                                                                                                                              
""")
print("Welcome to Astrophobia.")

# Game selection
while True:
    title_action = input(
        "Would you like to start a new game (new), continue a previous game (continue), or quit (quit)?"
    ).strip().lower()
    if title_action == "new":
        print("Forming a new galaxy..."); time.sleep(3); break
    elif title_action == "continue":
        print("Launching back into dead space..."); time.sleep(3); break
    elif title_action == "quit":
        print("Quitting..."); sys.exit()
    else:
        print("Please choose a valid option. (new) (continue) (quit)")

# New game
if title_action == "new":
    # Space monologue
    print("\"Certain collision, capable of causing global climatic catastrophe that may threaten the future of civilization as we know it.\"")
    time.sleep(1)
    # Introduction to timeline deviation
    print("In the early years of the 21st century, mankind learned that even something as pure as the heavens could harbor certain doom. In December of 2004, Asteroid 99942 Apophis was discovered – an aimlessly wandering leviathan of stone, destined to cross our path. With each new calculation, the outcome grew more dire – an impact which once seemed improbable began to take the shape of inevitability. World-renowned strategists and brilliant mathematicians did nothing but watch in grim silence as the numbers converged into a single, and inevitable outcome: global climatic catastrophe.")
    time.sleep(3)
    # Introduction to The Technological Rush
    print("For nearly 25 relentless years, the brightest minds on the planet raced against time, producing life-changing technological advancements at an unprecedented pace. As the threat of global annihilation grew, hope became as scarce as a clear sky in the fallout of despair. The forecast of devastation was clear – the collision would not only shatter the world we once knew, but guide us to abandon our crumbling cradle of a planet. When all options to save Earth had been exhausted, humanity's salvation became a desperate diaspora into the stars.")
    time.sleep(3)
    # Introduction to The Initiative
    print("Engineers worked around the clock. Not in a futile bid to save a doomed planet, but to forge humanity’s final exit ticket. The brightest minds all over the world intertwined, culminating into a radical plan. By 2029, a select five-hundred souls – the minimum viable population – were to be launched into the cosmos, carrying with them the last ember of our civilization, destined to seed the stars with the future of mankind.")
    time.sleep(3)
    # Introduction to The Greatest Exodus
    print("Thus,"); time.sleep(1)
    print("in the shadow of the impending apocalypse,"); time.sleep(1)
    print("the greatest exodus in human history was born."); time.sleep(3)

# Planet definitions: type, Earth Similarity Index (ESI), distance from Earth in parsecs, and possible home planet
planets = {
    "KOI-4878b":          {"type": "Exoplanet",         "esi": 0.98, "distance_pc": "329",   "starter": True},
    "TRAPPIST-1e":        {"type": "Exoplanet",         "esi": 0.95, "distance_pc": "12.5",  "starter": True},
    "Proxima Centauri B": {"type": "Exoplanet",         "esi": 0.87, "distance_pc": "1.3",   "starter": True},
    "Gliese 667 Cc":      {"type": "Exoplanet",         "esi": 0.84, "distance_pc": "7.2",   "starter": True},
    "Gliese 180 c":       {"type": "Exoplanet",         "esi": 0.84, "distance_pc": "11.95", "starter": True},
    "Kepler-452b":        {"type": "Exoplanet",         "esi": 0.83, "distance_pc": "550",   "starter": True},
    "HD 40307 g":         {"type": "Exoplanet",         "esi": 0.81, "distance_pc": "12.3",  "starter": True},
    "TOI-715.02":         {"type": "Exoplanet",         "esi": 0.81, "distance_pc": "42.3",  "starter": True},
    "Mars":               {"type": "Planet",            "esi": 0.70, "distance_pc": "1.2e-5","starter": True},
    "Tau Ceti f":         {"type": "Exoplanet",         "esi": 0.68, "distance_pc": "3.65",  "starter": True},
    "Mercury":            {"type": "Planet",            "esi": 0.60, "distance_pc": "6e-6",  "starter": True},
    "Lacaille 9352 d":    {"type": "Exoplanet",         "esi": 0.53, "distance_pc": "3.27",  "starter": True},
    "LTT 1445 Ad":        {"type": "Exoplanet",         "esi": 0.49, "distance_pc": "6.87",  "starter": True},
    "Venus":              {"type": "Planet",            "esi": 0.44, "distance_pc": "6e-6",  "starter": True},
    "The Moon":           {"type": "Natural satellite", "esi": 0.38, "distance_pc": "1e-6",  "starter": True},
    "Uranus":             {"type": "Ice giant",         "esi": 0.26, "distance_pc": "2.7e-4","starter": True},
    "Saturn":             {"type": "Gas giant",         "esi": 0.23, "distance_pc": "1.3e-4","starter": True},
    "Neptune":            {"type": "Ice giant",         "esi": 0.18, "distance_pc": "4.3e-4","starter": True},
    "Jupiter":            {"type": "Gas giant",         "esi": 0.17, "distance_pc": "6.3e-5","starter": True},
    "Pluto":              {"type": "Dwarf planet",      "esi": 0.09, "distance_pc": "5.3e-4","starter": True},
}

# Grab only starter planets from the full data
starter_planets = [name for name, data in planets.items() if data.get("starter")]

# Select home planet
home_planet = random.choice(starter_planets)

# Select era
era = random.randint(2165, 3165)

# Store home planet info
planet_info = planets[home_planet]

# Build and print the game setting
home_planet_type = planet_info["type"] + " " if planet_info["type"] else ""
print(home_planet_type + home_planet + ", year " + str(era) + " CE")

"""
# Warning if ESI too low
if planet_info["esi"] > 0.5:
    print("Notice: " + home_planet + " (Earth Similarity Index " + str(round(planet_info["esi"], 2)) + ") is classified as hospitable.")
else:
    print("WARNING: " + home_planet + " (Earth Similarity Index " + str(round(planet_info["esi"], 2)) + ") is classified as inhospitable. Outside of human habitats, certain death may be assumed.")
"""

# Placeholder for continuation logic
if title_action == "continue":
    print("Soooooooooooo... this doesn't actually exist yet. *boowomp-womp-womp-wowowowowomp*")
