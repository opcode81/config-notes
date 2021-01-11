from __future__ import print_function
import time
import ctypes, os
import shutil
import re
 
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def findVivaldiDir():
    base = "C:/Program Files/Vivaldi/Application"
    for fn in os.listdir(base):
        print(fn)
        if "0" <= fn[0] <= "9":
            return os.path.abspath("/".join([base, fn]))
    raise Exception("Could not find Vivaldi directory")
    

if not isAdmin():
    raise Exception("Must run as administrator")

vivaldiVersionRoot = findVivaldiDir()
print("Vivaldi is located in %s" % vivaldiVersionRoot)
resourcesDir = os.path.join(vivaldiVersionRoot, "resources", "vivaldi")

scripts = []
for fn in os.listdir("ui-mods"):
    if fn.endswith(".js"):
        scripts.append(fn)

browserHtml = os.path.join(resourcesDir, "browser.html")

shutil.copy(browserHtml, browserHtml + ".%d" % int(time.time()) + ".bak")

with open(browserHtml, "r") as f:
    html = f.read()

tag = "<!-- usermod -->"
if tag in html:
    tagre = re.escape(tag)
    html = re.sub(r'%s.*?%s' % (tagre, tagre), "", html, flags=re.DOTALL|re.MULTILINE)

lines = ["\n", tag]
for script in scripts:
    _script = "usermod__%s" % script
    shutil.copy(os.path.join("ui-mods", script), os.path.join(resourcesDir, _script))
    lines.append('<script src="%s"></script>' % _script)
lines.append(tag)
lines.append("\n")
patch = "\n".join(lines)
html = html.replace("</body>", patch + "</body>")
print("Patch applied:\n%s" % patch)

with open(browserHtml, "w") as f:
    f.write(html)
