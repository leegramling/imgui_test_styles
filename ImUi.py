# ImUi.py
# create a wrapper for imgui widgets
import imgui


class BaseStyle:
    def __init__(self):
        # Common colors
        self.text = (1.0, 1.0, 1.0, 1.0)        # Text color
        self.border_color = (0.5, 0.5, 0.5, 1.0) # Border color
        
        # Common padding and borders
        self.frame_padding = (4.0, 4.0)          # Inner padding
        self.frame_rounding = 3.0                # Corner rounding
        self.border_size = 1.0                   # Border width
        
        # Common sizing
        self.min_size = (0.0, 0.0)              # Minimum size

    def push_common_styles(self):
        """Push styles common to all widgets"""
        imgui.push_style_color(imgui.COLOR_TEXT, *self.text)
        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (self.frame_padding[0], self.frame_padding[1]))
        imgui.push_style_var(imgui.STYLE_FRAME_ROUNDING, self.frame_rounding)
        imgui.push_style_color(imgui.COLOR_BORDER, *self.border_color)

    def pop_common_styles(self):
        """Pop common styles"""
        imgui.pop_style_color(2)  # Pop text and border colors
        imgui.pop_style_var(2)    # Pop padding, rounding, border size

class InputStyle(BaseStyle):
    def __init__(self):
        super().__init__()
        # Input colors for different states
        self.normal_bg = (0.15, 0.15, 0.15, 1.0)    # Normal background
        self.hovered_bg = (0.19, 0.19, 0.19, 1.0)   # Hovered background
        self.active_bg = (0.25, 0.25, 0.25, 1.0)    # Active/focused background
        
    def push(self):
        """Apply all input styles"""
        self.push_common_styles()
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, self.normal_bg[0], self.normal_bg[1], self.normal_bg[2], self.normal_bg[3])
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_HOVERED, self.hovered_bg[0], self.hovered_bg[1], self.hovered_bg[2], self.hovered_bg[3])
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_ACTIVE, self.active_bg[0], self.active_bg[1], self.active_bg[2], self.active_bg[3])
        
    def pop(self):
        """Remove all pushed styles"""
        imgui.pop_style_color(3)  # Pop background colors
        self.pop_common_styles()

class FloatSliderStyle(BaseStyle):
    def __init__(self):
        super().__init__()
        # Slider colors for different states
        self.normal_bg = (0.15, 0.15, 0.15, 1.0)    # Background color
        self.hovered_bg = (0.19, 0.19, 0.19, 1.0)   # Hovered background
        self.active_bg = (0.25, 0.25, 0.25, 1.0)    # Active background
        self.grab_color = (0.6, 0.6, 0.6, 1.0)      # Slider grab color
        self.grab_active = (0.7, 0.7, 0.7, 1.0)     # Slider grab when active
        
    def push(self):
        """Apply all slider styles"""
        self.push_common_styles()
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, self.normal_bg[0], self.normal_bg[1], self.normal_bg[2], self.normal_bg[3])
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_HOVERED, self.hovered_bg[0], self.hovered_bg[1], self.hovered_bg[2], self.hovered_bg[3])
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND_ACTIVE, self.active_bg[0], self.active_bg[1], self.active_bg[2], self.active_bg[3])
        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, self.grab_color[0], self.grab_color[1], self.grab_color[2], self.grab_color[3])
        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB_ACTIVE, self.grab_active[0], self.grab_active[1], self.grab_active[2], self.grab_active[3])
        
    def pop(self):
        """Remove all pushed styles"""
        imgui.pop_style_color(5)  # Pop slider-specific colors
        self.pop_common_styles()


class ButtonStyle(BaseStyle):
    def __init__(self):
        super().__init__()
        # Button colors for different states
        self.normal_bg = (0.2, 0.2, 0.2, 1.0)    # Normal background color
        self.hovered_bg = (0.3, 0.3, 0.3, 1.0)   # Hovered background color 
        self.active_bg = (0.4, 0.4, 0.4, 1.0)    # Active/pressed background color
        
    def push(self):
        """Apply all button styles"""
        self.push_common_styles()
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.normal_bg)
        imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, *self.hovered_bg)
        imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, *self.active_bg)
        
    def pop(self):
        """Remove all pushed styles"""
        imgui.pop_style_color(3)  # Pop button-specific colors (normal, hovered, active)
        self.pop_common_styles()


def button(label: str, style: ButtonStyle = None) -> bool:
    """Wrapper for imgui button with optional style"""
    if style:
        style.push()
    clicked = imgui.button(label)
    if style:
        style.pop()
    return clicked

def input_text(label: str, value: str, buffer_length: int = 256, style: InputStyle = None) -> tuple[bool, str]:
    """Wrapper for imgui input_text with optional style"""
    if style:
        style.push()
    changed, new_value = imgui.input_text(label, value, buffer_length)
    if style:
        style.pop()
    return changed, new_value

def slider_float(label: str, value: float, min_value: float, max_value: float, style: FloatSliderStyle = None) -> tuple[bool, float]:
    """Wrapper for imgui slider_float with optional style"""
    if style:
        style.push() 
    changed, new_value = imgui.slider_float(label, value, min_value, max_value)
    if style:
        style.pop()
    return changed, new_value
