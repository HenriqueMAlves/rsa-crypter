
from src.interface.services.utils import Colors, FontStyles, Fonts
from src.interface.services.style import Style

# Button properties
button_style=Style()
button_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_style.set_border(2)
button_style.set_color(bg=Colors.CORAL, fg=Colors.GOLD)
button_style.set_area(8, 1)


