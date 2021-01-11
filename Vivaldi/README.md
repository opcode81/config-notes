# Initial Configuration

0. Open Vivaldi
1. Go to [vivaldi://experiments/](vivaldi://experiments/)
2. Enable ***Allow for using CSS modifications***
3. Go to [vivaldi://settings/appearance/](vivaldi://settings/appearance/)
4. Enable ***Open Settings in a Tab***
5. Set the ***Custom UI Modifications*** folder to `./ui-mods/css`
6. Close Vivaldi
7. Run apply-ui-mods as admin: `elevate -k python apply-ui-mods.py`
8. Reopen Vivaldi

# Restore Search Engines

1. Go to [vivaldi://settings/search/](vivaldi://settings/search/)
2. Click ***Restore Backup*** and paste contents from `./settings/search-engines.json`

# Restore Theme

1. Go to [vivaldi://settings/themes/](vivaldi://settings/themes/)
2. Add a new theme, click ***Edit Theme***, then click ***Import*** and paste contents from `./settings/theme-dj.json`

