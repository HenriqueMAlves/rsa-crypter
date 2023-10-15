
from src.interface.services.utils import ComponentAlignment, Colors, FontStyles, Fonts, TextAlignment
from src.interface.services.style import Style

########################
# Título
title_style=Style()
title_style.set_font(Fonts.ARIAL, 20, '')
title_style.set_border(2)
title_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
title_style.set_area(width=10)
title_style.set_component_alignmet(ComponentAlignment.LEFT)

########################
# String de entrada
label_style=Style()
label_style.set_font(Fonts.ARIAL, 12, '')
label_style.set_border(2)
label_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
label_style.set_area(width=50)

input_style=Style()
input_style.set_font(Fonts.ARIAL, 12, FontStyles.ITALIC)
input_style.set_border(2)
input_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
input_style.set_area(width=50)

########################
# Chaves de criptografia
key_input_style=Style()
key_input_style.set_font(Fonts.ARIAL, 12, FontStyles.ITALIC)
key_input_style.set_border(2)
key_input_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
key_input_style.set_component_alignmet(ComponentAlignment.LEFT)
key_input_style.set_padding(70)
key_input_style.set_area(width=15)

key_2_label_style=Style()
key_2_label_style.set_font(Fonts.ARIAL, 12, '')
key_2_label_style.set_border(2)
key_2_label_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
key_2_label_style.set_component_alignmet(ComponentAlignment.RIGHT)
key_2_label_style.set_padding(70)
key_2_label_style.set_area(width=15)

key_2_input_style=Style()
key_2_input_style.set_font(Fonts.ARIAL, 12, FontStyles.ITALIC)
key_2_input_style.set_border(2)
key_2_input_style.set_color(bg=Colors.SILVER_LIGHT, fg=Colors.BLACK)
key_2_input_style.set_component_alignmet(ComponentAlignment.RIGHT)
key_2_input_style.set_padding(10)
key_2_input_style.set_area(width=15)

########################
# Opções
button_convert_style=Style()
button_convert_style.set_padding(pad_x=55)
button_convert_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_convert_style.set_border(2)
button_convert_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_convert_style.set_area(13, 1)
button_convert_style.set_component_alignmet(ComponentAlignment.LEFT)

dropdown_style=Style()
dropdown_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
dropdown_style.set_border(2)
dropdown_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
dropdown_style.set_area(13, 1)

button_export_style=Style()
button_export_style.set_padding(pad_x=55)
button_export_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_export_style.set_border(2)
button_export_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_export_style.set_area(13, 1)
button_export_style.set_component_alignmet(ComponentAlignment.RIGHT)

########################
# Resultado
text_response_style=Style()
text_response_style.set_font(Fonts.ARIAL, 12, '')
text_response_style.set_border(2)
text_response_style.set_color(bg=Colors.SILVER, fg=Colors.BLACK)
text_response_style.set_text_alignment(TextAlignment.TOP + TextAlignment.LEFT)
text_response_style.set_area(width=48, height=7)
text_response_style.set_column_span(2)

button_copy_style=Style()
button_copy_style.set_padding(pad_x=10, pad_y=10)
button_copy_style.set_font(Fonts.ARIAL, 10, FontStyles.BOLD)
button_copy_style.set_border(2)
button_copy_style.set_color(bg=Colors.GRAY, fg=Colors.BLACK)
button_copy_style.set_area(8, 1)
button_copy_style.set_component_alignmet(ComponentAlignment.CENTER + ComponentAlignment.RIGHT)
button_copy_style.set_text_alignment(TextAlignment.CENTER)

# Space properties
space_style=Style()
space_style.set_padding(pad_x=0, pad_y=0)
space_style.set_font(Fonts.ARIAL, 1, '')
space_style.set_area(width=400, height=1)