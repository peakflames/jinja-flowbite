# Flowbite-Based Jinja Components

## Getting Started for Flask

1. Add the `jinja-flowbite` package to your python environment

    - Option 1: Add it to your `requirements.txt`
    - Option 2: Add it to your `pyproject.toml` if you are using `poetry`
    - Option 3: Install to your global packages: `pip install jinja-flowbite`

2. Register the `jinja-flowbite` package to the Flask runtime

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

3. In your HTML template, import the Components and use as Jinja macros

    ```html
    {% import "jinja_flowbite/controls/button.jinja" as Button %}
    {% import 'jinja_flowbite/controls/card.jinja' as Card %}

    <div class="flex flex-col items-center space-y-6">
        
        {{ Card.render(title="This is a card") }}

        {{ Button.render(text="Click me") }}

    <div>
    ```

