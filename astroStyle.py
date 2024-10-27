import imgui
from ImUi import ButtonStyle, InputStyle, FloatSliderStyle

class AstroButtonStyle(ButtonStyle):
    def __init__(self):
        super().__init__()
        # Astro button colors
        self.normal_bg = (0.302, 0.675, 1.0, 1.0)      # #4dacff
        self.hovered_bg = (0.302, 0.675, 1.0, 0.8)     # #4dacff with 0.8 alpha
        self.active_bg = (0.302, 0.675, 1.0, 0.6)      # #4dacff with 0.6 alpha
        self.text = (1.0, 1.0, 1.0, 1.0)               # #ffffff
        self.border_color = (0.302, 0.675, 1.0, 1.0)   # #4dacff
        
        # Astro button styling
        self.frame_padding = (16.0, 8.0)  # 1rem = 16px, 0.5rem = 8px
        self.frame_rounding = 3.0         # 3px border radius
        self.border_size = 1.0            # 1px border width

class AstroInputStyle(InputStyle):
    def __init__(self):
        super().__init__()
        # Astro input colors
        self.normal_bg = (0.133, 0.133, 0.133, 1.0)    # #222222
        self.hovered_bg = (0.2, 0.2, 0.2, 1.0)         # #333333
        self.active_bg = (0.267, 0.267, 0.267, 1.0)    # #444444
        self.text = (0.867, 0.867, 0.867, 1.0)         # #dddddd
        self.border_color = (0.267, 0.267, 0.267, 1.0) # #444444

        # Astro input styling
        self.frame_padding = (8.0, 6.0)
        self.frame_rounding = 4.0
        self.border_size = 1.0

class AstroSliderStyle(FloatSliderStyle):
    def __init__(self):
        super().__init__()
        # Astro slider colors
        self.normal_bg = (0.133, 0.133, 0.133, 1.0)    # #222222
        self.hovered_bg = (0.2, 0.2, 0.2, 1.0)         # #333333
        self.active_bg = (0.267, 0.267, 0.267, 1.0)    # #444444
        self.grab_color = (0.533, 0.533, 0.533, 1.0)   # #888888
        self.grab_active = (0.667, 0.667, 0.667, 1.0)  # #aaaaaa
        self.text = (0.867, 0.867, 0.867, 1.0)         # #dddddd
        self.border_color = (0.267, 0.267, 0.267, 1.0) # #444444

        # Astro slider styling
        self.frame_padding = (8.0, 4.0)
        self.frame_rounding = 4.0
        self.border_size = 1.0
