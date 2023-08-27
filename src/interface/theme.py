
from src.interface.services.utils import Colors, FontStyles, Fonts
from src.interface.services.style import Style

# Button properties
button_style=Style()
button_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_style.set_border(2)
button_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_style.set_area(8, 1)

# Input properties
input_style=Style()
input_style.set_font(Fonts.ARIAL, 12, FontStyles.ITALIC)
input_style.set_border(2)
input_style.set_color(bg=Colors.BLUE_LIGHT, fg=Colors.BLACK)
input_style.set_area(width=20)

# Label properties
label_style=Style()
label_style.set_font(Fonts.ARIAL, 12, FontStyles.UNDERLINE)
label_style.set_border(2)
label_style.set_color(bg=Colors.MAROON_LIGHT, fg=Colors.MAROON)
label_style.set_area(width=20)

# Space properties
space_style=Style()
space_style.set_padding(pad_x=0, pad_y=0)
space_style.set_font(Fonts.ARIAL, 1, '')
space_style.set_area(width=200, height=1)