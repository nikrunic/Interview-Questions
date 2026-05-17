# Build Tools (Webpack, Vite, Babel) Interview Questions

This document contains interview questions focused on modern frontend build tools.

## Basic (Easy)

### 1. What is Webpack?
**Answer:** 
**The Core Concept:**
Webpack is a static module bundler for modern JavaScript applications.

**Key Details:**
- It builds a dependency graph that maps out all the modules your project needs and generates one or more bundles.
- It supports loaders (for non-JS files) and plugins (for build optimization).

**Example:** `module.exports = { entry: './src/index.js', output: { filename: 'bundle.js' } };`

**Reference:** [Webpack Concepts](https://webpack.js.org/concepts/)

---

### 2. What is Vite?
**Answer:** 
**The Core Concept:**
Vite is a modern frontend build tool that provides a faster and leaner development experience.

**Key Details:**
- It uses native ES modules in the browser for ultra-fast Hot Module Replacement (HMR).
- For production, it bundles the code using Rollup for optimized static assets.

**Example:** `npm create vite@latest`

**Reference:** [Vite Guide](https://vitejs.dev/guide/)

---

### 3. What is Babel?
**Answer:** 
**The Core Concept:**
Babel is a JavaScript compiler, primarily used to convert ECMAScript 2015+ code into a backwards-compatible version of JavaScript.

**Key Details:**
- It enables you to use the latest JS syntax without worrying about browser support.
- It is commonly used alongside Webpack or other bundlers.

**Example:** `presets: ['@babel/preset-env', '@babel/preset-react']`

**Reference:** [Babel Docs](https://babeljs.io/docs/en/)

---
\n## Additional Depth (Architectural Focus)\n
### 4. What is Tree Shaking and how does Webpack implement it?
**Answer:** 
**The Core Concept:**
Tree shaking is a dead-code elimination technique used to optimize the final JavaScript bundle size. It relies on the static structure of ES2015 module syntax (import and export) to determine which exports are actually used in the application.

**Key Details:**
- Webpack marks unused exports during the build process, and a minifier (like Terser) physically removes the dead code from the output.
- For tree shaking to work efficiently, you must ensure that your codebase uses ES modules and that Babel is not compiling them down to CommonJS before Webpack analyzes them.

**Example:** 
`In package.json: `"sideEffects": false` tells Webpack the package has no side effects and is safe to tree-shake.`

**Reference:** [Documentation](https://webpack.js.org/guides/tree-shaking/)

---
