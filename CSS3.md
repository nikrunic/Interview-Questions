# CSS3 Interview Questions

This document contains a comprehensive list of CSS3 interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What does CSS stand for?
**Answer:** Cascading Style Sheets. It describes how HTML elements are to be displayed on screen, paper, or in other media.
**Example:** `body { background-color: lightblue; }`
**Reference:** [MDN - CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

### 2. How do you include CSS in a web page?
**Answer:** Inline (using the `style` attribute), Internal (using the `<style>` tag in the `<head>`), and External (using the `<link>` tag to link to a `.css` file).
**Example:** `<link rel="stylesheet" href="styles.css">`
**Reference:** [MDN - How CSS works](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_works)

### 3. What is a CSS selector?
**Answer:** A CSS selector is the part of a CSS rule that describes what HTML elements the style should be applied to.
**Example:** `p { color: red; }` (Here `p` is the selector).
**Reference:** [MDN - CSS Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

### 4. What is the difference between an ID selector and a Class selector?
**Answer:** An ID selector targets a specific element with a unique ID attribute (using `#`), while a Class selector targets one or more elements with a specific class attribute (using `.`).
**Example:** `#header { color: blue; }` vs `.card { border: 1px solid black; }`
**Reference:** [MDN - Class and ID selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors)

### 5. Explain the Universal Selector.
**Answer:** The universal selector (`*`) matches elements of any type. It is often used for resetting margins and padding.
**Example:** `* { margin: 0; padding: 0; box-sizing: border-box; }`
**Reference:** [MDN - Universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)

### 6. What is the CSS Box Model?
**Answer:** The CSS box model describes the rectangular boxes generated for elements in the document tree. It consists of: margins, borders, padding, and the actual content.
**Example:** `div { width: 300px; padding: 10px; border: 5px solid gray; margin: 0; }`
**Reference:** [MDN - The box model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

### 7. What is the difference between padding and margin?
**Answer:** Padding is the space between the element's content and its border (inside). Margin is the space around the outside of the element's border (outside).
**Example:** `div { padding: 20px; margin: 10px; }`
**Reference:** [MDN - Margin vs Padding](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#margins_padding_and_borders)

### 8. How do you change the background color of an element?
**Answer:** Using the `background-color` property.
**Example:** `h1 { background-color: yellow; }`
**Reference:** [MDN - background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)

### 9. How do you change the text color?
**Answer:** Using the `color` property.
**Example:** `p { color: #333333; }`
**Reference:** [MDN - color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)

### 10. How do you make text bold?
**Answer:** Using the `font-weight` property set to `bold` or a numeric value like `700`.
**Example:** `span { font-weight: bold; }`
**Reference:** [MDN - font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)


## Medium (30%)

### 11. What is the difference between `display: none` and `visibility: hidden`?
**Answer:** `display: none` removes the element completely from the document layout (it takes up no space). `visibility: hidden` hides the element, but it still takes up the same space in the layout.
**Example:** `.hidden-item { display: none; }`
**Reference:** [MDN - display vs visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)

### 12. Explain CSS Specificity.
**Answer:** Specificity determines which CSS rule is applied by the browsers. It is calculated based on the types of selectors used (Inline style > IDs > Classes/Attributes/Pseudo-classes > Elements/Pseudo-elements).
**Example:** `#id` overrides `.class`.
**Reference:** [MDN - Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

### 13. What is `box-sizing: border-box`?
**Answer:** By default, width and height calculate the content box only. `box-sizing: border-box` tells the browser to account for padding and border in the element's total width and height.
**Example:** `div { width: 100px; padding: 20px; box-sizing: border-box; } /* Total width is 100px */`
**Reference:** [MDN - box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing)

### 14. What are Pseudo-classes?
**Answer:** A pseudo-class is used to define a special state of an element (e.g., when a user hovers over it, or if it's the first child).
**Example:** `a:hover { color: red; }`
**Reference:** [MDN - Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

### 15. What are Pseudo-elements?
**Answer:** A pseudo-element is used to style specified parts of an element (e.g., styling the first letter, or inserting content before/after an element).
**Example:** `p::before { content: "Read: "; }`
**Reference:** [MDN - Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

### 16. What is the difference between relative, absolute, fixed, and sticky positioning?
**Answer:** 
- `relative`: positioned relative to its normal position.
- `absolute`: positioned relative to its closest positioned ancestor.
- `fixed`: positioned relative to the viewport (screen).
- `sticky`: toggles between relative and fixed based on scroll position.
**Example:** `.header { position: sticky; top: 0; }`
**Reference:** [MDN - position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

### 17. How do you center a div horizontally?
**Answer:** If it's a block element with a defined width, use `margin: 0 auto;`. In flexbox, use `justify-content: center;`.
**Example:** `.box { width: 50%; margin: 0 auto; }`
**Reference:** [MDN - Centering in CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Howto/Center_an_item)

### 18. What are CSS Flexbox and its main use case?
**Answer:** Flexbox is a one-dimensional layout model designed to lay out items in a row or column, and to distribute space dynamically and align items within a container.
**Example:** `.container { display: flex; justify-content: space-between; }`
**Reference:** [MDN - Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)

### 19. Explain the CSS Grid Layout.
**Answer:** CSS Grid Layout is a two-dimensional layout system that lets you arrange content in columns and rows.
**Example:** `.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; }`
**Reference:** [MDN - Grid Layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids)

### 20. What are CSS Variables (Custom Properties)?
**Answer:** Variables defined by CSS authors that contain specific values to be reused throughout a document. They are declared with `--` and accessed with `var()`.
**Example:** `:root { --primary-color: #3498db; } h1 { color: var(--primary-color); }`
**Reference:** [MDN - Custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)


## Hard (50%)

### 21. What is the stacking context and `z-index`?
**Answer:** `z-index` controls the vertical stacking order of elements that overlap. However, `z-index` only works inside a stacking context (created by positioning elements, opacity < 1, flex/grid children, transform, etc.). An element in a lower stacking context can never appear above an element in a higher stacking context, regardless of `z-index`.
**Example:** `.modal { position: absolute; z-index: 1000; }`
**Reference:** [MDN - The stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Understanding_z-index/Stacking_context)

### 22. Explain BEM architecture.
**Answer:** BEM (Block, Element, Modifier) is a methodology that helps you to create reusable components and code sharing in front-end development. It keeps CSS specificity flat and naming predictable.
**Example:** `.card {}` (Block), `.card__title {}` (Element), `.card--dark {}` (Modifier).
**Reference:** [CSS Tricks - BEM](https://css-tricks.com/bem-101/)

### 23. What are CSS animations and keyframes?
**Answer:** Animations make it possible to animate transitions from one CSS style configuration to another. `@keyframes` specify the animation code (the start, intermediate, and end states).
**Example:** `@keyframes slide { from { transform: translateX(0); } to { transform: translateX(100px); } } .box { animation: slide 2s ease-in-out; }`
**Reference:** [MDN - CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)

### 24. What is the difference between `transition` and `animation`?
**Answer:** `transition` requires a trigger (like `:hover` or class change) and moves from a start state to an end state. `animation` does not require a trigger, can loop indefinitely, and can have multiple complex keyframes.
**Example:** `button { transition: background-color 0.3s; }` vs `spinner { animation: spin 1s infinite linear; }`
**Reference:** [MDN - CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions/Using_CSS_transitions)

### 25. What is CSS cascading and how does `!important` affect it?
**Answer:** Cascading is the algorithm that defines how to combine property values originating from different sources. `!important` breaks the natural cascade by giving a rule the highest specificity, overriding inline styles and standard specificities.
**Example:** `p { color: red !important; }`
**Reference:** [MDN - Cascade and inheritance](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

### 26. How do media queries work for Responsive Web Design?
**Answer:** Media queries allow you to apply CSS only when specific conditions are true, such as screen width, resolution, or device orientation. This is the core of responsive design.
**Example:** `@media (max-width: 768px) { .sidebar { display: none; } }`
**Reference:** [MDN - Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries)

### 27. Explain Mobile-First vs Desktop-First CSS approaches.
**Answer:** Mobile-first means styling for the smallest screens initially, then using `min-width` media queries to add complexity for larger screens. Desktop-first styles for large screens initially, using `max-width` media queries to strip down the design for smaller devices.
**Example:** Mobile-first: `@media (min-width: 1024px) { ... }`
**Reference:** [MDN - Mobile First](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

### 28. What are calc(), min(), max(), and clamp() in CSS?
**Answer:** These are CSS math functions. `calc()` performs calculations. `min()` selects the smallest value. `max()` selects the largest. `clamp(min, preferred, max)` restricts a value between a lower and upper bound.
**Example:** `width: clamp(200px, 50vw, 600px);`
**Reference:** [MDN - CSS Math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Functions)

### 29. What is a block formatting context (BFC)?
**Answer:** A BFC is a part of a visual CSS rendering of a web page. It is the region in which the layout of block boxes occurs and in which floats interact with other elements. BFCs prevent margin collapsing and contain floated elements.
**Example:** Created using `overflow: hidden;`, `display: flex;`, or `display: flow-root;`.
**Reference:** [MDN - BFC](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Block_formatting_context)

### 30. How do you implement hardware acceleration in CSS?
**Answer:** By using properties that can be handed off to the GPU for rendering (compositing). Properties like `transform` (e.g., `translate3d(0,0,0)`), `opacity`, and `filter` trigger hardware acceleration, leading to smoother animations.
**Example:** `.animate { transform: translateZ(0); }`
**Reference:** [Web.dev - CSS Animations and Performance](https://web.dev/animations-guide/)
