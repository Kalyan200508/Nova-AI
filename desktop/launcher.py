from desktop.apps.windows import windows_apps
from desktop.apps.browsers import browser_apps

# We'll add these in the next steps
try:
    from desktop.apps.development import development_apps
except ImportError:
    development_apps = None

try:
    from desktop.apps.folders import folder_apps
except ImportError:
    folder_apps = None

try:
    from desktop.apps.office import office_apps
except ImportError:
    office_apps = None

try:
    from desktop.apps.media import media_apps
except ImportError:
    media_apps = None


class DesktopLauncher:

    def open(self, target: str):

        target = target.lower().strip()

        modules = [
            windows_apps,
            browser_apps,
            development_apps,
            folder_apps,
            office_apps,
            media_apps,
        ]

        for module in modules:

            if module is None:
                continue

            result = module.open(target)

            if result is not None:
                return result

        return f"I don't know how to open '{target}' yet."


launcher = DesktopLauncher()