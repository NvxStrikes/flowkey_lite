# FlowKeys Lite

**FlowKeys Lite** is a clean, lightweight, distraction-free shortcut reference panel that lives directly in Blender's N-panel sidebar.

This is the **free Lite version**. It shows essential **Object Mode shortcuts only**, so you can keep your flow without viewport clutter, and see if FlowKeys fits your workflow before upgrading.

---

## Features

- **Object Mode reference:** Hotkeys for selection, transforms, camera/view, and general operations, grouped into Selection, Transform, Object, View, and General.
- **Native Blender look:** Built with Blender's own box layouts and badge-row styling so it blends into the UI.
- **Zero viewport clutter:** A passive N-Panel, nothing running in the background.
- **Cross-platform:** Windows, macOS, Linux.
- **Free and open source:** GNU GPL v3.

---

## Installation

> **Recommended: download the ZIP from the [Releases page](../../releases)** (`FlowKeys_Lite_v1.0.0.zip`), not "Download repository as ZIP". The release ZIP has the correct folder structure for Blender.

### Blender 4.2+ (Extension)

1. Open Blender.
2. Go to **Edit → Preferences → Get Extensions**.
3. Click the dropdown arrow (top-right) → **Install from Disk…**
4. Select the ZIP and click **Install**.

### Blender 4.0 / 4.1 (Legacy add-on)

1. Go to **Edit → Preferences → Add-ons**.
2. Click **Install…** and select the ZIP.
3. Enable **Interface: FlowKeys Lite**.

---

## Usage

1. Press **N** in the 3D Viewport to open the sidebar.
2. Open the **FlowKeys** tab.
3. Browse the Object Mode shortcuts by category.

---

## FlowKeys Pro vs Lite

Want every mode, search, and notes? Check out **FlowKeys Pro**.

| Feature | Lite (Free) | Pro |
| --- | :---: | :---: |
| Object Mode shortcuts | ✅ | ✅ |
| All 8 3D Viewport modes (Edit, Sculpt, Pose, Weight/Vertex/Texture Paint, Grease Pencil) | ❌ | ✅ |
| Video Sequencer, Timeline & Dope Sheet | ❌ | ✅ |
| Auto mode detection | ✅ | ✅ |
| Instant search | ❌ | ✅ |
| Hidden Hotkeys filter (shortcuts not in any menu) | ❌ | ✅ |
| Personal notes, global across all projects | ❌ | ✅ |
| Notes export (TXT / JSON) | ❌ | ✅ |
| Favorites, global across all projects | ❌ | ✅ |
| One-click copy shortcut | ❌ | ✅ |
| Reads your custom keymaps (✱ marks remaps) | ❌ | ✅ |
| Viewport HUD overlay | ❌ | ✅ |
| Preferences (line spacing, colors, accent, HUD anchor) | ❌ | ✅ |

👉 **[Get FlowKeys Pro](https://superhivemarket.com/products/flowkeys)** ($3.99, free updates for Pro license holders)

---

## File Structure

```
flowkeys_lite/
├── blender_manifest.toml   # Extension metadata (Blender 4.2+)
├── __init__.py             # Add-on entry point and registration
├── constants.py            # Object Mode shortcut database
├── panels.py               # UI layout drawing
└── License.txt             # GNU GPL v3
```

---

## License

Licensed under the **GNU General Public License v3**. See `License.txt`.

Built by **NovaStrikes** · [novastrikes.com](https://novastrikes.com) · contact@novastrikes.com
