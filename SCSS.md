# SCSS/Sass Interview Questions

This document contains a comprehensive list of SCSS (Sassy CSS) interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is Sass and what is SCSS?
**Answer:** Sass (Syntactically Awesome Style Sheets) is a CSS preprocessor. SCSS (Sassy CSS) is the newer, most common syntax for Sass. SCSS is a superset of CSS, meaning any valid CSS is valid SCSS.
**Example:** Standard CSS brackets `{}` and semicolons `;` are used in SCSS, unlike the older indented Sass syntax.
**Reference:** [Sass Basics](https://sass-lang.com/guide)

### 2. How do you define a variable in SCSS?
**Answer:** Variables in SCSS are defined using the `$` symbol.
**Example:** `$primary-color: #3bbfce; .box { color: $primary-color; }`
**Reference:** [Sass - Variables](https://sass-lang.com/documentation/variables)

### 3. What is nesting in SCSS?
**Answer:** Nesting allows you to write CSS rules inside of other CSS rules, matching the visual hierarchy of your HTML.
**Example:** `nav { ul { margin: 0; } }` compiles to `nav ul { margin: 0; }`
**Reference:** [Sass - Nesting](https://sass-lang.com/documentation/style-rules/declarations#nesting)

### 4. What is the `&` (ampersand) used for in SCSS?
**Answer:** The `&` symbol references the parent selector within a nested block. It's heavily used for pseudo-classes (like `:hover`) and BEM-style naming.
**Example:** `a { color: blue; &:hover { color: red; } }`
**Reference:** [Sass - Parent Selector](https://sass-lang.com/documentation/style-rules/parent-selector)

### 5. How do you write comments in SCSS?
**Answer:** SCSS supports both single-line comments `//` (which are removed in the compiled CSS) and multi-line comments `/* */` (which are preserved in the compiled CSS).
**Example:** `// This comment won't be in CSS`
**Reference:** [Sass - Comments](https://sass-lang.com/documentation/syntax/comments)


## Medium (30%)

### 6. What is an `@mixin` and how do you use it?
**Answer:** A mixin lets you make groups of CSS declarations that you want to reuse throughout your site. You define it with `@mixin` and include it with `@include`.
**Example:** `@mixin border-radius($radius) { -webkit-border-radius: $radius; border-radius: $radius; } .box { @include border-radius(10px); }`
**Reference:** [Sass - Mixins](https://sass-lang.com/documentation/at-rules/mixin)

### 7. What is `@extend` and how is it different from `@mixin`?
**Answer:** `@extend` lets you share a set of CSS properties from one selector to another. While `@mixin` copies the properties into the current selector, `@extend` groups the selectors together in the compiled CSS, resulting in less code.
**Example:** `.message { border: 1px solid #ccc; } .success { @extend .message; border-color: green; }`
**Reference:** [Sass - Extend](https://sass-lang.com/documentation/at-rules/extend)

### 8. What is a placeholder selector (`%`)?
**Answer:** A placeholder selector is a special type of selector that behaves like a class but is not output in the compiled CSS on its own. It is strictly meant to be `@extend`ed.
**Example:** `%btn-base { display: inline-block; } .btn-primary { @extend %btn-base; }`
**Reference:** [Sass - Placeholder Selectors](https://sass-lang.com/documentation/style-rules/placeholder-selectors)

### 9. What does the `@import` directive do in SCSS?
**Answer:** `@import` allows you to split your SCSS into multiple smaller files and include them into a main file. Sass combines them into a single CSS file at compile time, reducing HTTP requests. Note: The Sass team is transitioning from `@import` to `@use`.
**Example:** `@import 'reset';`
**Reference:** [Sass - Import](https://sass-lang.com/documentation/at-rules/import)

### 10. Explain the new `@use` directive.
**Answer:** `@use` is the modern replacement for `@import`. It loads mixins, functions, and variables from other stylesheets, and combines CSS from multiple stylesheets together, but groups them in namespaces to prevent clashes.
**Example:** `@use 'colors'; .box { color: colors.$primary; }`
**Reference:** [Sass - Use](https://sass-lang.com/documentation/at-rules/use)


## Hard (50%)

### 11. What is interpolation (`#{}`) in SCSS?
**Answer:** Interpolation allows you to use variables inside selectors, property names, strings, and other places where a variable normally couldn't be evaluated.
**Example:** `$name: foo; $attr: border; p.#{$name} { #{$attr}-color: blue; }`
**Reference:** [Sass - Interpolation](https://sass-lang.com/documentation/interpolation)

### 12. How do you create loops in SCSS?
**Answer:** SCSS provides `@for`, `@each`, and `@while` directives to iterate over items or numbers to generate CSS.
**Example:** `@for $i from 1 through 3 { .col-#{$i} { width: 10% * $i; } }`
**Reference:** [Sass - Control Directives](https://sass-lang.com/documentation/at-rules/control/for)

### 13. How do conditionals (`@if`, `@else`) work in SCSS?
**Answer:** The `@if` directive takes a SassScript expression and uses the styles nested beneath it if the expression evaluates to true. It can be followed by `@else if` and `@else`.
**Example:** `@mixin theme-colors($light-theme: true) { @if $light-theme { color: black; } @else { color: white; } }`
**Reference:** [Sass - If](https://sass-lang.com/documentation/at-rules/control/if)

### 14. What are SCSS built-in modules?
**Answer:** Modern Sass comes with built-in modules that provide useful functions. Examples include `sass:color` (for `darken()`, `lighten()`), `sass:math` (for `round()`, `percentage()`), and `sass:map`.
**Example:** `@use "sass:color"; .button { background: color.scale($base, $lightness: -20%); }`
**Reference:** [Sass - Built-In Modules](https://sass-lang.com/documentation/modules)

### 15. What are Maps in SCSS?
**Answer:** Maps in Sass hold pairs of keys and values, and make it easy to look up a value by its corresponding key. They are written with parentheses and comma-separated pairs.
**Example:** `$colors: ("primary": red, "secondary": blue); .box { color: map-get($colors, "primary"); }`
**Reference:** [Sass - Maps](https://sass-lang.com/documentation/values/maps)

### 16. What is a `@function` and how is it different from a `@mixin`?
**Answer:** A `@function` is used to compute and return a single value. A `@mixin` is used to output blocks of CSS declarations.
**Example:** `@function half($val) { @return $val / 2; } .box { width: half(100px); }`
**Reference:** [Sass - Functions](https://sass-lang.com/documentation/at-rules/function)

### 17. How does the `!default` flag work?
**Answer:** The `!default` flag assigns a value to a variable *only* if that variable isn't already assigned a value. This is extremely useful for writing libraries (like Bootstrap) so users can override defaults easily.
**Example:** `$primary: blue !default;` (If `$primary` was defined earlier, it stays that color. Otherwise, it becomes blue).
**Reference:** [Sass - Default Values](https://sass-lang.com/documentation/variables#default-values)

### 18. What is the `@forward` rule?
**Answer:** The `@forward` rule loads a Sass stylesheet and makes its mixins, functions, and variables available when your stylesheet is loaded with `@use`. It's used to organize libraries across multiple files but present a single entry point.
**Example:** `@forward "variables"; @forward "mixins";` in `_index.scss`.
**Reference:** [Sass - Forward](https://sass-lang.com/documentation/at-rules/forward)

### 19. How do you handle responsive typography using SCSS maps and loops?
**Answer:** You can define a map of breakpoints and font sizes, then iterate over them using `@each` to generate media queries automatically.
**Example:** 
```scss
$sizes: (small: 12px, large: 16px);
@each $bp, $size in $sizes {
  @media (min-width: map-get($breakpoints, $bp)) { body { font-size: $size; } }
}
```
**Reference:** [Sass - Each](https://sass-lang.com/documentation/at-rules/control/each)

### 20. What is Dart Sass?
**Answer:** Dart Sass is the primary implementation of Sass, replacing Ruby Sass and LibSass (Node Sass). It is faster, easier to install, and compiles to pure JS or runs directly on the Dart VM.
**Example:** `npm install -g sass` installs Dart Sass.
**Reference:** [Sass - Dart Sass](https://sass-lang.com/dart-sass)
