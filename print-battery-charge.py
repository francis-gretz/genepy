def get_bars(charge):
    return round(charge / 10)


def battery_charge(charge):
    bars = get_bars(charge)

    st = ""

    for i in range(1, 11):
        if i <= bars:
            st = st + "❚"
        else:
            st = st + " "

    st = f"[{st}]"
    print(st)
    print(str(charge) + "%")


battery_charge(0)
# [          ]
# 0%
battery_charge(5)
# [          ]
# 5%
battery_charge(9)
# [❚         ]
# 9%
battery_charge(11)
# [❚         ]
# 11%
battery_charge(50)
# [❚❚❚❚❚      ]
# 50%
battery_charge(100)
# [❚❚❚❚❚❚❚❚❚❚]
# 100%
