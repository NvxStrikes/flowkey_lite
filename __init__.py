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

bl_info = {
    "name": "FlowKeys Lite",
    "author": "NovaStrikes",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > FlowKeys",
    "description": "Clean, lightweight Object Mode shortcut reference panel",
    "category": "Interface",
}

from . import constants
from . import panels

def register():
    try:
        panels.register()
    except Exception as e:
        print(f"[FlowKeys Lite] Failed to register: {e}")

def unregister():
    try:
        panels.unregister()
    except Exception as e:
        print(f"[FlowKeys Lite] Failed to unregister: {e}")

__all__ = [
    "constants",
    "panels",
]
