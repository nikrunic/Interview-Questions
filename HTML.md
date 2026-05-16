# HTML Interview Questions

This document contains a comprehensive list of 100 HTML interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories and front-end interview handbooks.

## Basic (20 Questions)

### 1. What does HTML stand for?
**Answer:** HyperText Markup Language.
**Example:** `<!DOCTYPE html><html>...</html>`
**Reference:** [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

### 2. What are HTML tags?
**Answer:** Keywords surrounded by angle brackets that define how a web browser must format and display the content.
**Example:** `<p>Paragraph</p>`
**Reference:** [MDN Element](https://developer.mozilla.org/en-US/docs/Glossary/Element)

### 3. What is an HTML attribute?
**Answer:** Modifiers of HTML elements that provide additional information.
**Example:** `<img src="image.jpg">` (`src` is the attribute).
**Reference:** [MDN Attribute](https://developer.mozilla.org/en-US/docs/Glossary/Attribute)

### 4. What is the `<!DOCTYPE html>` declaration?
**Answer:** 
**The Core Concept:**
It tells the browser what version of HTML the page is written in.

**Key Details:**
- `<!DOCTYPE html>` specifies HTML5.
**Example:** At the very top of an HTML document.
**Reference:** [MDN Doctype](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)

### 5. What is the difference between an element and a tag?
**Answer:** An element is the entire object (start tag, content, end tag), whereas tags are just the markers (`<p>` and `</p>`).
**Example:** `<p>Text</p>` is an element.
**Reference:** [MDN Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

### 6. What is Semantic HTML?
**Answer:** Using HTML markup to reinforce the meaning of the information, rather than just defining its appearance.
**Example:** Using `<article>` instead of `<div class="article">`.
**Reference:** [MDN Semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)

### 7. What is the difference between inline and block-level elements?
**Answer:** 
**The Core Concept:**
Block elements start on a new line and take full width.

**Key Details:**
- Inline elements don't start on a new line and only take necessary width.
**Example:** Block: `<div>`. Inline: `<span>`.
**Reference:** [MDN Block-level elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)

### 8. How do you create a hyperlink?
**Answer:** Using the `<a>` (anchor) tag and the `href` attribute.
**Example:** `<a href="https://example.com">Link</a>`
**Reference:** [MDN a tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)

### 9. What is the `alt` attribute for images?
**Answer:** Specifies alternate text for an image if it cannot be displayed, crucial for screen readers and SEO.
**Example:** `<img src="logo.png" alt="Company Logo">`
**Reference:** [MDN img alt](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt)

### 10. How do you insert a comment in HTML?
**Answer:** By wrapping text in `<!--` and `-->`.
**Example:** `<!-- Note -->`
**Reference:** [MDN Comments](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#html_comments)

### 11. What is a table in HTML?
**Answer:** A structured set of data made of rows and columns using `<table>`, `<tr>`, `<td>`, and `<th>`.
**Example:** `<table><tr><td>Data</td></tr></table>`
**Reference:** [MDN table](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

### 12. What are ordered and unordered lists?
**Answer:** 
**The Core Concept:**
Ordered lists (`<ol>`) are numbered.

**Key Details:**
- Unordered lists (`<ul>`) are bulleted.
- Both contain list items (`<li>`).
**Example:** `<ul><li>Item</li></ul>`
**Reference:** [MDN Lists](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#lists)

### 13. What is an iframe?
**Answer:** Used to embed another document within the current HTML document.
**Example:** `<iframe src="page.html"></iframe>`
**Reference:** [MDN iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)

### 14. What is the difference between `head` and `body`?
**Answer:** 
**The Core Concept:**
`<head>` contains metadata, title, and links to scripts/styles.

**Key Details:**
- `<body>` contains the visible content of the page.
**Example:** `<head><title>Doc</title></head><body>Content</body>`
**Reference:** [MDN Document structure](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure)

### 15. How do you make text bold or italic?
**Answer:** 
**The Core Concept:**
Bold: `<strong>` or `<b>`.

**Key Details:**
- Italic: `<em>` or `<i>`.
- `strong` and `em` are preferred for semantic meaning.
**Example:** `<strong>Important</strong>`
**Reference:** [MDN Text formatting](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals)

### 16. What is a form?
**Answer:** A section of a document containing interactive controls for submitting information to a web server.
**Example:** `<form action="/submit"><input></form>`
**Reference:** [MDN form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)

### 17. What are the common input types?
**Answer:** text, password, email, number, checkbox, radio, submit, button.
**Example:** `<input type="email">`
**Reference:** [MDN Input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

### 18. What does `<br>` do?
**Answer:** 
**The Core Concept:**
Inserts a single line break.

**Key Details:**
- It is an empty element (no closing tag).
**Example:** `Line 1<br>Line 2`
**Reference:** [MDN br](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)

### 19. What does `<hr>` do?
**Answer:** Represents a thematic break, typically rendered as a horizontal line.
**Example:** `<p>Topic 1</p><hr><p>Topic 2</p>`
**Reference:** [MDN hr](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)

### 20. How do you link a CSS file?
**Answer:** Using the `<link>` tag in the `<head>`.
**Example:** `<link rel="stylesheet" href="style.css">`
**Reference:** [MDN link](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)


## Medium (30 Questions)

### 21. What are meta tags?
**Answer:** Tags that provide metadata about the HTML document, not displayed on the page but machine-parsable.
**Example:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
**Reference:** [MDN meta](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)

### 22. What is the viewport meta tag?
**Answer:** It gives the browser instructions on how to control the page's dimensions and scaling, essential for mobile design.
**Example:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
**Reference:** [MDN Viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)

### 23. What are data attributes (`data-*`)?
**Answer:** They allow you to store extra information on standard HTML elements without hacks.
**Example:** `<div data-id="123">`
**Reference:** [MDN Data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

### 24. What is the difference between `id` and `class`?
**Answer:** 
**The Core Concept:**
An `id` must be unique on the page and identifies a single element.

**Key Details:**
- A `class` can be reused on multiple elements.
**Example:** `<div id="header" class="dark-theme">`
**Reference:** [MDN id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)

### 25. What is the `action` attribute in a form?
**Answer:** It specifies where to send the form-data when a form is submitted (usually a URL).
**Example:** `<form action="/login">`
**Reference:** [MDN form action](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#action)

### 26. What is the `method` attribute in a form?
**Answer:** It specifies the HTTP method to use when sending data (`GET` or `POST`).
**Example:** `<form method="POST">`
**Reference:** [MDN form method](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method)

### 27. What is `figure` and `figcaption`?
**Answer:** `<figure>` encapsulates media (like images) and `<figcaption>` provides a caption for it, associating them semantically.
**Example:** `<figure><img src="pic.jpg"><figcaption>A picture</figcaption></figure>`
**Reference:** [MDN figure](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)

### 28. What are `audio` and `video` tags?
**Answer:** HTML5 elements used to embed sound and video content natively without plugins like Flash.
**Example:** `<video src="vid.mp4" controls></video>`
**Reference:** [MDN video](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)

### 29. What is the `canvas` element?
**Answer:** Used to draw graphics, on the fly, via scripting (usually JavaScript).
**Example:** `<canvas id="myCanvas"></canvas>`
**Reference:** [MDN canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

### 30. What is SVG?
**Answer:** 
**The Core Concept:**
Scalable Vector Graphics.

**Key Details:**
- Used to define vector-based graphics for the web.
- Unlike raster images, SVGs don't lose quality when zoomed.
**Example:** `<svg><circle r="50"/></svg>`
**Reference:** [MDN SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)

### 31. What is the difference between `<script>`, `<script defer>`, and `<script async>`?
**Answer:** 
**The Core Concept:**
Normal script blocks parsing.

**Key Details:**
- `async` downloads in parallel and executes immediately.
- `defer` downloads in parallel but executes after parsing finishes.
**Example:** `<script src="app.js" defer></script>`
**Reference:** [MDN script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)

### 32. What is the `target` attribute on a link?
**Answer:** 
**The Core Concept:**
Specifies where to open the linked document.

**Key Details:**
- `target="_blank"` opens in a new tab.
**Example:** `<a target="_blank">`
**Reference:** [MDN a target](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#target)

### 33. Why use `rel="noopener noreferrer"` with `target="_blank"`?
**Answer:** For security (`noopener` prevents the new page from accessing `window.opener`) and privacy (`noreferrer` hides referrer info).
**Example:** `<a href="..." target="_blank" rel="noopener noreferrer">`
**Reference:** [MDN rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel)

### 34. What is the `<picture>` tag?
**Answer:** Gives developers flexibility in specifying multiple image resources depending on viewport size or format support.
**Example:** `<picture><source srcset="large.jpg" media="(min-width: 800px)"><img src="small.jpg"></picture>`
**Reference:** [MDN picture](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)

### 35. What is the `srcset` attribute?
**Answer:** Used on `<img>` or `<source>` to specify different image files for different screen resolutions (like Retina displays).
**Example:** `<img srcset="img-1x.jpg 1x, img-2x.jpg 2x">`
**Reference:** [MDN srcset](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

### 36. What is the purpose of `<datalist>`?
**Answer:** Specifies a list of pre-defined options for an `<input>` element, creating a searchable dropdown.
**Example:** `<input list="browsers"><datalist id="browsers"><option value="Chrome"></datalist>`
**Reference:** [MDN datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)

### 37. What is the `required` attribute?
**Answer:** A boolean attribute that specifies that an input field must be filled out before submitting the form.
**Example:** `<input type="text" required>`
**Reference:** [MDN required](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required)

### 38. What is `tabindex`?
**Answer:** An attribute that indicates if an element can be focused, and if so, specifies the order in which it receives focus during keyboard navigation.
**Example:** `<div tabindex="0">`
**Reference:** [MDN tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex)

### 39. Explain the `<label>` element.
**Answer:** 
**The Core Concept:**
Represents a caption for an item in a user interface.

**Key Details:**
- Clicking it focuses the associated input.
**Example:** `<label for="email">Email</label><input id="email">`
**Reference:** [MDN label](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)

### 40. What is `aria-label`?
**Answer:** An ARIA attribute used to define a string that labels the current element for screen readers when there is no visible text.
**Example:** `<button aria-label="Close">X</button>`
**Reference:** [MDN aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)

### 41. What is the `<details>` and `<summary>` element?
**Answer:** Creates a native disclosure widget from which the user can retrieve additional information (an accordion).
**Example:** `<details><summary>More info</summary>Hidden text</details>`
**Reference:** [MDN details](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)

### 42. What is the `<nav>` tag?
**Answer:** A semantic tag representing a section of a page whose purpose is to provide navigation links.
**Example:** `<nav><ul><li>Link</li></ul></nav>`
**Reference:** [MDN nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)

### 43. What is the `<main>` tag?
**Answer:** 
**The Core Concept:**
A semantic tag representing the dominant content of the `<body>`.

**Key Details:**
- There should be only one visible `<main>` per page.
**Example:** `<main><h1>Title</h1>...</main>`
**Reference:** [MDN main](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)

### 44. What are `header` and `footer`?
**Answer:** Semantic tags for introductory content (header) and closing content (footer) for a document or a section.
**Example:** `<footer>Copyright 2023</footer>`
**Reference:** [MDN footer](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)

### 45. What is the difference between `section` and `article`?
**Answer:** 
**The Core Concept:**
`<article>` is for standalone, distributable content (like a blog post).

**Key Details:**
- `<section>` is for a thematic grouping of content, typically with a heading.
**Example:** `<article>Blog post content</article>`
**Reference:** [MDN article](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)

### 46. What does `<base>` tag do?
**Answer:** Specifies the base URL and/or target for all relative URLs in a document.
**Example:** `<base href="https://example.com/dir/">`
**Reference:** [MDN base](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)

### 47. How do you create a disabled input?
**Answer:** 
**The Core Concept:**
Use the `disabled` attribute.

**Key Details:**
- The input cannot be interacted with and its value won't be submitted.
**Example:** `<input type="text" disabled>`
**Reference:** [MDN disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled)

### 48. What is the difference between `readonly` and `disabled`?
**Answer:** 
**The Core Concept:**
`readonly` inputs cannot be edited but can be focused and *will* be submitted.

**Key Details:**
- `disabled` inputs cannot be focused and *will not* be submitted.
**Example:** `<input readonly>`
**Reference:** [MDN readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/readonly)

### 49. What is a hidden field?
**Answer:** An input of type `hidden` lets web developers include data that cannot be seen or modified by users when a form is submitted.
**Example:** `<input type="hidden" name="token" value="abc">`
**Reference:** [MDN input hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/hidden)

### 50. What is a favicon?
**Answer:** A small icon associated with a website, displayed in the browser tab.
**Example:** `<link rel="icon" href="favicon.ico">`
**Reference:** [MDN Favicon](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)


## Hard (50 Questions)

### 51. Explain the HTML parsing process.
**Answer:** 
**The Core Concept:**
Bytes -> Characters -> Tokens (Tokenization) -> Nodes -> DOM Tree.

**Key Details:**
- HTML parser builds the DOM and handles errors gracefully.
**Example:** `<b>text</i>` is autocorrected in the DOM.
**Reference:** [MDN Parsing](https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work#parsing)

### 52. What is the Shadow DOM?
**Answer:** A web standard that encapsulates a component's DOM and CSS styling, keeping them hidden and separate from the rest of the document.
**Example:** Used heavily in Web Components.
**Reference:** [MDN Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM)

### 53. What are Web Components?
**Answer:** A suite of different technologies (Custom Elements, Shadow DOM, HTML Templates) allowing the creation of reusable custom elements.
**Example:** `<my-custom-element></my-custom-element>`
**Reference:** [MDN Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)

### 54. What is the `<template>` tag?
**Answer:** A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.
**Example:** `<template id="my-tmpl"><p>Hidden</p></template>`
**Reference:** [MDN template](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)

### 55. What is the `<slot>` tag?
**Answer:** A placeholder inside a web component (Shadow DOM) that you can fill with your own markup, which lets you create separate DOM trees and present them together.
**Example:** `<slot name="header"></slot>`
**Reference:** [MDN slot](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)

### 56. What are HTML5 Server-Sent Events (SSE)?
**Answer:** A standard describing how servers can initiate data transmission towards clients once an initial client connection has been established (unidirectional).
**Example:** EventSource API in JS relies on SSE.
**Reference:** [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

### 57. What are the Accessibility Tree and ARIA?
**Answer:** 
**The Core Concept:**
The accessibility tree is derived from the DOM and used by screen readers.

**Key Details:**
- ARIA (Accessible Rich Internet Applications) attributes modify this tree to provide semantics for complex widgets.
**Example:** `role="progressbar"`
**Reference:** [MDN Accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree)

### 58. Explain `aria-hidden="true"`.
**Answer:** Hides an element and its descendants from assistive technologies (like screen readers), but the element remains visible visually.
**Example:** `<i class="icon" aria-hidden="true"></i>`
**Reference:** [MDN aria-hidden](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-hidden)

### 59. Explain `role="presentation"`.
**Answer:** 
**The Core Concept:**
Removes the semantic meaning of an element from the accessibility tree.

**Key Details:**
- For example, making a `<table>` used for layout be ignored as a data table.
**Example:** `<table role="presentation">`
**Reference:** [MDN role presentation](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/presentation_role)

### 60. How do you implement resource preloading in HTML?
**Answer:** Using `<link rel="preload">` to tell the browser to download a critical resource early before it's discovered in the HTML parse.
**Example:** `<link rel="preload" href="font.woff2" as="font">`
**Reference:** [MDN Preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload)

### 61. What is the difference between `preload`, `prefetch`, and `preconnect`?
**Answer:** 
**The Core Concept:**
`preload`: fetch early for *this* page.

**Key Details:**
- `prefetch`: fetch idle for a *future* page.
- `preconnect`: establish early network connection (DNS/TCP/TLS) to an origin.
**Example:** `<link rel="preconnect" href="https://api.example.com">`
**Reference:** [Web.dev Resource Hints](https://web.dev/preconnect-and-dns-prefetch/)

### 62. What is Content Security Policy (CSP)?
**Answer:** An added layer of security via HTTP header or `<meta>` tag that mitigates XSS by specifying which dynamic resources are allowed to load.
**Example:** `<meta http-equiv="Content-Security-Policy" content="default-src 'self'">`
**Reference:** [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

### 63. How do you define a manifest file for a PWA?
**Answer:** Using the `<link rel="manifest">` tag pointing to a JSON file containing app metadata (name, icons, display mode).
**Example:** `<link rel="manifest" href="/manifest.json">`
**Reference:** [MDN Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest)

### 64. What is the `translate` attribute?
**Answer:** Specifies whether the content of an element should be translated by browsers/translation tools.
**Example:** `<span translate="no">BrandName</span>`
**Reference:** [MDN translate](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate)

### 65. What is the `contenteditable` attribute?
**Answer:** 
**The Core Concept:**
A global attribute indicating if the element should be editable by the user.

**Key Details:**
- Used to build rich text editors.
**Example:** `<div contenteditable="true">Edit me</div>`
**Reference:** [MDN contenteditable](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/contenteditable)

### 66. How does the browser determine Document Mode (Quirks vs Standard)?
**Answer:** 
**The Core Concept:**
Based on the presence and format of the `<!DOCTYPE>`.

**Key Details:**
- Without a proper DOCTYPE, browsers render in Quirks mode (emulating IE5 bugs).
**Example:** Omit DOCTYPE -> Quirks Mode.
**Reference:** [MDN Quirks Mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Quirks_Mode_and_Standards_Mode)

### 67. Explain HTML form encoding types (`enctype`).
**Answer:** 
**The Core Concept:**
`application/x-www-form-urlencoded` (default, keys/values URL encoded).

**Key Details:**
- `multipart/form-data` (required for file uploads).
- `text/plain` (rarely used, raw text).
**Example:** `<form enctype="multipart/form-data">`
**Reference:** [MDN enctype](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype)

### 68. What are Custom Elements?
**Answer:** 
**The Core Concept:**
Part of Web Components.

**Key Details:**
- They allow developers to define their own HTML tags and their associated behavior via JavaScript classes extending `HTMLElement`.
**Example:** `customElements.define('word-count', WordCount);`
**Reference:** [MDN Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)

### 69. How does `autocomplete` work on forms?
**Answer:** 
**The Core Concept:**
It tells the browser whether to autofill fields based on previously entered data.

**Key Details:**
- Using specific tokens like `cc-name` helps browsers fill specific data (credit cards).
**Example:** `<input type="text" autocomplete="cc-name">`
**Reference:** [MDN autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

### 70. What is Microdata?
**Answer:** A specification used to nest metadata within existing content on web pages to provide structured data for search engines (like Schema.org).
**Example:** `<div itemscope itemtype="http://schema.org/Person">`
**Reference:** [MDN Microdata](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata)

### 71. Why has strict adherence to Semantic HTML become increasingly critical in modern web development?
**Answer:** 
**The Core Concept:**
While visual styling can be handled by CSS, Semantic HTML (`<header>`, `<main>`, `<article>`, etc.) is heavily relied upon by search engines (SEO), accessibility tools (screen readers), AI crawlers, and modern frameworks (like React Server Components) to automatically parse and understand content.

**Key Details:**
- Poor semantics now carry much heavier penalties.
**Example:** Using `<nav>` instead of `<div class="navigation">`.
**Reference:** [MDN Semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)

### 72. How does the native `<dialog>` API improve accessibility and architecture over custom JS modals?
**Answer:** 
**The Core Concept:**
The native `<dialog>` element provides built-in accessibility, focus-trapping, keyboard navigation (Escape to close), and proper layering in the browser's top layer.

**Key Details:**
- This completely eliminates the need for massive third-party modal libraries and complex `z-index` management.
**Example:** `<dialog id="myModal">Hello</dialog>` opened via `document.getElementById('myModal').showModal();`
**Reference:** [MDN dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)

### 73. What is the Popover API and how does it simplify UI development?
**Answer:** 
**The Core Concept:**
The Popover API provides native browser management for tooltips, dropdowns, and flyouts.

**Key Details:**
- It automatically handles positioning, light dismiss (clicking outside to close), and keyboard accessibility without needing heavy JavaScript positioning engines or complex event listeners.
**Example:** `<button popovertarget="menu">Menu</button> <div id="menu" popover>Content</div>`
**Reference:** [MDN Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)

### 74. How does the View Transitions API improve UX without heavy JavaScript libraries?
**Answer:** The View Transitions API enables native, smooth visual transitions between different DOM states or pages (SPA-like navigation) directly within the browser engine, eliminating the need for complex, heavy JS animation libraries to cross-fade UI states.
**Example:** `document.startViewTransition(() => updateDOM());`
**Reference:** [MDN View Transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API)

### 75. Explain the Critical Rendering Path (CRP).
**Answer:** 
**The Core Concept:**
The sequence of steps the browser goes through to convert HTML, CSS, and JS into pixels on the screen.

**Key Details:**
- It involves building the DOM, building the CSSOM, combining them into the Render Tree, calculating Layout, and finally Painting.
**Example:** Optimizing CRP by minifying CSS and deferring non-critical JS.
**Reference:** [MDN CRP](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)

### 76. What is the DOM (Document Object Model)?
**Answer:** 
**The Core Concept:**
An object-oriented representation of the web page, which can be modified with a scripting language such as JavaScript.

**Key Details:**
- It represents the document as nodes and objects.
**Example:** `document.getElementById('app')` interacts with the DOM.
**Reference:** [MDN DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

### 77. How does the browser handle the `<!DOCTYPE html>` declaration?
**Answer:** 
**The Core Concept:**
The doctype declaration tells the browser which version of HTML the document is written in.

**Key Details:**
- `<!DOCTYPE html>` triggers HTML5 standard mode.
- Without it, the browser falls into Quirks mode, mimicking older browsers' bugs for backwards compatibility.
**Example:** Always place `<!DOCTYPE html>` at the very top of the file.
**Reference:** [MDN Doctype](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)

### 78. What are `data-*` attributes and when should they be used?
**Answer:** 
**The Core Concept:**
They allow you to store extra, custom information on standard, semantic HTML elements without resorting to non-standard attributes or extra DOM properties.

**Key Details:**
- Accessible via JavaScript `dataset`.
**Example:** `<article data-author-id="123">`
**Reference:** [MDN Data Attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

### 79. Explain the use of the `<colgroup>` element.
**Answer:** Used within a `<table>` to specify common styles for an entire column or group of columns, preventing the need to repeat styling on every `<td>` within that column.
**Example:** `<colgroup><col style="background-color: red;"></colgroup>`
**Reference:** [MDN colgroup](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)

### 80. What is the `scope` attribute in tables?
**Answer:** 
**The Core Concept:**
Used on `<th>` elements to define whether the header cell relates to a row, column, rowgroup, or colgroup.

**Key Details:**
- It is essential for screen readers to interpret complex tabular data correctly.
**Example:** `<th scope="col">Name</th>`
**Reference:** [MDN scope attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#scope)

### 81. How does the HTML5 native validation API work?
**Answer:** 
**The Core Concept:**
HTML5 introduced attributes like `required`, `pattern`, `min`, `max`, and specific `type`s (like email).

**Key Details:**
- The browser handles validation automatically before form submission, and exposes the `ValidityState` API to JavaScript for custom validation messaging.
**Example:** `<input type="email" required pattern=".*@example\.com">`
**Reference:** [MDN Form Validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

### 82. What is the difference between `<meter>` and `<progress>`?
**Answer:** 
**The Core Concept:**
`<progress>` represents the completion progress of a task (like a download).

**Key Details:**
- `<meter>` represents a scalar measurement within a known range, or a fractional value (like disk usage or a gauge).
**Example:** `<progress value="70" max="100">` vs `<meter value="0.6">`
**Reference:** [MDN meter](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)

### 83. Explain the `<time>` element and its `datetime` attribute.
**Answer:** 
**The Core Concept:**
Represents a specific period in time.

**Key Details:**
- The `datetime` attribute allows you to format the time in a machine-readable format while displaying a human-readable format, improving SEO and calendar integrations.
**Example:** `<time datetime="2023-01-01">New Year's Day</time>`
**Reference:** [MDN time](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)

### 84. What is `<noscript>` used for?
**Answer:** Defines an alternate content section to be displayed to users that have disabled scripts in their browser or have a browser that doesn't support scripts.
**Example:** `<noscript>Please enable JavaScript to use this site.</noscript>`
**Reference:** [MDN noscript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)

### 85. What are the SEO implications of heading hierarchy (`<h1>` to `<h6>`)?
**Answer:** 
**The Core Concept:**
Search engines use heading tags to understand the structure and context of the content.

**Key Details:**
- A logical hierarchy (one `<h1>` per page, followed by `<h2>`, `<h3>` etc.
- without skipping levels) drastically improves indexability and accessibility.
**Example:** `<h1>Title</h1> <h2>Subtitle</h2>`
**Reference:** [MDN Headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)

### 86. How do you embed an SVG directly into HTML?
**Answer:** 
**The Core Concept:**
You can write the `<svg>` tag directly into the HTML document.

**Key Details:**
- Inline SVGs do not require an extra HTTP request, can be styled with CSS (e.g., changing `fill`), and animated with JavaScript.
**Example:** `<svg width="100"><circle cx="50" cy="50" r="40" fill="red" /></svg>`
**Reference:** [MDN SVG in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web)

### 87. What is the `<output>` element?
**Answer:** Represents the result of a calculation or user action, typically associated with a `<form>` and dynamically updated via JavaScript.
**Example:** `<output name="result" for="a b"></output>`
**Reference:** [MDN output](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)

### 88. Explain the `ping` attribute on anchors.
**Answer:** 
**The Core Concept:**
A space-separated list of URLs to which the browser will send `POST` requests in the background when the user clicks the hyperlink.

**Key Details:**
- Often used for analytics tracking without JavaScript redirects.
**Example:** `<a href="page.html" ping="tracker.php">Link</a>`
**Reference:** [MDN ping attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#ping)

### 89. What is a "Skip to Content" link?
**Answer:** An accessibility best practice where the very first focusable element on the page is an anchor link that jumps over repetitive navigation menus directly to the `<main>` content, aiding keyboard users.
**Example:** `<a href="#main" class="sr-only focus:not-sr-only">Skip to content</a>`
**Reference:** [WebAim Skip Navigation](https://webaim.org/techniques/skipnav/)

### 90. Explain the `role="alert"` ARIA attribute.
**Answer:** Used to communicate an important, time-sensitive message to the user visually and via screen readers (creates a live region that interrupts the screen reader).
**Example:** `<div role="alert">Your session has expired.</div>`
**Reference:** [MDN role="alert"](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/alert_role)

### 91. What is the `<kbd>` element?
**Answer:** Represents inline text denoting user input from a keyboard, voice input, or any other text entry device.
**Example:** `Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.`
**Reference:** [MDN kbd](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)

### 92. What is the `translate` attribute?
**Answer:** Specifies whether the content of an element should be translated when the page is localized (e.g., using Google Translate).
**Example:** `<span translate="no">BrandName</span>`
**Reference:** [MDN translate](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/translate)

### 93. Explain the `<bdi>` element.
**Answer:** 
**The Core Concept:**
Bidirectional Isolation.

**Key Details:**
- It isolates a span of text that might be formatted in a different direction (RTL vs LTR) from other text outside it, preventing layout scrambling in mixed-language content.
**Example:** `<bdi>مستخدم</bdi>: 3 posts`
**Reference:** [MDN bdi](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)

### 94. What is the `<ruby>` element?
**Answer:** Used to provide pronunciation, translation, or transliteration annotations alongside base text (common in East Asian typography).
**Example:** `<ruby>漢<rt>kan</rt>字<rt>ji</rt></ruby>`
**Reference:** [MDN ruby](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)

### 95. What are the `defer` and `async` script attributes?
**Answer:** 
**The Core Concept:**
Both download scripts without blocking HTML parsing.

**Key Details:**
- `async` executes immediately after download (breaking execution order).
- `defer` executes in order right before the `DOMContentLoaded` event.
**Example:** `<script src="analytics.js" async></script>`
**Reference:** [MDN Script attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)

### 96. What is the `download` attribute on an anchor tag?
**Answer:** Instructs the browser to download a URL instead of navigating to it, prompting the user to save it as a local file.
**Example:** `<a href="file.pdf" download="report.pdf">Download</a>`
**Reference:** [MDN anchor download](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#download)

### 97. Explain the `<wbr>` element.
**Answer:** 
**The Core Concept:**
Word Break Opportunity.

**Key Details:**
- It specifies where in a text it would be ok to add a line-break, useful for extremely long URLs or strings without spaces to prevent layout overflow.
**Example:** `https://www.example<wbr>.com/very<wbr>long<wbr>url`
**Reference:** [MDN wbr](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)

### 98. What is the purpose of the `<object>` element?
**Answer:** Used to embed external resources like PDFs, Flash (historically), or even other HTML documents inside the current document.
**Example:** `<object data="file.pdf" type="application/pdf"></object>`
**Reference:** [MDN object](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)

### 99. How does `loading="lazy"` work on images?
**Answer:** 
**The Core Concept:**
Instructs the browser to defer loading of the image until it reaches a calculated distance from the viewport.

**Key Details:**
- This significantly saves bandwidth and speeds up the initial page load.
**Example:** `<img src="heavy.jpg" loading="lazy">`
**Reference:** [MDN Lazy Loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading)

### 100. What is an iframe sandbox?
**Answer:** The `sandbox` attribute restricts the actions that the embedded iframe content can perform (like executing scripts, submitting forms, or opening popups), heavily improving security against malicious third-party embeds.
**Example:** `<iframe sandbox="allow-scripts" src="..."></iframe>`
**Reference:** [MDN iframe sandbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#sandbox)
