# P3 Protocol

Personal exercise tracker for restoration, foundation and stretch work.

## Files

```
index.html       ← the full app (no build step)
exercises.json   ← your exercise list (edit this to update exercises on all devices)
manifest.json    ← PWA manifest (enables "Add to Home Screen")
```

## Deploy to Vercel (one-time, ~10 min)

1. **Create a GitHub account** if you don't have one: https://github.com
2. **Create a new repo** on GitHub called `p3-protocol` (public or private, both work)
3. **Upload these files** via GitHub's web UI:
   - Click "Add file" → "Upload files"
   - Drag in `index.html`, `exercises.json`, `manifest.json`
   - Commit
4. **Connect to Vercel**:
   - Go to https://vercel.com and sign in with GitHub
   - Click "Add New Project"
   - Import your `p3-protocol` repo
   - Framework preset: **Other** (no framework)
   - Click Deploy — done in ~30 seconds
5. Vercel gives you a URL like `https://p3-protocol.vercel.app`

## Add to Home Screen (iOS)

1. Open the Vercel URL in Safari
2. Tap the Share button (box with arrow)
3. Tap "Add to Home Screen"
4. Done — it opens like a native app

## Add to Home Screen (Android)

1. Open the Vercel URL in Chrome
2. Tap the three-dot menu
3. Tap "Add to Home screen"

## Updating your exercise list

Edit `exercises.json` directly on GitHub (click the file → pencil icon → commit).
Any device opening the app will get the updated list on next load.

**Note**: existing per-device progress/settings live in localStorage and are not
affected by edits to `exercises.json` unless you hit "Reset to defaults" in Settings.

## Syncing between devices

- **Export** a backup from the Manage tab on device A
- **Import** it on device B
- Or use "Reset to defaults" on a new device to start fresh with the latest `exercises.json`
