from pathlib import Path
from typing import Final



main_win_size: Final = (980, 670)
panel_size: Final = (main_win_size[0] - 20, main_win_size[1] - 30)
project_path: Final = Path(__file__).resolve().parent


main_menu = {
    'Арифметика': 'on_click_menu_for_arithmetic',
    'Квадратные уровнения': 'on_click_menu_for_equation',
    'выход': None
}
