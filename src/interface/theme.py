
from src.interface.services.utils import ComponentAlignment, Colors, FontStyles, Fonts, TextAlignment
from src.interface.services.style import Style

# Button properties
button_convert_style=Style()
button_convert_style.set_padding(pad_x=55)
button_convert_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_convert_style.set_border(2)
button_convert_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_convert_style.set_area(13, 1)
button_convert_style.set_component_alignmet(ComponentAlignment.LEFT)

# Button properties
button_export_style=Style()
button_export_style.set_padding(pad_x=55)
button_export_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_export_style.set_border(2)
button_export_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_export_style.set_area(13, 1)
button_export_style.set_component_alignmet(ComponentAlignment.RIGHT)

# Dropdown properties
dropdown_style=Style()
dropdown_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
dropdown_style.set_border(2)
dropdown_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
dropdown_style.set_area(13, 1)

# Input properties
input_style=Style()
input_style.set_font(Fonts.ARIAL, 12, FontStyles.ITALIC)
input_style.set_border(2)
input_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
input_style.set_area(width=50)

# Label properties
label_style=Style()
label_style.set_font(Fonts.ARIAL, 12, '')
label_style.set_border(2)
label_style.set_color(bg=Colors.SILVER, fg=Colors.BLACK)
label_style.set_area(width=50)


# Title properties
title_style=Style()
title_style.set_font(Fonts.ARIAL, 20, '')
title_style.set_border(2)
title_style.set_color(bg=Colors.SILVER, fg=Colors.BLACK)
title_style.set_area(width=10)
title_style.set_component_alignmet(ComponentAlignment.LEFT)

# Label properties
label_response_style=Style()
label_response_style.set_font(Fonts.ARIAL, 12, '')
label_response_style.set_border(2)
label_response_style.set_color(bg=Colors.SILVER, fg=Colors.BLACK)
label_response_style.set_area(width=48, height=7)
label_response_style.set_column_span(2)

# Space properties
space_style=Style()
space_style.set_padding(pad_x=0, pad_y=0)
space_style.set_font(Fonts.ARIAL, 1, '')
space_style.set_area(width=400, height=1)