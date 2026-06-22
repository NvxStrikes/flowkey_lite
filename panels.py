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

import bpy
from . import constants

class FLOWKEYS_PT_lite_main(bpy.types.Panel):
    bl_label = "FlowKeys Lite"
    bl_idname = "FLOWKEYS_PT_lite_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "FlowKeys"

    def draw(self, context):
        layout = self.layout
        
        # Header display
        header_box = layout.box()
        header_row = header_box.row(align=True)
        header_row.label(text="Object Mode Reference", icon='OBJECT_DATA')
        
        shortcuts_data = constants.SHORTCUTS.get("OBJECT", {})
        
        for category, shortcuts in shortcuts_data.items():
            # Category container box
            cat_box = layout.box()
            cat_box.label(text=category, icon='BORDERMOVE')
            
            for shortcut in shortcuts:
                key_str = shortcut.get("key", "")
                desc_str = shortcut.get("description", "")
                
                row_split = cat_box.row(align=True)
                
                # Split for key badge vs description
                split = row_split.split(factor=0.35, align=True)
                
                # Key badge
                key_box = split.box()
                key_box.label(text=key_str)
                
                # Description
                split.label(text=desc_str)

CLASSES = [
    FLOWKEYS_PT_lite_main,
]

def register():
    for cls in CLASSES:
        try:
            bpy.utils.register_class(cls)
        except Exception as e:
            print(f"[FlowKeys Lite] Could not register panel class {cls.__name__}: {e}")

def unregister():
    for cls in reversed(CLASSES):
        try:
            bpy.utils.unregister_class(cls)
        except Exception as e:
            print(f"[FlowKeys Lite] Could not unregister panel class {cls.__name__}: {e}")
