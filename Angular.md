# Angular Interview Questions

This document contains a comprehensive list of Angular interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is Angular?
**Answer:** Angular is a TypeScript-based open-source web application framework led by the Angular Team at Google. It is used for building single-page client applications using HTML and TypeScript.
**Example:** Creating a new app using CLI: `ng new my-app`
**Reference:** [Angular Official Docs](https://angular.io/docs)

### 2. What is the difference between AngularJS and Angular?
**Answer:** AngularJS (Angular 1.x) is based on JavaScript and uses scopes and controllers. Angular (Angular 2+) is a complete rewrite, based on TypeScript, and uses a component-based architecture.
**Example:** AngularJS uses `$scope`, Angular uses `export class MyComponent { ... }`.
**Reference:** [Angular - Upgrading from AngularJS](https://angular.io/guide/upgrade)

### 3. What are Components in Angular?
**Answer:** Components are the main building block for Angular applications. Each component consists of an HTML template, a TypeScript class that defines behavior, and a CSS selector that defines how the component is used in a template.
**Example:** `@Component({ selector: 'app-root', templateUrl: './app.component.html' })`
**Reference:** [Angular Docs - Components](https://angular.io/guide/component-overview)

### 4. What are Directives?
**Answer:** Directives are classes that add new behavior or modify the DOM structure. There are three types: Components (directives with a template), Structural directives (change DOM layout like `*ngIf`), and Attribute directives (change appearance/behavior like `ngClass`).
**Example:** `<div *ngIf="isTrue">Visible</div>`
**Reference:** [Angular Docs - Built-in directives](https://angular.io/guide/built-in-directives)

### 5. What is `*ngIf`?
**Answer:** `*ngIf` is a structural directive that conditionally includes or excludes a template based on a boolean expression.
**Example:** `<p *ngIf="showText">This is conditionally shown.</p>`
**Reference:** [Angular Docs - ngIf](https://angular.io/api/common/NgIf)

### 6. What is Data Binding in Angular?
**Answer:** Data binding is a mechanism that connects the application's UI (template) to the data models (component class). It can be one-way (Interpolation `{{ }}`, Property binding `[]`, Event binding `()`) or two-way (`[()]`).
**Example:** `<h1>{{ title }}</h1>`
**Reference:** [Angular Docs - Property binding](https://angular.io/guide/property-binding)

### 7. What is Two-way Data Binding?
**Answer:** Two-way data binding allows for the automatic synchronization of data between the model and the view. It is achieved using the `ngModel` directive.
**Example:** `<input [(ngModel)]="username">`
**Reference:** [Angular Docs - Two-way binding](https://angular.io/guide/two-way-binding)

### 8. What is the Angular CLI?
**Answer:** The Angular Command Line Interface (CLI) is a tool to initialize, develop, scaffold, and maintain Angular applications directly from a command shell.
**Example:** `ng generate component my-comp`
**Reference:** [Angular Docs - CLI](https://angular.io/cli)


## Medium (30%)

### 9. What are Angular Services?
**Answer:** Services are classes with a well-defined purpose, often used to share data, logic, and functions across different components in an application. They are typically injected using Dependency Injection.
**Example:** `@Injectable({ providedIn: 'root' }) export class DataService { }`
**Reference:** [Angular Docs - Services and Dependency Injection](https://angular.io/guide/architecture-services)

### 10. Explain Dependency Injection (DI) in Angular.
**Answer:** DI is a design pattern in which a class requests dependencies from external sources rather than creating them itself. Angular has its own DI framework that creates and provides instances of dependencies (like services) to classes that request them.
**Example:** `constructor(private dataService: DataService) {}`
**Reference:** [Angular Docs - Dependency Injection](https://angular.io/guide/dependency-injection)

### 11. What is RxJS and how does Angular use it?
**Answer:** RxJS (Reactive Extensions for JavaScript) is a library for reactive programming using Observables. Angular uses it heavily for handling asynchronous operations, such as HTTP requests (`HttpClient`), routing events, and form value changes.
**Example:** `this.http.get(url).subscribe(data => console.log(data));`
**Reference:** [Angular Docs - Observables in Angular](https://angular.io/guide/observables-in-angular)

### 12. What are Angular Pipes?
**Answer:** Pipes are simple functions to use in template expressions to accept an input value and return a transformed value. They are used for formatting data like dates, currency, and uppercase text.
**Example:** `<p>The hero's birthday is {{ birthday | date:"MM/dd/yy" }}</p>`
**Reference:** [Angular Docs - Pipes](https://angular.io/guide/pipes)

### 13. What is the difference between Template-driven forms and Reactive forms?
**Answer:** Template-driven forms rely heavily on directives in the template to create and manipulate the underlying object model. Reactive forms provide direct, explicit access to the underlying form's object model and use reactive programming principles (Observables).
**Example:** `[(ngModel)]` vs `[formControl]="myControl"`
**Reference:** [Angular Docs - Reactive and template-driven forms](https://angular.io/guide/forms-overview)

### 14. What is a Module (`NgModule`) in Angular?
**Answer:** An `NgModule` is a class marked by the `@NgModule` decorator. It configures the injector and the compiler and helps organize related things together. It defines the components, directives, pipes, and services used by the application block.
**Example:** `@NgModule({ declarations: [AppComponent], imports: [BrowserModule], bootstrap: [AppComponent] })`
**Reference:** [Angular Docs - NgModules](https://angular.io/guide/ngmodules)


## Hard (50%)

### 15. Explain the Component Lifecycle Hooks.
**Answer:** Lifecycle hooks are methods that Angular calls at specific moments during a component's or directive's life. Key hooks include `ngOnChanges`, `ngOnInit`, `ngDoCheck`, `ngAfterViewInit`, and `ngOnDestroy`.
**Example:** `ngOnInit() { this.loadData(); }` runs once after the first `ngOnChanges`.
**Reference:** [Angular Docs - Lifecycle hooks](https://angular.io/guide/lifecycle-hooks)

### 16. What is Ahead-of-Time (AOT) compilation?
**Answer:** AOT compilation converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase *before* the browser downloads and runs that code. It provides faster rendering, smaller bundle sizes, and catches template errors early.
**Example:** `ng build --aot`
**Reference:** [Angular Docs - AOT Compiler](https://angular.io/guide/aot-compiler)

### 17. How do Route Guards work in Angular?
**Answer:** Route guards are interfaces that can tell the router whether or not it should allow navigation to a requested route. Common guards are `CanActivate`, `CanDeactivate`, `Resolve`, and `CanLoad`.
**Example:** `canActivate() { return this.authService.isLoggedIn(); }`
**Reference:** [Angular Docs - Routing & Navigation (Guards)](https://angular.io/guide/router-tutorial-toh#milestone-5-route-guards)

### 18. What is the `async` pipe?
**Answer:** The `async` pipe subscribes to an Observable or Promise and returns the latest value it has emitted. When a new value is emitted, the pipe marks the component to be checked for changes. It also automatically unsubscribes to avoid memory leaks.
**Example:** `<div *ngIf="user$ | async as user">{{ user.name }}</div>`
**Reference:** [Angular Docs - AsyncPipe](https://angular.io/api/common/AsyncPipe)

### 19. What is content projection and `ng-content`?
**Answer:** Content projection is a pattern in which you insert, or project, the content you want to use inside another component. It is achieved using the `<ng-content>` tag, which acts as a placeholder.
**Example:** In a Card component: `<div><ng-content></ng-content></div>`. Usage: `<app-card><h2>Projected Title</h2></app-card>`.
**Reference:** [Angular Docs - Content projection](https://angular.io/guide/content-projection)

### 20. How does Change Detection work in Angular?
**Answer:** Angular uses a tree of Change Detectors. When an asynchronous event occurs (DOM event, Timer, XHR), Zone.js notifies Angular, which then triggers a top-down check of the component tree to update the DOM if the model has changed.
**Example:** `ChangeDetectionStrategy.Default` checks the whole tree.
**Reference:** [Angular Docs - Optimizing with ChangeDetectionStrategy](https://angular.io/guide/change-detection-strategy)

### 21. What is `ChangeDetectionStrategy.OnPush`?
**Answer:** `OnPush` strategy tells Angular to only run change detection for a component if its input references change, if an event originates from the component or one of its children, or if you manually trigger it (e.g., using `async` pipe or `ChangeDetectorRef`).
**Example:** `@Component({ changeDetection: ChangeDetectionStrategy.OnPush })`
**Reference:** [Angular Docs - OnPush strategy](https://angular.io/guide/change-detection-strategy#onpush)

### 22. What are Interceptors in Angular?
**Answer:** HTTP Interceptors allow you to inspect and transform HTTP requests before they are sent to the server, and to inspect and transform HTTP responses on their way back to the application.
**Example:** Adding an Authorization token to headers globally.
**Reference:** [Angular Docs - Intercepting requests and responses](https://angular.io/guide/http#intercepting-requests-and-responses)

### 23. What is lazy loading and how is it implemented?
**Answer:** Lazy loading is a technique to load NgModules only when they are needed, decreasing the initial bundle size and load time. It is implemented in the router configuration using `loadChildren`.
**Example:** `{ path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }`
**Reference:** [Angular Docs - Lazy-loading feature modules](https://angular.io/guide/lazy-loading-ngmodules)

### 24. Explain ViewChild and ContentChild.
**Answer:** `@ViewChild` allows a component to query and access a directive, child component, or DOM element inside its own template view. `@ContentChild` allows a component to access elements projected into it via `<ng-content>`.
**Example:** `@ViewChild('myInput') inputElem: ElementRef;`
**Reference:** [Angular Docs - ViewChild](https://angular.io/api/core/ViewChild)

### 25. What is Zone.js?
**Answer:** Zone.js is a library that provides an execution context (a "zone") that persists across asynchronous tasks. Angular uses it to know when asynchronous operations (like `setTimeout`, HTTP calls, or clicks) finish, so it can automatically trigger change detection.
**Example:** N/A (Internal dependency).
**Reference:** [Angular Docs - Zone.js](https://angular.io/guide/zone)
