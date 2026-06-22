# FlowKeys Lite 

**FlowKeys Lite** is a clean, lightweight, and distraction-free shortcut reference panel that lives directly in Blender's N-panel sidebar. 

This is the **Free Lite Version**, configured to display essential **Object Mode shortcuts only** to help you keep your workflow fluid without viewport clutter.

---

## Features

- **Object Mode Reference:** Displays critical hotkeys for Object selection, transformations, camera views, and general operations.
- **Native Blender Integration:** Designed using Blender's box layouts and custom badge row styles to blend in seamlessly with the native UI.
- **Modern Extension Support:** Fully compatible as a Blender Extension for **Blender 4.2+** (uses `blender_manifest.toml`), while maintaining compatibility for legacy installations in **Blender 4.0 / 4.1**.
- **Completely Free:** Open-source under the GNU GPL v3 license.

---

## Installation Guide

### Blender 4.2+ (Extension Mode)
1. Download this repository as a ZIP archive (or download `FlowKeys_Lite_v1.0.0.zip` from releases).
2. Open Blender.
3. Go to **Edit > Preferences > Get Extensions**.
4. Click the dropdown arrow/cog in the top-right corner and choose **Install from Disk...**.
5. Select the ZIP package and click **Install**.

### Blender 4.0 / 4.1 (Legacy Mode)
1. Open Blender.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install...** in the top header and select the ZIP package.
4. Enable the checkbox next to **Interface: FlowKeys Lite**.

---

## Usage
1. Press **N** in the 3D Viewport to toggle the sidebar.
2. Select the **FlowKeys** tab.
3. Reference the Object Mode shortcuts list divided neatly into Selection, Transform, Object, View, and General categories.

---

## File Structure

```
flowkeys_lite/
├── blender_manifest.toml   # Extension metadata (Blender 4.2+)
├── __init__.py            # Addon entry point and registration logic
├── constants.py           # Object Mode shortcut database
├── panels.py              # UI layout drawing logic
└── License.txt            # GNU GPL v3 License text
```

---

## FlowKeys Pro vs Lite

If you need more advanced reference tools, check out **FlowKeys Pro**:

| Feature | Lite (Free) | Pro |
| :--- | :---: | :---: |
| **Object Mode Shortcuts** | Yes | Yes |
| **7 Additional Modes** (Edit Mesh, Sculpt, Pose, Paint Modes, Grease Pencil) | No | **Yes** |
| **Keyword & Description Search** | No | **Yes** (Instant filtering) |
| **Personal Notes** | No | **Yes** (Saved in .blend) |
| **UI Customization** (Font size scale, priority highlight, accent themes) | No | **Yes** |

*Built by NovaStrikes | contact@novastrikes.com*
