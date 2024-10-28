# Initial Configuration

In the following, `.` refers to the directory this README is in.

1. Enable CSS modifications (in particular, for multi-line tabs; tabs configured at bottom recommended)
   1. Open Vivaldi
   2. Go to [vivaldi://experiments/](vivaldi://experiments/)
   3. Enable ***Allow for using CSS modifications***
   4. Go to [vivaldi://settings/appearance/](vivaldi://settings/appearance/)
   5. Enable ***Open Settings in a Tab***
   6. Set the ***Custom UI Modifications*** folder to `./ui-mods/css`
   7. Optionally edit `./ui-mods/css/multiline-tabs.css` to modify the desired tab width. The default width of `308px` is designed for 6 tabs at 1920x1080 when using 100% scaling (with some pixels left over for tool icons displayed by default). To maintain 6 tabs when using, for example, 125% scaling, scale the width accordingly (308/1.25).
   8. Close Vivaldi
2. Enable additional UI modifications (allowing theme export/import & search settings export/import)
   1. Run apply-ui-mods as admin: `elevate -k python apply-ui-mods.py`
3. Reopen Vivaldi and enjoy the modifications

# Debugging the Vivaldi UI

The Vivaldi UI changes sometimes, requiring changes to the CSS.
To debug the Vivaldi UI, follow the instructions [here](https://forum.vivaldi.net/topic/16684/inspecting-the-vivaldi-ui-with-devtools)

# Restore Search Engines

1. Go to [vivaldi://settings/search/](vivaldi://settings/search/)
2. Click ***Restore Backup*** and paste contents from `./settings/search-engines.json`

# Restore Theme

1. Go to [vivaldi://settings/themes/](vivaldi://settings/themes/)
2. Add a new theme, click ***Edit Theme***, then click ***Import*** and paste contents from `./settings/theme-dj.json`

