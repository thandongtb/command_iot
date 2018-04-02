COMMANDS = [
    "bật",
    'mở',
    'sáng',
    'chạy',
    'dừng',
    'đóng',
    'ngắt',
    'tắt',
]

CMDS_MAPPING = dict.fromkeys(COMMANDS[:4], 1)
CMDS_MAPPING.update(dict.fromkeys(COMMANDS[4:], 0))

OBJECTS = [
    'điện',
    'đèn',
    'đèn chiếu sáng',
    'đèn ngủ',
    'đèn sưởi',
    'đèn học',
    'đèn nháy',
    'đèn chùm',
    'đèn thờ',
    'quạt',
    'quạt trần',
    'quạt cây',
    'quạt máy',
    'quạt điện',
    'điều hòa',
    'tivi',
    'tủ lạnh',
    'lò vi sóng',
    'dàn âm thanh',
    'máy giặt',
    'máy rửa bát',
    'máy lạnh',
    'lò nướng',
    'bếp điện',
    'bếp từ',
    'rèm cửa',
    'máy vi tính',
]

LOCATIONS = [
    'bếp',
    'nhà bếp',
    'nhà tắm',
    'phòng tắm',
    'phòng bếp',
    'phòng khách',
    'phòng ngủ',
    'phòng học',
    'phòng ăn',
    'phòng thờ',
    'phòng vệ sinh',
    'phòng giải trí',
    'phòng làm việc',
    'nhà vệ sinh',
    'sân',
    'hành lang',
    'cầu thang',
    'sân thượng',
    'sân phơi',
    'khu giải trí',
    'cửa ra vào',
    'cửa sổ',
]

PINMODE_MAPPING = dict.fromkeys(LOCATIONS, 0)

PINMODE_MAPPING.update({
    LOCATIONS[4] : 5,
    LOCATIONS[5] : 4,
    LOCATIONS[6] : 14,
    LOCATIONS[7] : 12,
})

print("" + str(PINMODE_MAPPING['phòng khách']))