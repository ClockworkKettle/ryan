#sys.path.append(".")
from template import loc

print(f"""
    You wake, jolted awake by a sudden shake, heart beating
    furiously in your chest.
    The image of a large rat chasing you down East Granville
    Street fades into nothing more than an unpleasant
    itch.


    The first thing you notice is the air. Stale in a way
    that only the recycled air of an airplane can be.
    The groaning and stretching of cramped passengers
    after a long flight drifts gently to your ears.

    You crack your eyes open, and quickly wince, the bright
    light streaming unhindered in the window on your left
    burning your retinas. To your right, down the aisle
    you notice the flight attendant verbally pressing
    passengers back into their seats. The seat belt light
    is still on.

    What do you do?
    """)


location = loc()
location.look_around()
