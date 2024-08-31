Controls
========

.. _alert:

alert
---------------------

.. code:: Jinja

    {% import "jinja_flowbite/controls/alert.jinja" as flowbite_alert %}

    {{ flowbite_alert.render(text="This is a success alert", type="success") }}
    {{ flowbite_alert.render(text="This is a warning alert", type="warning") }}
    {{ flowbite_alert.render(text="This is a failure alert", type="danger") }}
    

.. figure:: /images/alerts-light.png
   :alt: Alerts Light
   :align: center

   Alerts (Light)

.. figure:: /images/alerts-dark.png
   :alt: Alerts Dark
   :align: center

   Alerts (Dark)

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
    {% import "jinja_flowbite/icons/plus.jinja" as flowbite_plus_icon %}

    <div class="flex flex-col space-y-4">
        <div>
            {{ flowbite_button.render( style="default", text="Default" ) }}
        </div>
        <div>
            {{ flowbite_button.render( style="primary", text="Primary" ) }}
        </div>
        <div>
            {{ flowbite_button.render( style="primary", text="Primary (disabled)", disabled="true" ) }}
        </div>
        <div>
            {% call flowbite_button.render(style="primary") %}
                <div class="flex items-center space-x-3">
                    {{ flowbite_plus.render() }}
                    <p>Primary with Icon</p>
                </div>
            {% endcall %}
        </div>
        <div>
            {% call flowbite_button.render( style="primary", tooltip="A tooltip") %}
                <div class="flex items-center space-x-3">
                    {{ flowbite_plus_icon.render() }}
                    <p>Primary with Icon & Tooltip</p>
                </div>
            {% endcall %}
        </div>
        <div>
            {{ flowbite_button.render( style="spinner" ) }}
        </div>
        
    </div>

.. |buttons_light| image:: /images/buttons-light.gif
   :scale: 100%

.. |buttons_dark| image:: /images/buttons-dark.gif
   :scale: 100%

+-----------------+----------------+
| |buttons_light| | |buttons_dark| |
+-----------------+----------------+
|  Light          | Dark           |
+-----------------+----------------+




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


.. |card_light| image:: /images/card-light.png
   :scale: 100%

.. |card_dark| image:: /images/card-dark.png
   :scale: 100%

+--------------+----------------+
| |card_light| | |card_dark|    |
+--------------+----------------+
|  Light       | Dark           |
+--------------+----------------+




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
