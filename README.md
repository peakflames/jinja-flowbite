# Flowbite-Based Jinja Components

## Getting Started for Flask

1. Add the `jinja-flowbite` package to your python environment

    - Option 1: Add it to your `requirements.txt`
    - Option 2: Add it to your `pyproject.toml` if you are using `poetry`
    - Option 3: Install to your global packages: `pip install jinja-flowbite`

1. Register the `jinja-flowbite` package to the Flask runtime

    ```python
    from flask import Flask
    import jinja2

    app = Flask(__name__,)
    app.jinja_env.auto_reload = True

    enhanced_loader = jinja2.ChoiceLoader([
        jinja2.PackageLoader("jinja_flowbite", ""),
        app.jinja_loader
    ])

    app.jinja_loader = template_loader
    ```

1. Register the `jinja-flowbite` source file with Tailwind configurations

    > NOTE: Below is a standard flowbite setup with the key addition of adding the
    > `jinja-flowbite` package .jinja files to the `content` section.

    ```json
    /** @type {import('tailwindcss').Config} */
    module.exports = {
    
    content: [
        ".your_app_folder/templates/**/*.{html,jinja}",
        "./src/static/js/**/*.js",
        "./node_modules/flowbite/**/*.js",
        "./venv/Lib/site-packages/jinja-flowbite/**/*.{html,jinja}",
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                primary: { "50": "#eff6ff", "100": "#dbeafe", "200": "#bfdbfe", "300": "#93c5fd", "400": "#60a5fa", "500": "#3b82f6", "600": "#2563eb", "700": "#1d4ed8", "800": "#1e40af", "900": "#1e3a8a", "950": "#172554" }
            },
            maxHeight: {
                'table-xl': '60rem',
            }
        },
        fontFamily: {
            'body': [
                'Inter',
                'ui-sans-serif',
                'system-ui',
                '-apple-system',
                'system-ui',
                'Segoe UI',
                'Roboto',
                'Helvetica Neue',
                'Arial',
                'Noto Sans',
                'sans-serif',
                'Apple Color Emoji',
                'Segoe UI Emoji',
                'Segoe UI Symbol',
                'Noto Color Emoji'
            ],
            'sans': [
                'Inter',
                'ui-sans-serif',
                'system-ui',
                '-apple-system',
                'system-ui',
                'Segoe UI',
                'Roboto',
                'Helvetica Neue',
                'Arial',
                'Noto Sans',
                'sans-serif',
                'Apple Color Emoji',
                'Segoe UI Emoji',
                'Segoe UI Symbol',
                'Noto Color Emoji'
            ],
            'mono': [
                'ui-monospace',
                'SFMono-Regular',
                'MesloLGL Nerd Font Mono', 
                'Cascadia Mono',
                'Courier New'
            ]
        }
    },
    plugins: [
        require('flowbite/plugin')
    ],
    }
    ```

1. In your HTML template, import the Components and use as Jinja macros

    ```html
    {% import "jinja_flowbite/controls/button.jinja" as Button %}
    {% import 'jinja_flowbite/controls/card.jinja' as Card %}

    <div class="flex flex-col items-center space-y-6">
        
        {{ Card.render(title="This is a card") }}

        {{ Button.render(text="Click me") }}

    <div>
    ```

