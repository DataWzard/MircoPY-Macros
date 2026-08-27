# SPDX-FileCopyright Text: 2026 Jacob Stack 
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Figma macros with tool capabilty

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {# REQUIRED dict, must be named 'app'
    'name' : 'Figma', # Application name
    'macros' : [# List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x073079, 'Note', ['s']),# Sticky note
        (0x090049, 'Line', ['l']), # Line Tool
        (0x072019, 'Text', ['t']), # Text Tool
        # 2nd row ----------
        (0x024960, 'Bckwrd', [Keycode.CONTROL, '[']),# Send Backward 
        (0x071517, 'Export', [Keycode.CONTROL, Keycode.SHIFT, 'e']),# Export selection
        (0x007200, 'Forward', [Keycode.CONTROL, ']']), # Bring Forward
        # 3rd row ----------
        (0x000090, 'Zoom +', [Keycode.CONTROL, '+']), # Zoom In
        (0x000090, 'Group', [Keycode.CONTROL, 'g']), # Group selection
        (0x000090, 'Zoom -', [Keycode.CONTROL, '-']), # Zoom Out
        # 4th row ----------
        (0x002400, 'Select', ['v']), # Select Tool 
        (0x900090, '  Connector', ['x']),# Connector tool, spacing to adjust for screen readability
        (0x002400, 'Hand', ['h']), # Hand Tool
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
