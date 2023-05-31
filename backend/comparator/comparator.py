import re

from comparator.settings import colors, characteristics, engNotNeedWord


def compare(current_product_names, new_product_names):
    data_base = {}
    iterator = 0
    result = [""] * len(new_product_names)
    for product_name in current_product_names + new_product_names:
        name = product_name.lower()
        new_temp_stuff = re.sub("\[.*?\]", "", name)
        new_temp_stuff = new_temp_stuff.split()
        another_temp_stuff = ["", "", "", ""]
        for tempName in new_temp_stuff:
            subname = ''.join(
                ch for ch in tempName if ch.isalnum())
            break_flag = False
            for color in colors.values():
                if subname in color:
                    another_temp_stuff[2] = color[0]
                    break_flag = True
                    break
            if break_flag:
                continue
            for characteristic in characteristics.values():
                if subname == characteristic:
                    another_temp_stuff[3] = subname
                    break_flag = True
                    break
            if break_flag:
                continue
            if any(map(str.isdigit, subname)):
                another_temp_stuff[1] += subname
                break_flag = True
            if break_flag:
                continue
            if re.search(r'[a-z0-9]', subname):
                if subname in engNotNeedWord:
                    continue
                another_temp_stuff[0] += subname
        final_name = ''.join(another_temp_stuff)
        if iterator < len(current_product_names) or not(final_name in data_base):
            data_base[final_name] = iterator
        else:
            if data_base[final_name] >= len(current_product_names):
                result[iterator - len(current_product_names)] = new_product_names[data_base[final_name] - len(current_product_names)]
            else:
                result[iterator - len(current_product_names)] = current_product_names[data_base[final_name]]
        iterator += 1
    return result


# print(compare([], [
# "Мышь беспроводная SteelSeries Aerox 3 Wireless черный [18000 dpi, светодиодный, Bluetooth, USB Type-A, кнопки - 6]",
# "Мышь проводная SteelSeries Aerox 3 Onyx 2022 [62611] черный [8500 dpi, светодиодный, USB Type-A, кнопки - 6]",
# "Мышь проводная Steelseries Sensei Ten черный",
# "Мышь проводная SteelSeries Sensei 310 черный [12000 dpi, светодиодный, USB Type-A, кнопки - 8]",
# "Мышь проводная SteelSeries Rival 3 черный [8500 dpi, светодиодный, USB Type-A, кнопки - 6]",
#
# "Мышь проводная SteelSeries Aerox 3 Onyx 2022 [62603] белый [8500 dpi, светодиодный, USB Type-A, кнопки - 6]",
# "Мышь проводная SteelSeries Rival 5 [62551] черный [18000 dpi, светодиодный, USB Type-A, кнопки - 9]",
# "Мышь беспроводная SteelSeries Prime Wireless черный [18000 dpi, лазерный, радиоканал, кнопки - 6]",
#
# "Мышь проводная SteelSeries Prime черный [18000 dpi, лазерный, USB Type-A, кнопки - 6]",
# "Игровая мышь SteelSeries Prime, черный"
# ]))
