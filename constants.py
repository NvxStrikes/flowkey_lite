"""
Copyright (C) 2025-2026 NovaStrikes
https://superhivemarket.com/creators/novastrikes
https://novastrikes.com/
mailto:contact@novastrikes.com

Created by Hamayl

This file is part of Flowkey.
Flowkey is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see https://www.gnu.org/licenses/gpl-3.0.txt.
"""

SHORTCUTS = {
    "OBJECT": {
        "Selection": [
            {"key": "A", "description": "Select All", "modifier": None, "priority": "PRIMARY"},
            {"key": "Alt + A", "description": "Deselect All", "modifier": "ALT", "priority": "PRIMARY"},
            {"key": "Double Tap A", "description": "Deselect All", "modifier": None, "priority": "SECONDARY"},
            {"key": "B", "description": "Box Select", "modifier": None, "priority": "PRIMARY"},
            {"key": "C", "description": "Circle Select", "modifier": None, "priority": "PRIMARY"},
            {"key": "Ctrl + I", "description": "Invert Selection", "modifier": "CTRL", "priority": "SECONDARY"},
            {"key": "Shift + L", "description": "Select Linked", "modifier": "SHIFT", "priority": "SECONDARY"},
            {"key": "Shift + G", "description": "Select Grouped", "modifier": "SHIFT", "priority": "SECONDARY"},
        ],
        "Transform": [
            {"key": "G", "description": "Grab / Move", "modifier": None, "priority": "PRIMARY"},
            {"key": "R", "description": "Rotate", "modifier": None, "priority": "PRIMARY"},
            {"key": "S", "description": "Scale", "modifier": None, "priority": "PRIMARY"},
            {"key": "G + X/Y/Z", "description": "Constraint to Axis", "modifier": None, "priority": "PRIMARY"},
            {"key": "G + Shift + X/Y/Z", "description": "Constraint to Plane", "modifier": "SHIFT", "priority": "SECONDARY"},
            {"key": "Alt + G", "description": "Clear Location", "modifier": "ALT", "priority": "SECONDARY"},
            {"key": "Alt + R", "description": "Clear Rotation", "modifier": "ALT", "priority": "SECONDARY"},
            {"key": "Alt + S", "description": "Clear Scale", "modifier": "ALT", "priority": "SECONDARY"},
            {"key": "Ctrl + A", "description": "Apply Transform Menu", "modifier": "CTRL", "priority": "PRIMARY"},
            {"key": "Shift + Ctrl + Alt + C", "description": "Set Origin", "modifier": "CTRL+SHIFT+ALT", "priority": "ADVANCED"},
        ],
        "Object": [
            {"key": "Shift + D", "description": "Duplicate Object", "modifier": "SHIFT", "priority": "PRIMARY"},
            {"key": "Alt + D", "description": "Duplicate Linked", "modifier": "ALT", "priority": "PRIMARY"},
            {"key": "M", "description": "Move to Collection", "modifier": None, "priority": "PRIMARY"},
            {"key": "Ctrl + J", "description": "Join Objects", "modifier": "CTRL", "priority": "PRIMARY"},
            {"key": "Ctrl + P", "description": "Set Parent", "modifier": "CTRL", "priority": "PRIMARY"},
            {"key": "Alt + P", "description": "Clear Parent", "modifier": "ALT", "priority": "SECONDARY"},
            {"key": "H", "description": "Hide Selected", "modifier": None, "priority": "PRIMARY"},
            {"key": "Alt + H", "description": "Reveal Hidden", "modifier": "ALT", "priority": "PRIMARY"},
            {"key": "Shift + H", "description": "Hide Unselected", "modifier": "SHIFT", "priority": "SECONDARY"},
            {"key": "X or Delete", "description": "Delete Object", "modifier": None, "priority": "PRIMARY"},
            {"key": "Ctrl + Z", "description": "Undo", "modifier": "CTRL", "priority": "PRIMARY"},
            {"key": "Ctrl + Shift + Z", "description": "Redo", "modifier": "CTRL+SHIFT", "priority": "PRIMARY"},
            {"key": "F9", "description": "Adjust Last Operation", "modifier": None, "priority": "PRIMARY"},
            {"key": "Tab", "description": "Toggle Edit/Object Mode", "modifier": None, "priority": "PRIMARY"},
            {"key": "Ctrl + Tab", "description": "Mode Pie Menu", "modifier": "CTRL", "priority": "PRIMARY"},
        ],
        "View": [
            {"key": "Numpad 0", "description": "Active Camera View", "modifier": None, "priority": "SECONDARY"},
            {"key": "Numpad 1", "description": "Front View", "modifier": None, "priority": "SECONDARY"},
            {"key": "Numpad 3", "description": "Right View", "modifier": None, "priority": "SECONDARY"},
            {"key": "Numpad 7", "description": "Top View", "modifier": None, "priority": "SECONDARY"},
            {"key": "Ctrl + Numpad 1/3/7", "description": "Back/Left/Bottom View", "modifier": "CTRL", "priority": "SECONDARY"},
            {"key": "Numpad 5", "description": "Toggle Orthographic/Perspective", "modifier": None, "priority": "SECONDARY"},
            {"key": "Numpad Period", "description": "Frame Selected", "modifier": None, "priority": "PRIMARY"},
            {"key": "/", "description": "Local View Toggle", "modifier": None, "priority": "PRIMARY"},
            {"key": "Shift + Middle Mouse", "description": "Pan View", "modifier": "SHIFT", "priority": "PRIMARY"},
            {"key": "Middle Mouse", "description": "Orbit View", "modifier": None, "priority": "PRIMARY"},
            {"key": "Scroll Wheel", "description": "Zoom View", "modifier": None, "priority": "PRIMARY"},
            {"key": "Z", "description": "Shading Pie Menu", "modifier": None, "priority": "PRIMARY"},
            {"key": "N", "description": "Toggle Sidebar", "modifier": None, "priority": "PRIMARY"},
            {"key": "T", "description": "Toggle Toolbar", "modifier": None, "priority": "PRIMARY"},
        ],
        "General": [
            {"key": "F3", "description": "Search Menu", "modifier": None, "priority": "PRIMARY"},
            {"key": "Ctrl + Space", "description": "Maximize Area", "modifier": "CTRL", "priority": "SECONDARY"},
            {"key": "Ctrl + Alt + Space", "description": "Fullscreen Area", "modifier": "CTRL+ALT", "priority": "ADVANCED"},
            {"key": "Ctrl + O", "description": "Open File", "modifier": "CTRL", "priority": "SECONDARY"},
            {"key": "Ctrl + S", "description": "Save File", "modifier": "CTRL", "priority": "SECONDARY"},
        ],
    },
}
