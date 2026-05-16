# HTML Interview Questions

This document contains a comprehensive list of HTML interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is HTML?
**Answer:** HTML stands for HyperText Markup Language. It is the standard markup language used to create and design documents on the World Wide Web.
**Example:** `<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>`
**Reference:** [MDN Web Docs - HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)

### 2. What are HTML tags?
**Answer:** HTML tags are keywords surrounded by angle brackets (e.g., `<html>`) that define how a web browser must format and display the content.
**Example:** `<p>This is a paragraph tag.</p>`
**Reference:** [MDN Web Docs - HTML tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

### 3. What is an HTML element?
**Answer:** An HTML element consists of a start tag, content, and an end tag. It represents a single part of a web page.
**Example:** `<h1>This is an element</h1>`
**Reference:** [MDN Web Docs - Elements](https://developer.mozilla.org/en-US/docs/Glossary/Element)

### 4. What is the purpose of the `<!DOCTYPE html>` declaration?
**Answer:** It is an instruction to the web browser about what version of HTML the page is written in. `<!DOCTYPE html>` specifies HTML5.
**Example:** `<!DOCTYPE html>` at the very top of an HTML document.
**Reference:** [MDN Web Docs - Doctype](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)

### 5. What is the difference between `<head>` and `<body>` tags?
**Answer:** The `<head>` element contains meta-information about the HTML page (title, links to CSS), while the `<body>` element contains the visible page content (headings, paragraphs, images).
**Example:** `<head><title>Title</title></head><body>Content goes here</body>`
**Reference:** [MDN Web Docs - Document and website structure](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure)

### 6. What are HTML attributes?
**Answer:** Attributes provide additional information about HTML elements. They are always specified in the start tag and usually come in name/value pairs like `name="value"`.
**Example:** `<a href="https://www.example.com">Visit Example</a>` (Here, `href` is the attribute).
**Reference:** [MDN Web Docs - Attributes](https://developer.mozilla.org/en-US/docs/Glossary/Attribute)

### 7. What is the `alt` attribute in an `<img>` tag used for?
**Answer:** The `alt` attribute specifies alternate text for an image, if the image cannot be displayed. It is crucial for web accessibility (screen readers) and SEO.
**Example:** `<img src="logo.png" alt="Company Logo">`
**Reference:** [MDN Web Docs - alt attribute](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt)

### 8. How do you create a hyperlink in HTML?
**Answer:** You use the `<a>` (anchor) tag with the `href` attribute to specify the destination URL.
**Example:** `<a href="https://www.google.com">Google</a>`
**Reference:** [MDN Web Docs - a tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)

### 9. What is the difference between `<ol>`, `<ul>`, and `<dl>`?
**Answer:** `<ol>` defines an ordered (numbered) list. `<ul>` defines an unordered (bulleted) list. `<dl>` defines a description list, with terms (`<dt>`) and descriptions (`<dd>`).
**Example:** `<ul><li>Item 1</li></ul>`
**Reference:** [MDN Web Docs - Lists](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#lists)

### 10. How do you add a comment in HTML?
**Answer:** You can add comments in HTML by wrapping the text with `<!--` and `-->`. Comments are not displayed in the browser.
**Example:** `<!-- This is a comment -->`
**Reference:** [MDN Web Docs - HTML comments](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#html_comments)

### 11. What is semantic HTML?
**Answer:** Semantic HTML uses HTML markup to reinforce the semantics, or meaning, of the information in web pages rather than merely to define its presentation (look).
**Example:** Using `<article>` instead of `<div class="article">`.
**Reference:** [MDN Web Docs - Semantics](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)

### 12. What is a block-level element?
**Answer:** A block-level element always starts on a new line and takes up the full width available (stretches out to the left and right as far as it can).
**Example:** `<div>`, `<h1>` - `<h6>`, `<p>`.
**Reference:** [MDN Web Docs - Block-level elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)

### 13. What is an inline element?
**Answer:** An inline element does not start on a new line and only takes up as much width as necessary.
**Example:** `<span>`, `<a>`, `<img>`.
**Reference:** [MDN Web Docs - Inline elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements)

### 14. How do you insert an image in HTML?
**Answer:** Using the `<img>` tag, which is an empty tag (no closing tag), with the `src` attribute pointing to the image URL.
**Example:** `<img src="image.jpg" alt="Description">`
**Reference:** [MDN Web Docs - img tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)

### 15. What does the `<br>` tag do?
**Answer:** The `<br>` tag inserts a single line break. It is an empty tag, meaning it does not need a closing tag.
**Example:** `First line.<br>Second line.`
**Reference:** [MDN Web Docs - br tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)

### 16. What is the `<hr>` tag?
**Answer:** The `<hr>` tag defines a thematic break in an HTML page, usually displayed as a horizontal rule (line).
**Example:** `<p>Topic 1</p><hr><p>Topic 2</p>`
**Reference:** [MDN Web Docs - hr tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)

### 17. How do you define a table in HTML?
**Answer:** Using the `<table>` tag. Rows are defined with `<tr>`, headers with `<th>`, and data cells with `<td>`.
**Example:** `<table><tr><th>Name</th></tr><tr><td>John</td></tr></table>`
**Reference:** [MDN Web Docs - table tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

### 18. What is the `target` attribute in links?
**Answer:** The `target` attribute specifies where to open the linked document. Using `_blank` opens the link in a new tab or window.
**Example:** `<a href="url" target="_blank">Link</a>`
**Reference:** [MDN Web Docs - a tag target](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#target)

### 19. How do you create a checkbox in HTML?
**Answer:** Use the `<input>` element with the `type` attribute set to "checkbox".
**Example:** `<input type="checkbox" id="check1" name="check1" value="Bike">`
**Reference:** [MDN Web Docs - Input checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)

### 20. What is the `<form>` element?
**Answer:** The `<form>` element is used to create an HTML form for user input. It contains form elements like text fields, checkboxes, radio buttons, submit buttons, etc.
**Example:** `<form action="/submit_page"><input type="text" name="fname"><input type="submit" value="Submit"></form>`
**Reference:** [MDN Web Docs - form tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)


## Medium (30%)

### 21. What is the difference between `<div>` and `<span>`?
**Answer:** `<div>` is a block-level element used for grouping larger chunks of code, starting on a new line. `<span>` is an inline element used to style or group a small chunk of text without breaking the line.
**Example:** `<div style="color:red">Block of text</div>` vs `<p>This is a <span style="color:red">word</span></p>`.
**Reference:** [MDN Web Docs - div element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)

### 22. What are meta tags?
**Answer:** Meta tags provide metadata about the HTML document. Metadata is not displayed on the page but is machine-parsable. They are used by browsers, search engines, and other web services.
**Example:** `<meta name="description" content="Free Web tutorials">`
**Reference:** [MDN Web Docs - meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)

### 23. What is an iframe in HTML?
**Answer:** An iframe (`<iframe>`) is used to embed another document within the current HTML document.
**Example:** `<iframe src="https://www.example.com" width="500" height="200"></iframe>`
**Reference:** [MDN Web Docs - iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)

### 24. What are data attributes?
**Answer:** Data attributes (`data-*`) allow you to store extra information on standard, semantic HTML elements without other hacks such as non-standard attributes or extra properties on DOM.
**Example:** `<article data-columns="3" data-index-number="12314">...</article>`
**Reference:** [MDN Web Docs - Using data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)

### 25. Explain the `mailto:` protocol.
**Answer:** The `mailto:` protocol is used in an `href` attribute to create a hyperlink that, when clicked, opens the user's default email client with a pre-addressed email.
**Example:** `<a href="mailto:someone@example.com">Send email</a>`
**Reference:** [MDN Web Docs - Email links](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#email_links)

### 26. What is the difference between `id` and `class` attributes?
**Answer:** The `id` attribute is used to uniquely identify a single element on a page. The `class` attribute is used to classify multiple elements to apply the same CSS styling or JavaScript behavior.
**Example:** `<div id="header"></div>` vs `<div class="card"></div><div class="card"></div>`
**Reference:** [MDN Web Docs - id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)

### 27. What does the `action` attribute do in a form?
**Answer:** The `action` attribute specifies where to send the form-data when a form is submitted. It usually points to a server-side script.
**Example:** `<form action="/login.php">`
**Reference:** [MDN Web Docs - form action](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#action)

### 28. What are the method attribute options in a form?
**Answer:** The `method` attribute specifies the HTTP method to use when sending form-data. The two most common are `GET` (appends data to the URL) and `POST` (sends data in the HTTP body).
**Example:** `<form method="POST" action="/submit">`
**Reference:** [MDN Web Docs - form method](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method)

### 29. What is a responsive image in HTML?
**Answer:** Responsive images provide different image files depending on device resolution, viewport size, or layout, ensuring optimal performance and visual quality. This is done using `<picture>` or `srcset`.
**Example:** `<img srcset="small.jpg 500w, large.jpg 1000w" src="large.jpg" alt="Responsive">`
**Reference:** [MDN Web Docs - Responsive images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

### 30. What is the purpose of the `<picture>` tag?
**Answer:** The `<picture>` element allows you to define multiple `<source>` elements and an `<img>` element fallback, letting the browser choose the most appropriate image based on media queries or image format support.
**Example:** `<picture><source media="(min-width:650px)" srcset="img_pink_flowers.jpg"><img src="img_white_flower.jpg" alt="Flowers"></picture>`
**Reference:** [MDN Web Docs - picture tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)


## Hard (50%)

### 31. How does the browser parse HTML and construct the DOM?
**Answer:** The browser reads the raw HTML bytes, converts them to characters, tokenizes them into HTML tags, converts tokens to node objects, and links the nodes in a tree data structure called the Document Object Model (DOM).
**Example:** `<p>Hello</p>` becomes a TextNode("Hello") inside a Paragraph Element node.
**Reference:** [MDN Web Docs - Populating the page: how browsers work](https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work)

### 32. What is the Shadow DOM?
**Answer:** Shadow DOM allows hidden DOM trees to be attached to elements in the regular DOM tree. This is useful for web components to encapsulate styling and markup.
**Example:** `<video>` elements use Shadow DOM to hide their internal playback controls.
**Reference:** [MDN Web Docs - Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM)

### 33. What are HTML Custom Elements?
**Answer:** Custom Elements are a web standard that allows developers to create their own HTML tags, define their behavior with JavaScript, and use them like standard tags.
**Example:** `<my-custom-element></my-custom-element>` defined via `customElements.define('my-custom-element', MyClass)`.
**Reference:** [MDN Web Docs - Using custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)

### 34. What is Content Security Policy (CSP) and how is it implemented in HTML?
**Answer:** CSP is an added layer of security that helps detect and mitigate certain types of attacks, including XSS and data injection. It can be implemented via an HTTP header or a `<meta>` tag.
**Example:** `<meta http-equiv="Content-Security-Policy" content="default-src 'self'">`
**Reference:** [MDN Web Docs - Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

### 35. What is the difference between `script` tags with `defer` vs `async`?
**Answer:** A normal `<script>` pauses HTML parsing to download and execute. `async` downloads in parallel and executes as soon as downloaded (parsing is paused during execution). `defer` downloads in parallel but executes *after* HTML parsing is fully complete.
**Example:** `<script src="script.js" defer></script>`
**Reference:** [MDN Web Docs - Script tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)

### 36. How do HTML5 Server-Sent Events (SSE) work?
**Answer:** Server-Sent Events allow a web page to get updates from a server via an HTTP connection. It's a one-way communication channel from server to client.
**Example:** `const source = new EventSource('demo_sse.php'); source.onmessage = function(event) { console.log(event.data); };`
**Reference:** [MDN Web Docs - Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

### 37. Explain the Accessibility Tree.
**Answer:** Browsers convert the DOM tree into an Accessibility Tree. This tree contains semantic information (roles, states, properties) about elements, which assistive technologies (like screen readers) use to interpret the page for users with disabilities.
**Example:** An `<img>` with an `alt` attribute has a node in the accessibility tree with the role "image" and the name equal to the `alt` text.
**Reference:** [MDN Web Docs - Accessibility tree](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree)

### 38. What are ARIA roles and attributes?
**Answer:** WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) defines roles, states, and properties to make web content and applications more accessible to people with disabilities, especially dynamic content and advanced user interface controls.
**Example:** `<div role="button" aria-pressed="false" tabindex="0">Click Me</div>`
**Reference:** [MDN Web Docs - ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)

### 39. How do you optimize HTML for rendering performance?
**Answer:** Optimize by minifying HTML, deferring/asyncing non-critical scripts, putting CSS in the `<head>`, putting JS at the bottom (or deferring it), avoiding deep DOM trees, and preloading critical assets.
**Example:** `<link rel="preload" href="critical.css" as="style">`
**Reference:** [MDN Web Docs - Web performance](https://developer.mozilla.org/en-US/docs/Web/Performance)

### 40. What is the `<canvas>` element and how is it used?
**Answer:** The `<canvas>` element is used to draw graphics, on the fly, via scripting (usually JavaScript). It can be used for animations, games, data visualization, and photo manipulation.
**Example:** `<canvas id="myCanvas"></canvas>` in HTML, then manipulated using `getContext('2d')` in JS.
**Reference:** [MDN Web Docs - Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

*(Note: These 40 questions serve as a sample of the structure. Expanding to 100+ questions per file will follow this exact format: Question, Answer, Example, and Reference.)*
