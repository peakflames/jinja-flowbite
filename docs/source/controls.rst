Controls
========


alert
---------------------

.. code:: Jinja

    {% import "jinja_flowbite/controls/alert.jinja" as flowbite_alert %}

    {{ flowbite_alert.render(text="An error msg", type="danger") }}
    {{ flowbite_alert.render(text="An warning msg", type="warning") }}
    {{ flowbite_alert.render(text="An success msg", type="success") }}



+-----------+------+--------------------------------------------------------+
| Attribute | Type | Description                                            |
+===========+======+========================================================+
| id        | str  | Sets the div containers id attribute.                  |
+-----------+------+--------------------------------------------------------+
|| type     || str || Supported values include                              |
||          ||     || - `danger`                                            |
||          ||     || - `warning`                                           |
||          ||     || - `success`                                           |
+-----------+------+--------------------------------------------------------+
| text      | str  | The text to be displayed                               |
+-----------+------+--------------------------------------------------------+
| class     | str  | Additional css classes to be appended to the component |
+-----------+------+--------------------------------------------------------+




anchor
---------------------

.. code:: Jinja

    {% import "jinja_flowbite/controls/anchor.jinja" as flowbite_anchor %}

    {{ flowbite_anchor.render(text="Flowbite", href="https://www.flowbite.com", new_tab=True) }}



+-----------+------+--------------------------------------------------------+
| Attribute | Type | Description                                            |
+===========+======+========================================================+
| id        | str  | Sets the `id`` attribute of the main element.          |
+-----------+------+--------------------------------------------------------+
| text      | str  | The text to be displayed                               |
+-----------+------+--------------------------------------------------------+
| href      | str  | The href of the anchor                                 |
+-----------+------+--------------------------------------------------------+
| new_tab   | bool | True will open the link in a new browser tab           |
+-----------+------+--------------------------------------------------------+
| class     | str  | Additional css classes to be appended to the component |
+-----------+------+--------------------------------------------------------+



badge
---------------------

.. code:: Jinja

    {% import "jinja_flowbite/controls/badge.jinja" as flowbite_badge %}

    {{ flowbite_badge.render(type="error", text="error text", class="w-16") }}
    {{ flowbite_badge.render(type="warning", text="warning text", class="w-16") }}
    {{ flowbite_badge.render(type="success", text="success text", class="w-16") }}
    {{ flowbite_badge.render(type="dark", text="dark text", class="w-16") }}


+-----------+------+--------------------------------------------------------+
| Attribute | Type | Description                                            |
+===========+======+========================================================+
| id        | str  | Sets the div containers id attribute.                  |
+-----------+------+--------------------------------------------------------+
|| type     || str || Supported values include                              |
||          ||     || - `danger`                                            |
||          ||     || - `warning`                                           |
||          ||     || - `success`                                           |
||          ||     || - `dark`                                              |
+-----------+------+--------------------------------------------------------+
| text      | str  | The text to be displayed                               |
+-----------+------+--------------------------------------------------------+
| class     | str  | Additional css classes to be appended to the component |
+-----------+------+--------------------------------------------------------+
| text_size | str  | default: `text-xs`                                     |
+-----------+------+--------------------------------------------------------+



button
---------------------

.. code:: Jinja

    {% import "jinja_flowbite/controls/button.jinja" as flowbite_button %}

    {# Example of a simple button #}
    {{ flowbite_button.render(text="Back", 
                              style="primary", 
                              additional_attribs="onclick='history.back()'") }}

    {# Example of a simple button with an icon #}
    {% call flowbite_button.render(type="submit", style="primary", class="w-full") %}
        <div class="flex items-center space-x-3 justify-center whitespace-nowrap">
            {{ flowbite_folder_icon.render() }}
            <p>Open Folder</p>
        </div>
    {% endcall %}


+--------------------+------+--------------------------------------------------------+
| Attribute          | Type | Description                                            |
+====================+======+========================================================+
| id                 | str  | Sets the div containers id attribute.                  |
+--------------------+------+--------------------------------------------------------+
|| style             || str || Supported values include:                             |
||                   ||     || - `default`                                           |
||                   ||     || - `primary`                                           |
||                   ||     || - `spinner`                                           |
+--------------------+------+--------------------------------------------------------+
| type               | str  | default: button. HTML Button type enumeration          |
+--------------------+------+--------------------------------------------------------+
| class              | str  | Additional css classes to be appended to the component |
+--------------------+------+--------------------------------------------------------+
| tooltip            | str  | default: None. Display a tooltip with the button       |
+--------------------+------+--------------------------------------------------------+
| disabled           | bool | default: False.                                        |
+--------------------+------+--------------------------------------------------------+
| padding            | str  | default: `"px-4 py-2"`                                 |
+--------------------+------+--------------------------------------------------------+
| spacing            | str  | default: `"space-x-1"`                                 |
+--------------------+------+--------------------------------------------------------+
| additional_attribs | str  | raw html attributes pass to the element                |
+--------------------+------+--------------------------------------------------------+



card
---------------------
.. code:: Jinja

    {% import "jinja_flowbite/controls/card.jinja" as flowbite_card %}
    {% import "jinja_flowbite/icons/plus.jinja" as flowbite_plus_icon %}

    {# Example card (simple) #}
    {% call(section) flowbite_card.render(title="Simple Card") %}

        {% if section == "body" %}
            <p>This is the card body</p>
        {% endif %}
    
    {% endcall %}

    {# Example card (Enhanced) #}
    {% call(section) flowbite_card.render(title="Enhanced Card", 
                                          subtitle="Subtitle Text",
                                          show_header_subtitle=True, 
                                          enable_header_bg=True) %}

        {% if section == "header_controls" %}
            {{ flowbite_plus_icon.render()  }}
        {% endif %}
        
        {% if section == "body" %}
            <p>This is the card body</p>
        {% endif %}
    
    {% endcall %}


+--------------------------+------+--------------------------------------------------------+
| Attribute                | Type | Description                                            |
+==========================+======+========================================================+
| id                       | str  | Sets the div containers id attribute.                  |
+--------------------------+------+--------------------------------------------------------+
| class                    | str  | Additional css classes to be appended to the component |
+--------------------------+------+--------------------------------------------------------+
| show_header              | bool | default: True.                                         |
+--------------------------+------+--------------------------------------------------------+
| show_header_subtitle     | bool | default: False.                                        |
+--------------------------+------+--------------------------------------------------------+
| show_header_controls     | bool | default: True.                                         |
+--------------------------+------+--------------------------------------------------------+
| title                    | str  |                                                        |
+--------------------------+------+--------------------------------------------------------+
| subtitle                 | str  |                                                        |
+--------------------------+------+--------------------------------------------------------+
| title_text_size_class    | str  | default: `"text-lg"`.                                  |
+--------------------------+------+--------------------------------------------------------+
| subtitle_text_size_class | str  | default: `"text-base"`.                                |
+--------------------------+------+--------------------------------------------------------+
| header_bg_class          | str  | default: `"bg-gray-50 dark:bg-gray-700"`.              |
+--------------------------+------+--------------------------------------------------------+
| enable_header_bg         | bool |                                                        |
+--------------------------+------+--------------------------------------------------------+
|| caller sections         || str || Supported values include:                             |
||                         ||     || - `header_controls`                                   |
||                         ||     || - `body`                                              |
+--------------------------+------+--------------------------------------------------------+


checkbox
---------------------

dark_mode_toggle
---------------------

error_card
---------------------

help_tooltip
---------------------

input_label
---------------------

input_text
---------------------

select
---------------------

spinner
---------------------

tabs
---------------------

tab_control
---------------------

tab_control
^^^^^^^^^^^^^^^^^^^^^^^^^

table
--------------------------------

table_static
^^^^^^^^^^^^^^^^^^^^^^^^^

table_static_header_cell
^^^^^^^^^^^^^^^^^^^^^^^^^

table_static_row
^^^^^^^^^^^^^^^^^^^^^^^^^

table_static_row_cell
^^^^^^^^^^^^^^^^^^^^^^^^^


toast
---------------------

tooltip
---------------------
