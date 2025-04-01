1. Install Flet (using a Python package manager, like uv)
(see https://flet.dev/docs/getting-started/)

```bash
mkdir my-app
cd my-app
uv init
uv add 'flet[all]' --dev
uv run flet --version
```

Then, the following command initialises/creates a sample app:

```bash
uv run flet create
```

(see the point n. 2, below)

Running the app as a desktop app is as simple as launching

```bash
uv run flet run
```



2. Packaging app for macOS (and iOS?) requires having
- Rosetta 2 installed
- XCode installed (see the App Store and then )
- CocoaPods installed (see https://cocoapods.org/)

Note the following script detects whether Rosetta 2 is already there.

```bash
#!/bin/sh

# If cpu is Apple branded, use arch binary to check if x86_64 code can run
if [[ "$(sysctl -n machdep.cpu.brand_string)" == *'Apple'* ]]; then
    if arch -x86_64 /usr/bin/true 2> /dev/null; then
        result="Installed"
    else
        result="Missing"
    fi
else
    result="Ineligible"
fi

echo "<result>$result</result>"
```


I took the bell sound from https://pixabay.com/sound-effects/search/meditation-bell/




