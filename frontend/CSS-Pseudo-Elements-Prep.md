# CSS Pseudo-Elements — Interview Preparation

Quick reference for common and modern CSS pseudo-elements. Use **double colon** (`::`) for pseudo-elements; single colon (`:`) is legacy syntax for some older browsers.

**Reference:** [MDN — Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

---

## `::before` and `::after`

**What they do:** Create a **virtual child** as the first (`::before`) or last (`::after`) child of the selected element. They require the `content` property (even `content: ""` for decorative use).

**Common uses:** icons, badges, clearfix, tooltips, decorative shapes.

```css
.quote::before {
  content: "“";
  font-size: 2rem;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

**Interview tip:** `::before` / `::after` are **not** in the DOM — you cannot select them with JavaScript as elements.

---

## `::backdrop`

**What it does:** Styles the **fullscreen backdrop** behind a **top layer** element, such as a `<dialog>` opened with `.showModal()`.

**Important:** The backdrop is shown only when the dialog is opened with **`dialog.showModal()`**, not with `.show()` or a normal open state.

```css
dialog::backdrop {
  background: rgba(255, 0, 0, 0.25);
}
```

```html
<dialog id="myDialog">
  <p>Modal content</p>
  <button onclick="myDialog.close()">Close</button>
</dialog>
<script>
  document.getElementById("myDialog").showModal();
</script>
```

**Reference:** [MDN ::backdrop](https://developer.mozilla.org/en-US/docs/Web/CSS/::backdrop)

---

## `::cue` and `::cue-region`

**What they do:** Style **text video cues** (subtitles/captions) for media elements (`<video>`, `<audio>`).

| Pseudo-element | Scope |
|----------------|--------|
| `::cue` | Individual cue (subtitle line) |
| `::cue-region` | Named region that contains cues |

```css
video::cue {
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  font-size: 1.1rem;
}

video::cue-region {
  background: rgba(0, 0, 0, 0.5);
}
```

**Use case:** Custom caption appearance without replacing the entire track UI.

**Reference:** [MDN ::cue](https://developer.mozilla.org/en-US/docs/Web/CSS/::cue)

---

## `::first-letter`

**What it does:** Styles the **first letter** of the first line of a block container (drop caps, magazine-style headings).

```css
p::first-letter {
  font-size: 3em;
  float: left;
  line-height: 1;
  margin-right: 0.1em;
}
```

**Note:** Only applies to block containers; punctuation may be included depending on language rules.

**Reference:** [MDN ::first-letter](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter)

---

## `::first-line`

**What it does:** Styles the **first formatted line** of an element (line length changes with viewport width).

```css
p::first-line {
  font-weight: bold;
  text-transform: uppercase;
}
```

**Interview tip:** If the window is resized, “first line” can change — styles update accordingly.

**Reference:** [MDN ::first-line](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line)

---

## `::file-selector-button`

**What it does:** Styles the **button** part of `<input type="file">` (the “Choose file” control), not the filename text.

```css
input[type="file"]::file-selector-button {
  background: #2563eb;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}
```

**Browser note:** Supported in modern Chromium, Firefox, Safari; check [caniuse](https://caniuse.com) for legacy targets.

**Reference:** [MDN ::file-selector-button](https://developer.mozilla.org/en-US/docs/Web/CSS/::file-selector-button)

---

## `::placeholder`

**What it does:** Styles **placeholder text** in inputs and textareas.

```css
input::placeholder {
  color: #9ca3af;
  font-style: italic;
}
```

**Reference:** [MDN ::placeholder](https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder)

---

## `::selection`

**What it does:** Styles text when the user **highlights/selects** it with the mouse or keyboard.

```css
::selection {
  background: #fde047;
  color: #1f2937;
}
```

**Reference:** [MDN ::selection](https://developer.mozilla.org/en-US/docs/Web/CSS/::selection)

---

## `::marker`

**What it does:** Styles the **list marker** (bullet, number, custom content) of `<li>` elements in `<ul>` / `<ol>`.

```css
li::marker {
  color: #dc2626;
  font-size: 1.2em;
}
```

**Reference:** [MDN ::marker](https://developer.mozilla.org/en-US/docs/Web/CSS/::marker)

---

## `::part()`

**What it does:** Styles **shadow DOM parts** exposed by Web Components via the `part` attribute on internal elements.

```css
/* From outside the component */
my-tabs::part(tab) {
  font-weight: bold;
  border-bottom: 2px solid blue;
}
```

```html
<!-- Inside shadow root -->
<button part="tab">Tab 1</button>
```

**Use case:** Theming/customizing encapsulated components without breaking shadow DOM.

**Reference:** [MDN ::part](https://developer.mozilla.org/en-US/docs/Web/CSS/::part)

---

## `::slotted()`

**What it does:** Styles **elements slotted** into a Web Component’s `<slot>` from the **light DOM** (content projected into the component).

```css
/* In component stylesheet */
::slotted(img) {
  max-width: 100%;
  border-radius: 8px;
}

::slotted(.highlight) {
  background: yellow;
}
```

**Limitation:** Only **direct** slotted children can be targeted (not deeply nested slotted content in all cases).

**Reference:** [MDN ::slotted](https://developer.mozilla.org/en-US/docs/Web/CSS/::slotted)

---

## `::grammar-error` (experimental)

**What it does:** Styles text segments flagged as **grammar errors** by browser spell/grammar check (e.g. underlines).

```css
::grammar-error {
  text-decoration: underline wavy #dc2626;
}
```

**Status:** Experimental — limited browser support. Check MDN before using in production.

**Reference:** [MDN ::grammar-error](https://developer.mozilla.org/en-US/docs/Web/CSS/::grammar-error)

---

## `::spelling-error` (experimental)

**What it does:** Styles text flagged as **spelling mistakes** by the browser.

```css
::spelling-error {
  text-decoration: underline wavy #ea580c;
}
```

**Status:** Experimental — verify support for your target browsers.

**Reference:** [MDN ::spelling-error](https://developer.mozilla.org/en-US/docs/Web/CSS/::spelling-error)

---

## `::target-text` (experimental)

**What it does:** Styles the **specific text fragment** targeted by a URL fragment / Scroll-to-Text directive (e.g. `#:~:text=...` in some browsers).

```css
::target-text {
  background: #fef08a;
  color: #1c1917;
}
```

**Status:** Experimental — part of scroll-to-text and highlight APIs.

**Reference:** [MDN ::target-text](https://developer.mozilla.org/en-US/docs/Web/CSS/::target-text)

---

## Quick comparison table

| Pseudo-element | Main use |
|----------------|----------|
| `::before` / `::after` | Decorative content via `content` |
| `::backdrop` | Modal/dialog overlay |
| `::cue` / `::cue-region` | Video/audio captions |
| `::first-letter` | Drop caps |
| `::first-line` | First line emphasis |
| `::file-selector-button` | File input button styling |
| `::placeholder` | Input placeholder text |
| `::selection` | User text selection highlight |
| `::marker` | List bullets/numbers |
| `::part()` | Web Component `part` API |
| `::slotted()` | Slotted light DOM content |
| `::grammar-error` | Grammar check underline (experimental) |
| `::spelling-error` | Spell check underline (experimental) |
| `::target-text` | URL text fragment highlight (experimental) |

---

## Pseudo-element vs pseudo-class

| | Pseudo-class (`:`) | Pseudo-element (`::`) |
|---|-------------------|------------------------|
| Examples | `:hover`, `:focus`, `:nth-child()` | `::before`, `::after`, `::first-line` |
| Targets | State or position in tree | Specific part of element |

---

## Related in this repo

- [CSS3.md](./CSS3.md) — 100 CSS3 interview Q&A  
- [SCSS.md](./SCSS.md) — preprocessor syntax  
