# Build Tools (Webpack, Vite, Babel) Interview Questions

This document contains interview questions focused on modern frontend build tools.

## Basic Questions

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

---

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

---

## Intermediate Questions

---

## Intermediate Questions

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

## Additional Depth (Architectural Focus)


---

---

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

---

## Expert Questions

## Practice Questions

---

## Expert Questions

### 1. Build a basic webpack.config.js handling TypeScript and CSS bundle extraction.

**Example Solution:**
```javascript
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/index.ts",
  module: {
    rules: [
      { test: /\.tsx?$/, use: "ts-loader", exclude: /node_modules/ },
      { test: /\.css$/, use: [MiniCssExtractPlugin.loader, "css-loader"] }
    ]
  },
  resolve: { extensions: [".tsx", ".ts", ".js"] },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
    clean: true
  },
  plugins: [new MiniCssExtractPlugin()]
};
```

---

### 2. Configure bundle code-splitting via standard `optimization.splitChunks` blocks.

**Example Solution:**
```javascript
module.exports = {
  // ... entry, output, rules
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
  },
};
```

---

## Practice Questions

### 1. Build a basic webpack.config.js handling TypeScript and CSS bundle extraction.

**Example Solution:**
```javascript
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/index.ts",
  module: {
    rules: [
      { test: /\.tsx?$/, use: "ts-loader", exclude: /node_modules/ },
      { test: /\.css$/, use: [MiniCssExtractPlugin.loader, "css-loader"] }
    ]
  },
  resolve: { extensions: [".tsx", ".ts", ".js"] },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
    clean: true
  },
  plugins: [new MiniCssExtractPlugin()]
};
```

### 2. Configure bundle code-splitting via standard `optimization.splitChunks` blocks.

**Example Solution:**
```javascript
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
  },
};
```

### 3. Configure a Webpack compression compiler plugin for GZIP bundle assets.

**Example Solution:**
```javascript
const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  plugins: [
    new CompressionPlugin({
      algorithm: "gzip",
      test: /\.js$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ]
};
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Webpack & Build Tooling application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Webpack & Build Tooling operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Webpack & Build Tooling configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Webpack & Build Tooling event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Webpack & Build Tooling with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Webpack & Build Tooling performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Webpack & Build Tooling failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Webpack & Build Tooling data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Webpack & Build Tooling state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Webpack & Build Tooling logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Webpack & Build Tooling files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Webpack & Build Tooling connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Webpack & Build Tooling.

*(Challenge question for self-study and practical project implementation.)*

