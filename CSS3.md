# CSS3 Interview Questions

This document contains a comprehensive list of 100 CSS3 interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and front-end interview handbooks.

## Basic (20 Questions)

### 1. What does CSS stand for?
**Answer:** Cascading Style Sheets.
**Example:** `body { color: blue; }`
**Reference:** [MDN CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

### 2. What is the Box Model in CSS?
**Answer:** 
**The Core Concept:**
A box that wraps around every HTML element.

**Key Details:**
- It consists of: margins, borders, padding, and the actual content.
**Example:** `div { width: 100px; padding: 10px; border: 1px solid black; margin: 10px; }`
**Reference:** [MDN Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

### 3. What is the difference between `padding` and `margin`?
**Answer:** 
**The Core Concept:**
Padding is the space inside the border, between the content and the border.

**Key Details:**
- Margin is the space outside the border, pushing other elements away.
**Example:** `padding: 10px; margin: 20px;`
**Reference:** [MDN Box Model Properties](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

### 4. How do you include CSS in HTML?
**Answer:** Inline (using `style` attribute), Internal (using `<style>` tag in head), and External (using `<link>` tag pointing to a `.css` file).
**Example:** `<link rel="stylesheet" href="style.css">`
**Reference:** [MDN How CSS works](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_works)

### 5. What are CSS Selectors?
**Answer:** Patterns used to select the elements you want to style.
**Example:** `.class`, `#id`, `element`.
**Reference:** [MDN Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

### 6. What is the difference between an ID selector and a Class selector?
**Answer:** 
**The Core Concept:**
An ID is unique and can only be used once per page (`#id`).

**Key Details:**
- A class can be used on multiple elements (`.class`).
**Example:** `#header {}` vs `.btn {}`
**Reference:** [MDN Class and ID selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors)

### 7. What is the universal selector?
**Answer:** The asterisk `*` selects all elements on the page.
**Example:** `* { box-sizing: border-box; }`
**Reference:** [MDN Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)

### 8. What does `box-sizing: border-box` do?
**Answer:** It tells the browser to include padding and border in the element's total width and height.
**Example:** `width: 100px` stays exactly 100px wide, even with padding.
**Reference:** [MDN box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing)

### 9. What is the difference between `display: none` and `visibility: hidden`?
**Answer:** 
**The Core Concept:**
`display: none` removes the element from the document flow (takes zero space).

**Key Details:**
- `visibility: hidden` hides the element, but it still takes up the same physical space.
**Example:** `.hidden { visibility: hidden; }`
**Reference:** [MDN visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)

### 10. What are pseudo-classes?
**Answer:** Keywords added to a selector that specify a special state of the selected elements.
**Example:** `a:hover { color: red; }`
**Reference:** [MDN Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

### 11. What are pseudo-elements?
**Answer:** Keywords added to a selector that let you style a specific part of the selected element.
**Example:** `p::first-line { font-weight: bold; }`
**Reference:** [MDN Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

### 12. How do you center a block element horizontally?
**Answer:** By setting a specific width and using `margin: 0 auto;`.
**Example:** `div { width: 50%; margin: 0 auto; }`
**Reference:** [MDN Centering](https://developer.mozilla.org/en-US/docs/Learn/CSS/Howto/Center_an_item)

### 13. What is CSS Specificity?
**Answer:** The set of rules applied by browsers to determine which CSS property is applied when multiple rules target the same element.
**Example:** Inline styles (1000) > IDs (100) > Classes (10) > Elements (1).
**Reference:** [MDN Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

### 14. What does the `!important` rule do?
**Answer:** It breaks the natural cascading rules and gives a property the highest specificity, overriding all other declarations.
**Example:** `color: red !important;`
**Reference:** [MDN !important](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity#the_!important_exception)

### 15. What are CSS variables (Custom Properties)?
**Answer:** Entities defined by CSS authors that contain specific values to be reused throughout a document.
**Example:** `--main-color: blue; color: var(--main-color);`
**Reference:** [MDN CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

### 16. What is `display: flex`?
**Answer:** It enables a Flexbox layout, which provides a more efficient way to lay out, align, and distribute space among items in a container, even when their size is unknown.
**Example:** `.container { display: flex; }`
**Reference:** [MDN Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)

### 17. What is `display: grid`?
**Answer:** It enables a CSS Grid layout, a 2-dimensional layout system for the web that lets you lay content out in rows and columns.
**Example:** `.grid { display: grid; grid-template-columns: 1fr 1fr; }`
**Reference:** [MDN Grid](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids)

### 18. What is the difference between `position: relative` and `position: absolute`?
**Answer:** 
**The Core Concept:**
`relative` positions an element relative to its normal position.

**Key Details:**
- `absolute` removes it from the document flow and positions it relative to its closest positioned ancestor.
**Example:** `.child { position: absolute; top: 0; }`
**Reference:** [MDN Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

### 19. What is `position: fixed`?
**Answer:** 
**The Core Concept:**
Removes the element from the document flow and positions it relative to the viewport.

**Key Details:**
- It does not move when the page is scrolled.
**Example:** `nav { position: fixed; top: 0; width: 100%; }`
**Reference:** [MDN Fixed position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

### 20. What is a CSS media query?
**Answer:** A technique used in responsive web design to apply CSS rules only when certain conditions (like screen width) are met.
**Example:** `@media (max-width: 600px) { body { font-size: 14px; } }`
**Reference:** [MDN Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)


## Medium (30 Questions)

### 21. What is the difference between `inline`, `inline-block`, and `block`?
**Answer:** 
**The Core Concept:**
`block` takes full width and starts a new line.

**Key Details:**
- `inline` takes necessary width, no new line, and ignores top/bottom margins/padding.
- `inline-block` is like `inline` but respects width, height, margins, and padding.
**Example:** `span { display: inline-block; width: 50px; }`
**Reference:** [MDN Display](https://developer.mozilla.org/en-US/docs/Web/CSS/display)

### 22. What is the stacking context and `z-index`?
**Answer:** 
**The Core Concept:**
`z-index` controls the vertical stacking order.

**Key Details:**
- It only works on positioned elements.
- The stacking context is a 3D conceptualization of HTML elements along an imaginary z-axis.
- An element with lower stacking context can never overlap one with higher, regardless of `z-index`.
**Example:** `.modal { z-index: 1000; position: absolute; }`
**Reference:** [MDN Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Understanding_z-index/Stacking_context)

### 23. What are CSS Sprites?
**Answer:** A technique of combining multiple small images into a single image file to reduce HTTP requests, displaying parts of it using `background-position`.
**Example:** `background: url(sprite.png) -20px -50px;`
**Reference:** [MDN Image Sprites](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Images/Implementing_image_sprites_in_CSS)

### 24. What are CSS preprocessors?
**Answer:** Tools (like Sass, LESS) that extend CSS with variables, mixins, and nesting, compiling down to standard CSS.
**Example:** `SCSS: $color: red; .box { color: $color; }`
**Reference:** [MDN Preprocessors](https://developer.mozilla.org/en-US/docs/Glossary/CSS_preprocessor)

### 25. What is BEM methodology?
**Answer:** 
**The Core Concept:**
Block Element Modifier.

**Key Details:**
- A naming convention for CSS classes to keep them flat and highly maintainable.
**Example:** `.card {}`, `.card__title {}`, `.card--dark {}`
**Reference:** [BEM Documentation](https://en.bem.info/methodology/)

### 26. Explain the difference between `em` and `rem`.
**Answer:** 
**The Core Concept:**
`em` is relative to the font-size of its direct or nearest parent.

**Key Details:**
- `rem` is relative only to the root (`<html>`) font-size.
**Example:** `margin: 2rem;` (If root is 16px, margin is 32px).
**Reference:** [MDN CSS values](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)

### 27. What are CSS transitions?
**Answer:** Allow you to change property values smoothly (from one value to another) over a given duration.
**Example:** `button { transition: background-color 0.3s ease; }`
**Reference:** [MDN Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

### 28. What are CSS animations?
**Answer:** Let you animate transitions from one CSS style to another using `@keyframes`.
**Example:** `@keyframes spin { 100% { transform: rotate(360deg); } }`
**Reference:** [MDN Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations)

### 29. What is the difference between `transition` and `animation`?
**Answer:** 
**The Core Concept:**
Transitions require a trigger (like hover) to change between two states.

**Key Details:**
- Animations don't need a trigger, can loop indefinitely, and use multiple keyframes for complex movements.
**Example:** Hover vs Spinning loader.
**Reference:** [CSS Tricks - Animation vs Transition](https://css-tricks.com/css-animations-vs-transitions/)

### 30. How do you create a triangle with CSS?
**Answer:** By using a 0 width/height element with thick borders, where one border has a color and the others are transparent.
**Example:** `border-left: 5px solid transparent; border-bottom: 5px solid red;`
**Reference:** [CSS Tricks - Triangles](https://css-tricks.com/snippets/css/css-triangle/)

### 31. What is responsive web design?
**Answer:** An approach to web design that makes web pages render well on a variety of devices and window or screen sizes, typically using media queries, fluid grids, and flexible images.
**Example:** Using `%` widths and `@media` queries.
**Reference:** [MDN Responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

### 32. What is mobile-first design?
**Answer:** Styling for mobile screens first as the default, then adding complexity via `min-width` media queries for larger screens.
**Example:** `@media (min-width: 768px) { ... }`
**Reference:** [MDN Mobile First](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design#mobile_first)

### 33. What is progressive enhancement vs graceful degradation?
**Answer:** 
**The Core Concept:**
Progressive enhancement builds a core experience first, then adds enhancements for capable browsers.

**Key Details:**
- Graceful degradation builds for modern browsers first, then provides fallbacks for older ones.
**Example:** Base CSS -> `@supports (display: grid) { ... }`
**Reference:** [MDN Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)

### 34. What is a clear fix in CSS?
**Answer:** A CSS hack used to force an element to self-clear its floated children, so the parent doesn't collapse to zero height.
**Example:** `.clearfix::after { content: ""; display: table; clear: both; }`
**Reference:** [CSS Tricks - Clearfix](https://css-tricks.com/snippets/css/clear-fix/)

### 35. Explain `calc()` function.
**Answer:** A CSS math function that lets you perform calculations when specifying CSS property values.
**Example:** `width: calc(100% - 50px);`
**Reference:** [MDN calc](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)

### 36. What is the `vh` and `vw` unit?
**Answer:** 
**The Core Concept:**
Viewport Height (`vh`) and Viewport Width (`vw`).

**Key Details:**
- 1vh is 1% of the viewport's height.
**Example:** `height: 100vh;` (Full screen height).
**Reference:** [MDN Viewport units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#viewport-percentage_lengths)

### 37. What does `flex-wrap` do?
**Answer:** Specifies whether flex items are forced onto one line or can wrap onto multiple lines.
**Example:** `flex-wrap: wrap;`
**Reference:** [MDN flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)

### 38. Explain `justify-content` vs `align-items` in Flexbox.
**Answer:** 
**The Core Concept:**
`justify-content` aligns items along the main axis (usually horizontal).

**Key Details:**
- `align-items` aligns items along the cross axis (usually vertical).
**Example:** `justify-content: center; align-items: center;`
**Reference:** [CSS Tricks - Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

### 39. What is CSS `object-fit`?
**Answer:** Specifies how the contents of a replaced element (like `<img>` or `<video>`) should be resized to fit its container.
**Example:** `img { width: 100%; height: 100%; object-fit: cover; }`
**Reference:** [MDN object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)

### 40. What is `position: sticky`?
**Answer:** 
**The Core Concept:**
Toggles between relative and fixed depending on the scroll position.

**Key Details:**
- It behaves like relative until a given offset threshold is met, then behaves like fixed.
**Example:** `.header { position: sticky; top: 0; }`
**Reference:** [MDN sticky](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

### 41. How do you implement a CSS tooltip without JavaScript?
**Answer:** Using a pseudo-element (`::after`), setting its `content` to `attr(data-tooltip)`, initially hiding it, and showing it on `:hover`.
**Example:** `.btn::after { content: attr(data-tooltip); display: none; } .btn:hover::after { display: block; }`
**Reference:** [CSS Tooltips](https://css-tricks.com/css-tooltip/)

### 42. Explain the `ch` CSS unit.
**Answer:** 
**The Core Concept:**
Represents the width, or more precisely the advance measure, of the glyph "0" in the element's font.

**Key Details:**
- Good for limiting reading width.
**Example:** `max-width: 60ch;`
**Reference:** [MDN ch](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)

### 43. What is the `:nth-child()` selector?
**Answer:** Matches elements based on their position among a group of siblings.
**Example:** `li:nth-child(even) { background: gray; }`
**Reference:** [MDN nth-child](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)

### 44. What is the difference between `:nth-child()` and `:nth-of-type()`?
**Answer:** 
**The Core Concept:**
`:nth-child()` selects the Nth child element regardless of type.

**Key Details:**
- `:nth-of-type()` selects the Nth child of a *specific* element type.
**Example:** `p:nth-of-type(2)` selects the second paragraph, even if it's the 4th child.
**Reference:** [MDN nth-of-type](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type)

### 45. What does the `~` (tilde) selector do?
**Answer:** 
**The Core Concept:**
General sibling combinator.

**Key Details:**
- Selects all elements that follow the first element and share the same parent.
**Example:** `h1 ~ p { color: red; }` (All paragraphs after an h1).
**Reference:** [MDN General sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator)

### 46. What does the `+` (plus) selector do?
**Answer:** 
**The Core Concept:**
Adjacent sibling combinator.

**Key Details:**
- Selects an element that is *immediately* following the specified element.
**Example:** `h1 + p { margin-top: 0; }`
**Reference:** [MDN Adjacent sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Adjacent_sibling_combinator)

### 47. What does the `>` (greater than) selector do?
**Answer:** 
**The Core Concept:**
Child combinator.

**Key Details:**
- Selects elements that are direct children of the specified element.
**Example:** `ul > li { list-style: none; }` (Doesn't affect `li` inside nested `ul`).
**Reference:** [MDN Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator)

### 48. What is the `:not()` pseudo-class?
**Answer:** 
**The Core Concept:**
The negation pseudo-class.

**Key Details:**
- Matches elements that do not match the provided selector.
**Example:** `input:not([type="submit"]) { border: 1px solid black; }`
**Reference:** [MDN :not](https://developer.mozilla.org/en-US/docs/Web/CSS/:not)

### 49. What are CSS Custom Filters (Blend Modes)?
**Answer:** Blend modes define how an element's content should blend with its background or backdrop.
**Example:** `mix-blend-mode: multiply;`
**Reference:** [MDN mix-blend-mode](https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode)

### 50. What is `backdrop-filter`?
**Answer:** Lets you apply graphical effects such as blurring or color shifting to the area *behind* an element, creating "glassmorphism" effects.
**Example:** `.glass { background: rgba(255,255,255,0.5); backdrop-filter: blur(10px); }`
**Reference:** [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)


## Hard (50 Questions)

### 51. What is a Block Formatting Context (BFC)?
**Answer:** 
**The Core Concept:**
A region in which the layout of block boxes occurs and floats interact with other elements.

**Key Details:**
- BFCs contain floated children and prevent margin collapsing.
**Example:** Created by `overflow: hidden`, `display: flex`, or `display: flow-root`.
**Reference:** [MDN BFC](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Block_formatting_context)

### 52. Explain margin collapsing.
**Answer:** 
**The Core Concept:**
When the top and bottom margins of adjacent block elements combine into a single margin, taking the size of the largest margin.

**Key Details:**
- It does not happen on horizontal margins, flex items, or across BFCs.
**Example:** Parent has margin-top 10px, child has margin-top 20px, total margin top is 20px, not 30px.
**Reference:** [MDN Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)

### 53. How do you implement hardware acceleration in CSS?
**Answer:** 
**The Core Concept:**
Using properties that trigger the GPU compositor, such as `transform: translateZ(0)` or `will-change: transform`.

**Key Details:**
- This ensures smooth animations off the main thread.
**Example:** `.animate { transform: translate3d(0,0,0); }`
**Reference:** [Web.dev Hardware Acceleration](https://web.dev/animations-guide/)

### 54. What is the `will-change` property?
**Answer:** A property that hints to browsers how an element is expected to change in the future, allowing them to set up optimizations (like creating a new compositor layer) beforehand.
**Example:** `will-change: transform, opacity;`
**Reference:** [MDN will-change](https://developer.mozilla.org/en-US/docs/Web/CSS/will-change)

### 55. What is the CSS Painting API (Houdini)?
**Answer:** Part of CSS Houdini, it allows developers to write JavaScript functions that draw directly into an element's background, border, or content using a Canvas-like API.
**Example:** `background-image: paint(my-custom-pattern);`
**Reference:** [MDN CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)

### 56. What is the `clamp()` function?
**Answer:** 
**The Core Concept:**
Clamps a value between an upper and lower bound.

**Key Details:**
- It takes three parameters: a minimum value, a preferred value, and a maximum allowed value.
- Great for fluid typography.
**Example:** `font-size: clamp(1rem, 2.5vw, 2rem);`
**Reference:** [MDN clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)

### 57. What are Container Queries?
**Answer:** A newer CSS feature that allows you to apply styles to an element based on the size of its *container*, rather than the viewport size (like media queries).
**Example:** `@container (min-width: 400px) { .card { display: flex; } }`
**Reference:** [MDN Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries)

### 58. How does `grid-template-areas` work?
**Answer:** Allows you to name grid items and place them on the grid visually using ascii-art-like strings.
**Example:** `grid-template-areas: "header header" "sidebar main" "footer footer";`
**Reference:** [MDN grid-template-areas](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas)

### 59. Explain `minmax()` in CSS Grid.
**Answer:** Defines a size range greater than or equal to `min` and less than or equal to `max`.
**Example:** `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));`
**Reference:** [MDN minmax](https://developer.mozilla.org/en-US/docs/Web/CSS/minmax)

### 60. What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
**Answer:** 
**The Core Concept:**
`auto-fill` creates as many tracks as fit in the container, even if they are empty.

**Key Details:**
- `auto-fit` creates tracks but collapses empty ones to 0, stretching the filled ones to fit the container.
**Example:** `repeat(auto-fit, minmax(100px, 1fr))`
**Reference:** [CSS Tricks - auto-fit vs auto-fill](https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/)

### 61. How do you create an aspect ratio box in CSS?
**Answer:** 
**The Core Concept:**
Historically, using the `padding-top` hack (padding % is based on width).

**Key Details:**
- Modern CSS uses the `aspect-ratio` property.
**Example:** `.box { aspect-ratio: 16 / 9; }`
**Reference:** [MDN aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio)

### 62. What is `font-display: swap`?
**Answer:** 
**The Core Concept:**
An `@font-face` descriptor that dictates how a web font is displayed while downloading.

**Key Details:**
- `swap` tells the browser to use a fallback font immediately, then swap in the custom font once loaded, preventing FOIT (Flash of Invisible Text).
**Example:** `@font-face { font-family: 'MyFont'; font-display: swap; }`
**Reference:** [MDN font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)

### 63. What are CSS Modules?
**Answer:** A build step process where all class names and animation names are scoped locally by default, preventing CSS global namespace collisions.
**Example:** `import styles from './Button.module.css'; <button className={styles.btn}>`
**Reference:** [CSS Modules](https://github.com/css-modules/css-modules)

### 64. What is styled-components / CSS-in-JS?
**Answer:** A library/pattern for writing CSS within JavaScript files using tagged template literals, automatically generating unique class names for encapsulation.
**Example:** `const Button = styled.button\`color: red;\`;`
**Reference:** [Styled Components](https://styled-components.com/)

### 65. What is `content-visibility`?
**Answer:** A property that enables the browser to skip the rendering work of an element until it is needed (e.g., scrolled into view), massively improving initial load time for long pages.
**Example:** `content-visibility: auto; contain-intrinsic-size: 1000px;`
**Reference:** [Web.dev content-visibility](https://web.dev/content-visibility/)

### 66. How does CSS handle specificity resolution when specificities are identical?
**Answer:** If two rules have the exact same specificity, the one that appears *last* in the CSS document wins (the Cascade).
**Example:** `.a { color: red; } .b { color: blue; }` (If element has both, it's blue).
**Reference:** [MDN Cascade](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

### 67. Explain the `@supports` rule (Feature Queries).
**Answer:** Allows you to test whether a browser supports a particular CSS property-value pair before applying a block of CSS.
**Example:** `@supports (display: grid) { .layout { display: grid; } }`
**Reference:** [MDN @supports](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)

### 68. What are `rem` units based on if `html` font-size is not set?
**Answer:** The browser's default root font size, which is typically `16px`.
**Example:** `1rem` = `16px`.
**Reference:** [MDN CSS values](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)

### 69. What is the `pointer-events` property?
**Answer:** 
**The Core Concept:**
Defines whether or under what circumstances a particular graphic element can become the target of pointer events (like mouse clicks).

**Key Details:**
- `pointer-events: none` makes an element "click-through".
**Example:** `.overlay { pointer-events: none; }`
**Reference:** [MDN pointer-events](https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events)

### 70. How does the `:focus-within` pseudo-class work?
**Answer:** 
**The Core Concept:**
Matches an element if the element itself or any of its descendants are focused.

**Key Details:**
- Great for styling a form group when an input inside it is focused.
**Example:** `.form-group:focus-within { border-color: blue; }`
**Reference:** [MDN :focus-within](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-within)

### 71. How would you center a div vertically and horizontally without using Flexbox or Grid?
**Answer:** 
**The Core Concept:**
Use absolute positioning with `top: 50%`, `left: 50%`, and `transform: translate(-50%, -50%)`.

**Key Details:**
- The parent must have `position: relative`.
**Example:** `.child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }`
**Reference:** [CSS Centering](https://css-tricks.com/centering-css-complete-guide/)

### 72. What’s the difference between relative, absolute, fixed, and sticky positioning — and where have you practically used them?
**Answer:** 
**The Core Concept:**
`relative`: offset from normal position (used as a reference for absolute children).

**Key Details:**
- `absolute`: removed from document flow, positioned relative to nearest positioned ancestor (dropdowns/modals).
- `fixed`: relative to the viewport, stays put on scroll (navbars).
- `sticky`: toggles between relative and fixed based on scroll position (table headers).
**Example:** `position: sticky; top: 0; /* Sticks to top when scrolling down */`
**Reference:** [MDN Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

### 73. You’re asked to create a responsive layout that changes from 3 columns to 1 column on mobile — how would you do that efficiently?
**Answer:** 
**The Core Concept:**
Using CSS Grid or Flexbox combined with a media query.

**Key Details:**
- With Grid, it can be entirely query-less using `auto-fit` and `minmax`.
**Example:** `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));`
**Reference:** [Responsive Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

### 74. What does box-sizing: border-box actually fix in real-world layouts?
**Answer:** 
**The Core Concept:**
By default (`content-box`), adding padding or borders increases an element's total width/height.

**Key Details:**
- `border-box` forces padding and borders to be included *within* the specified width/height, preventing layouts from breaking or overflowing unexpectedly.
**Example:** `* { box-sizing: border-box; }`
**Reference:** [MDN box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing)

### 75. How would you improve performance on a page with heavy CSS animations and images?
**Answer:** 
**The Core Concept:**
Use `transform` and `opacity` for animations (triggers GPU compositing without layout repaints).

**Key Details:**
- Use `will-change` sparingly.
- For images, use `loading="lazy"`, modern formats (WebP), and responsive images (`srcset`).
**Example:** `animation: slide 1s; /* Using transform instead of left/margin */`
**Reference:** [CSS Performance](https://web.dev/rendering-performance/)

### 76. What are Container Queries (`@container`) and why are they considered a major architectural shift?
**Answer:** 
**The Core Concept:**
Container queries allow an element's styles to adapt based on the size of its *parent container*, not the viewport.

**Key Details:**
- This shifts architecture from "viewport-first" to "component-first," enabling truly modular and reusable components that look perfect regardless of where they are placed in a layout.
**Example:** `@container (min-width: 400px) { .card { display: flex; } }`
**Reference:** [MDN Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries)

### 77. How does Native CSS Nesting improve stylesheet maintainability?
**Answer:** 
**The Core Concept:**
Native CSS now supports nesting selectors directly within one another, mirroring the functionality previously only available in preprocessors like Sass or LESS.

**Key Details:**
- This reduces the dependency on build tools and keeps related component styles grouped logically.
**Example:** `.card { padding: 1rem; .title { font-size: 2rem; } }`
**Reference:** [MDN CSS Nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Nesting)

### 78. What makes the `:has()` pseudo-class one of the most powerful selectors in modern CSS?
**Answer:** 
**The Core Concept:**
The `:has()` selector acts as a "parent selector," allowing you to style an element based on its descendants or subsequent siblings.

**Key Details:**
- This enables complex, parent-aware styling and state management directly in CSS that previously required JavaScript event listeners.
**Example:** `.card:has(img) { padding: 0; } /* Styles the card only if it contains an image */`
**Reference:** [MDN :has()](https://developer.mozilla.org/en-US/docs/Web/CSS/:has)

### 79. How does `subgrid` solve longstanding layout issues in CSS Grid?
**Answer:** 
**The Core Concept:**
Previously, nested grids were independent of their parent's grid tracks.

**Key Details:**
- `grid-template-columns: subgrid;` allows a nested element to inherit and participate in the sizing of its parent grid, keeping disparate nested child elements (like card headers and footers) perfectly aligned across multiple columns.
**Example:** `.child { grid-template-columns: subgrid; }`
**Reference:** [MDN Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Subgrid)

### 80. What problems do Dynamic Viewport Units (`dvh`, `svh`, `lvh`) solve for mobile web design?
**Answer:** 
**The Core Concept:**
Classic viewport units (`vh`) did not account for the expansion and contraction of mobile browser address bars, causing elements to overflow unexpectedly.

**Key Details:**
- `dvh` (Dynamic), `svh` (Small), and `lvh` (Large) accurately respond to the changing UI of mobile browsers.
**Example:** `height: 100dvh; /* Adapts dynamically as the URL bar hides/shows */`
**Reference:** [MDN Viewport Concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/length)

### 81. How do Cascade Layers (`@layer`) resolve CSS specificity wars in large codebases?
**Answer:** 
**The Core Concept:**
`@layer` allows developers to define the explicit precedence of entire groups of CSS rules, regardless of selector specificity.

**Key Details:**
- This ensures that utility classes always override base components without relying on `!important` or overly complex selectors.
**Example:** `@layer reset, base, components, utilities;`
**Reference:** [MDN Cascade Layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer)

### 82. How do native Scroll-Driven Animations change frontend development?
**Answer:** 
**The Core Concept:**
Native CSS can now link animations directly to the scroll position of a container (`animation-timeline: scroll()`) rather than time.

**Key Details:**
- This eliminates the need for heavy, performance-intensive JavaScript scroll listeners (like GSAP or ScrollMagic) for basic parallax or progress bar effects.
**Example:** `.progress-bar { animation: fill-up linear; animation-timeline: scroll(); }`
**Reference:** [MDN Scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations)

### 83. Why has Utility-First CSS (like Tailwind) largely overtaken runtime CSS-in-JS in modern development stacks?
**Answer:** 
**The Core Concept:**
Runtime CSS-in-JS (like older styled-components) introduces significant runtime overhead, bundle size bloat, and hydration complexity, especially poorly suited for Server Components.

**Key Details:**
- Utility-first CSS scales better for large teams by solving naming fatigue, eliminating dead CSS, and maintaining strict design token consistency via atomic, static classes.
**Example:** Using `<div class="flex p-4 text-center">` over writing isolated, scoped `.wrapper` classes.
**Reference:** [Tailwind Utility-First](https://tailwindcss.com/docs/utility-first)

### 84. What are CSS Logical Properties and why are they replacing physical properties?
**Answer:** 
**The Core Concept:**
Physical properties (`margin-left`, `padding-top`) are strictly tied to the screen's geometry.

**Key Details:**
- Logical properties (`margin-inline-start`, `padding-block-start`) map to the text's writing mode.
- This makes building sites that support both Left-to-Right (English) and Right-to-Left (Arabic) languages completely automatic without writing separate stylesheets.
**Example:** `padding-inline-start: 10px;` (Left for English, Right for Arabic).
**Reference:** [MDN CSS Logical Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values)

### 85. What is the `prefers-color-scheme` media feature?
**Answer:** 
**The Core Concept:**
It detects if the user has requested the system use a light or dark color theme natively on their OS.

**Key Details:**
- This is the foundation of modern dark mode implementations.
**Example:** `@media (prefers-color-scheme: dark) { body { background: black; } }`
**Reference:** [MDN prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)

### 86. Why is `prefers-reduced-motion` critical for accessibility?
**Answer:** 
**The Core Concept:**
It detects if the user has requested the system to minimize the amount of non-essential motion.

**Key Details:**
- For users with vestibular disorders, heavy parallax or zoom animations can cause physical illness.
- Developers must use this query to turn off heavy animations.
**Example:** `@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }`
**Reference:** [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

### 87. What is CSS Houdini?
**Answer:** 
**The Core Concept:**
Houdini is a set of low-level APIs that expose parts of the CSS engine directly to developers, allowing them to write code (like Paint Worklets or Layout Worklets) that the browser parses as native CSS.

**Key Details:**
- This allows for entirely custom layout engines or complex visual effects without waiting for W3C standardization.
**Example:** `background: paint(my-custom-pattern);`
**Reference:** [MDN CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Houdini)

### 88. How do CSS Scroll Snap points work?
**Answer:** 
**The Core Concept:**
Scroll Snapping allows you to lock the viewport to specific elements (like a carousel item or full-page section) after a user finishes scrolling.

**Key Details:**
- It provides a native, buttery-smooth alternative to heavy JavaScript scroll-hijacking libraries.
**Example:** Parent: `scroll-snap-type: x mandatory;` Child: `scroll-snap-align: center;`
**Reference:** [MDN CSS Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap)

### 89. Explain the `clamp()` function.
**Answer:** 
**The Core Concept:**
`clamp()` enables fluid typography and layouts by defining a minimum value, a preferred dynamic value (usually viewport-based), and a maximum value.

**Key Details:**
- It replaces multiple media queries with a single line of CSS.
**Example:** `font-size: clamp(1rem, 2.5vw, 2rem);`
**Reference:** [MDN clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)

### 90. What is the difference between `min()`, `max()`, and `clamp()`?
**Answer:** 
**The Core Concept:**
`min()` chooses the smallest of a set of values, acting as a maximum boundary.

**Key Details:**
- `max()` chooses the largest, acting as a minimum boundary.
- `clamp()` combines both to strictly lock a responsive value within bounds.
**Example:** `width: min(100%, 500px);` (Will be 100% until the container exceeds 500px).
**Reference:** [MDN CSS Math Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Functions)

### 91. What is the `backdrop-filter` property used for?
**Answer:** 
**The Core Concept:**
It applies graphical effects (like blurring or color shifting) to the area *behind* an element.

**Key Details:**
- It is the core property used to achieve "glassmorphism" (frosted glass UI effects) natively in CSS.
**Example:** `.glass-card { background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); }`
**Reference:** [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)

### 92. Explain the `aspect-ratio` property.
**Answer:** 
**The Core Concept:**
It allows you to natively define the proportional relationship between an element's width and height.

**Key Details:**
- It replaces the old "padding-bottom hack" historically used to maintain responsive iframe and image ratios.
**Example:** `.video { aspect-ratio: 16 / 9; }`
**Reference:** [MDN aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio)

### 93. What is the `all` property in CSS?
**Answer:** 
**The Core Concept:**
The `all` property resets all of an element's CSS properties (except `unicode-bidi` and `direction`) to their initial or inherited state.

**Key Details:**
- It is highly useful when building isolated web components or completely resetting a third-party widget.
**Example:** `all: unset;`
**Reference:** [MDN all](https://developer.mozilla.org/en-US/docs/Web/CSS/all)

### 94. How does `isolation: isolate` fix z-index issues?
**Answer:** 
**The Core Concept:**
`isolation: isolate` forces the creation of a new stacking context on an element.

**Key Details:**
- This ensures that the z-indexes of its children are contained and cannot break out to interleave with elements outside the parent, curing z-index specificity wars.
**Example:** `.modal-wrapper { isolation: isolate; }`
**Reference:** [MDN isolation](https://developer.mozilla.org/en-US/docs/Web/CSS/isolation)

### 95. What are the `:is()` and `:where()` pseudo-classes?
**Answer:** 
**The Core Concept:**
Both are selector lists that drastically reduce CSS repetition.

**Key Details:**
- They allow you to write `.header :is(h1, h2, h3)` instead of `.header h1, .header h2, .header h3`.
- The key difference is specificity: `:is()` takes the specificity of its most specific argument, while `:where()` has 0 specificity.
**Example:** `:where(.btn, button) { padding: 1rem; }`
**Reference:** [MDN :is](https://developer.mozilla.org/en-US/docs/Web/CSS/:is)

### 96. What is the `color-mix()` function?
**Answer:** 
**The Core Concept:**
A modern CSS function that takes two colors and returns the result of mixing them in a specified color space and percentage.

**Key Details:**
- It replaces Sass `mix()` and `darken()/lighten()` functions.
**Example:** `background: color-mix(in srgb, blue 50%, white);`
**Reference:** [MDN color-mix()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix)

### 97. What is `oklch()` and why is it preferred over `hsl()` in modern design systems?
**Answer:** 
**The Core Concept:**
OKLCH is a modern perceptual color space.

**Key Details:**
- Unlike HSL, where "blue" at 50% lightness looks completely different from "yellow" at 50% lightness, OKLCH guarantees uniform perceptual lightness across the entire color wheel, making algorithmic palette generation perfectly accessible.
**Example:** `color: oklch(60% 0.15 50);`
**Reference:** [MDN OKLCH](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch)

### 98. What is the `content-visibility` property?
**Answer:** 
**The Core Concept:**
An advanced performance property that allows the browser to skip the layout and rendering work of an element entirely until it approaches the viewport.

**Key Details:**
- It acts similarly to lazy loading, but for the DOM rendering phase, heavily improving initial load times on massive pages.
**Example:** `.footer { content-visibility: auto; }`
**Reference:** [MDN content-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility)

### 99. Explain `overscroll-behavior`.
**Answer:** 
**The Core Concept:**
Controls what the browser does when reaching the boundary of a scrolling area.

**Key Details:**
- Setting it to `contain` or `none` prevents "scroll chaining" (where scrolling a child modal inadvertently scrolls the background body).
**Example:** `.modal { overscroll-behavior: contain; }`
**Reference:** [MDN overscroll-behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior)

### 100. How do CSS Custom Properties (Variables) differ from preprocessor variables (Sass)?
**Answer:** 
**The Core Concept:**
Sass variables (`$color`) are compiled away at build time and do not exist in the browser.

**Key Details:**
- CSS Custom Properties (`--color`) live in the DOM, inherit through the cascade, and can be manipulated by JavaScript or Media Queries at runtime dynamically.
**Example:** `:root { --primary: blue; }`
**Reference:** [MDN CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
