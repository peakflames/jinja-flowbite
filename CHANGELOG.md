# Jinja Flowbite

## 0.4.dev12

- controls: fix bug in `table_static_row_cell.jinja`

## 0.4.dev11

- controls: improved table_static_* to apply identifiers and correct jinja syntax. This was required
  to support htmx interactions.

## 0.4.dev10

- controls: fixed bug in `toggle_switch.jinja`

## 0.4.dev9

- controls: added `toggle_switch.jinja`

## 0.4.dev8

- controls - Conditionally add the Boolean attributes for the following input controls (PR #2):
  - `input_text.jinja`
  - `select.jinja`
  - `checkbox.jinja`
- icons - add `close.jinja` icon

## 0.4.dev7

- layout - updated main_layout and stacked_layout to use `flowbite_header_content_center_outlet` block to allow for center content in header

## 0.4.dev6

- icon - add angle_left.jinja
- icon - add angle_right.jinja
- icon - add angle_up.jinja
- icon - add arrow_left.jinja
- icon - add arrow_right.jinja
- icon - add expand.jinja

## 0.4.dev5

- icon - add adjustments_horizontal.jinja
- icon - add adjustments_vertical.jinja
- icon - add annotation.jinja
- icon - add archive.jinja
- icon - add award.jinja
- icon - add badge_check.jinja
- icon - add play.jinja
- icon - add play_solid.jinja

## 0.4.dev4

- icon - add arrow_up_right.jinja

## 0.4.dev3

- bug - fix issue with pattern attribute not working for input_text

## 0.4.dev2

- `components/input_text.jinja` now supports `readonly` and `disabled` attributes

## 0.4.dev1

- remove the `p-4` from the `<main>` element of the stacked layout to all for more user control of the layout

## 0.3.dev7

- update input_text to support pattern attribute
  
## 0.3.dev6

- fix toast content spacing

## 0.3.dev5

- fix toast border

## 0.3.dev4

- fix toast bg color

## 0.3.dev3

- Add tab components that switch based anchor/query string: `tab_control_anchor` & `tab_anchor`
- Add tab components that use Flowbite javascript to hidden/show tab contents:
  - `tab_content.jinja`
  - `tab_control_body.jinja`
  - `tab_control_header.jinja`
  - `tab.jinja`

## v3.0.dev0

- Added layouts
