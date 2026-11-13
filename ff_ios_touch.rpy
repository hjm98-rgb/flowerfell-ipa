# iOS/触摸设备补丁：实体“继续”按钮 + 安全区适配
# 只在 Ren'Py 判定为触摸设备时出现，PC 端不受影响。

init python:
    def _ff_touch():
        return renpy.variant("touch") or renpy.variant("small") or renpy.variant("medium")

screen ff_tap_button():
    zorder 90
    if _ff_touch():
        button:
            xalign 0.96
            yalign 0.90
            xysize (150, 150)
            background None
            action Dismiss()
            text "▶" size 54 color "#ffffffcc" outlines [(1, "#00000080", 0, 0)] xalign 0.5 yalign 0.5

init 1 python:
    config.overlay_screens.append("ff_tap_button")
