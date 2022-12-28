import datetime
import reftab.term as t

symbols = {
    "win": {
        "shift": ("Shift", "\u21e7"),
        "control": ("Ctrl", "\u2303"),
        "alternate": ("Alt", "\u2387"),
        "escape": ("Esc", "\u241b"),
        "backspace": ("Backspace", "\u232b"),
        "delete": ("Delete", "\u2326"),
        "enter": ("Enter", "\u21b5"),
        "tab": ("Tab", "\u21b9"),
        "pageup": ("PageUp", "PgUp"),
        "pagedown": ("PageDown", "PgDn"),
        "left": ("Left", "\u2190"),
        "right": ("Right", "\u2192"),
        "up": ("Up", "\u2191"),
        "down": ("Down", "\u2193"),
    },
    # "mac": {
    #     "shift": ("Shift", "\u21e7"),
    #     "control": ("Command", "\u2318"),
    #     "alternate": ("Option", "\u2325"),
    #     "escape": ("Esc", "\u238b"),
    #     "backspace": ("Delete", "\u232b"),
    #     "tab": ("Tab", "\u21e5"),

    # }
}


class vscode_shortcuts:
    name = "VS Code Shortcuts"
    ref_added = datetime.date(2022, 12, 26)
    ref_updated = datetime.date(2022, 12, 26)
    authority = "Microsoft"
    aliases = [
        "vsc",
        "vs code",
        "code",
        "vscode"
    ]
    data = {
        "Add Cursor Above": ""
    }

    def __str__(self):
        title = f"{self.name} (Windows)"
