# Angular Interview Questions

This document contains a comprehensive list of 100 Angular interview questions, categorized by difficulty (20 Basic, 30 Medium, 50 Hard). These questions are curated based on popular public Git repositories (e.g., sudheerj/angular-interview-questions).

## Basic (20 Questions)

### 1. What is Angular?
**Answer:** A TypeScript-based open-source front-end web application platform led by the Angular Team at Google.
**Example:** Creating an app: `ng new my-app`
**Reference:** [Angular Official Docs](https://angular.io/docs)

### 2. What is the difference between AngularJS and Angular?
**Answer:** 
**The Core Concept:**
AngularJS (Angular 1.x) uses JavaScript, MVC architecture, and scopes.

**Key Details:**
- Angular (2+) uses TypeScript and a component-based architecture.
**Example:** AngularJS: `$scope.name`. Angular: `name: string;`
**Reference:** [Upgrading from AngularJS](https://angular.io/guide/upgrade)

### 3. What is TypeScript?
**Answer:** A typed superset of JavaScript that compiles to plain JavaScript, providing static typing and ES6+ features.
**Example:** `let count: number = 5;`
**Reference:** [TypeScript Docs](https://www.typescriptlang.org/)

### 4. What are the key components of Angular?
**Answer:** Components, Modules, Templates, Metadata, Data Binding, Directives, Services, and Dependency Injection.
**Example:** N/A
**Reference:** [Architecture overview](https://angular.io/guide/architecture)

### 5. What are Directives?
**Answer:** Classes that add additional behavior to elements in your Angular applications.
**Example:** `*ngIf`, `ngClass`.
**Reference:** [Built-in directives](https://angular.io/guide/built-in-directives)

### 6. What are the different types of directives?
**Answer:** Component Directives (with a template), Structural Directives (change DOM layout), and Attribute Directives (change appearance/behavior).
**Example:** Structural: `*ngFor`. Attribute: `ngModel`.
**Reference:** [Attribute Directives](https://angular.io/guide/attribute-directives)

### 7. What is data binding in Angular?
**Answer:** The mechanism that coordinates what users see (View) with the application's data values (Component).
**Example:** Interpolation `{{ value }}`, Property binding `[property]="value"`.
**Reference:** [Data Binding](https://angular.io/guide/binding-overview)

### 8. Explain two-way data binding.
**Answer:** 
**The Core Concept:**
It combines property binding and event binding.

**Key Details:**
- Changes in the model update the view, and changes in the view update the model.
**Example:** `<input [(ngModel)]="username">`
**Reference:** [Two-way binding](https://angular.io/guide/two-way-binding)

### 9. What are Angular Pipes?
**Answer:** Functions that transform input values to a desired output format for display in the template.
**Example:** `{{ birthday | date:'fullDate' }}`
**Reference:** [Pipes](https://angular.io/guide/pipes)

### 10. What is a Component?
**Answer:** The fundamental building block of an Angular application, containing a TypeScript class, an HTML template, and CSS styles.
**Example:** `@Component({ selector: 'app-hello' })`
**Reference:** [Components](https://angular.io/guide/component-overview)

### 11. What is an Angular Module (NgModule)?
**Answer:** A mechanism to group components, directives, pipes, and services that are related, in such a way that can be combined with other modules.
**Example:** `@NgModule({ declarations: [...], imports: [...] })`
**Reference:** [NgModules](https://angular.io/guide/ngmodules)

### 12. What is the Angular CLI?
**Answer:** Command Line Interface to initialize, develop, scaffold, and maintain Angular applications.
**Example:** `ng generate component user`
**Reference:** [Angular CLI](https://angular.io/cli)

### 13. What is String Interpolation?
**Answer:** A one-way data binding technique to output data from a component to the view using double curly braces.
**Example:** `<h1>{{ title }}</h1>`
**Reference:** [Interpolation](https://angular.io/guide/interpolation)

### 14. What is Property Binding?
**Answer:** A one-way data binding technique to set the property of a view element to the value of a template expression.
**Example:** `<img [src]="imageUrl">`
**Reference:** [Property binding](https://angular.io/guide/property-binding)

### 15. What is Event Binding?
**Answer:** A one-way data binding technique to listen to and respond to user actions such as keystrokes, mouse movements, and clicks.
**Example:** `<button (click)="onSave()">Save</button>`
**Reference:** [Event binding](https://angular.io/guide/event-binding)

### 16. What is the purpose of the `*ngIf` directive?
**Answer:** A structural directive that conditionally includes or excludes a template based on a boolean expression.
**Example:** `<div *ngIf="isLoggedIn">Welcome</div>`
**Reference:** [ngIf](https://angular.io/api/common/NgIf)

### 17. What is the purpose of the `*ngFor` directive?
**Answer:** A structural directive that renders a template for each item in a collection.
**Example:** `<li *ngFor="let user of users">{{ user.name }}</li>`
**Reference:** [ngFor](https://angular.io/api/common/NgForOf)

### 18. What is a Service in Angular?
**Answer:** A broad category encompassing any value, function, or feature that an application needs, usually used to share logic or data across components.
**Example:** `@Injectable() export class DataService {}`
**Reference:** [Services](https://angular.io/guide/architecture-services)

### 19. What is Dependency Injection (DI)?
**Answer:** 
**The Core Concept:**
A design pattern where classes receive their dependencies from an external source rather than creating them.

**Key Details:**
- Angular has its own DI framework.
**Example:** `constructor(private http: HttpClient) {}`
**Reference:** [Dependency Injection](https://angular.io/guide/dependency-injection)

### 20. How do you bootstrap an Angular application?
**Answer:** By defining a root module (`AppModule`) and specifying the root component in its `bootstrap` array, then bootstrapping it in `main.ts`.
**Example:** `platformBrowserDynamic().bootstrapModule(AppModule)`
**Reference:** [Bootstrapping](https://angular.io/guide/bootstrapping)


## Medium (30 Questions)

### 21. What are Lifecycle Hooks in Angular?
**Answer:** Methods that allow you to tap into specific moments in the lifecycle of a component or directive.
**Example:** `ngOnInit()`, `ngOnDestroy()`.
**Reference:** [Lifecycle Hooks](https://angular.io/guide/lifecycle-hooks)

### 22. Explain the difference between constructor and `ngOnInit`.
**Answer:** 
**The Core Concept:**
The constructor is a default TS method used for dependency injection.

**Key Details:**
- `ngOnInit` is an Angular lifecycle hook used for initialization logic after Angular first displays the data-bound properties.
**Example:** Put HTTP calls in `ngOnInit`, not the constructor.
**Reference:** [ngOnInit](https://angular.io/api/core/OnInit)

### 23. What is the difference between Template-driven and Reactive forms?
**Answer:** 
**The Core Concept:**
Template-driven forms rely on directives in the HTML and two-way binding.

**Key Details:**
- Reactive forms provide direct, explicit access to the underlying form object model in the component class.
**Example:** `[(ngModel)]` vs `[formControl]`.
**Reference:** [Forms Overview](https://angular.io/guide/forms-overview)

### 24. What is `FormBuilder`?
**Answer:** A service that provides convenient methods for generating form controls, groups, and arrays in Reactive Forms.
**Example:** `this.fb.group({ name: ['', Validators.required] })`
**Reference:** [FormBuilder](https://angular.io/api/forms/FormBuilder)

### 25. How do you validate a form in Angular?
**Answer:** Using built-in validators (`Validators.required`) or creating custom validator functions.
**Example:** `email: ['', [Validators.required, Validators.email]]`
**Reference:** [Form Validation](https://angular.io/guide/form-validation)

### 26. What is RxJS?
**Answer:** 
**The Core Concept:**
Reactive Extensions for JavaScript.

**Key Details:**
- A library for reactive programming using Observables, heavily integrated into Angular.
**Example:** `Observable.subscribe()`
**Reference:** [Observables](https://angular.io/guide/observables)

### 27. What is an Observable?
**Answer:** A declarative way to perform asynchronous tasks, representing a stream of data that can arrive over time.
**Example:** `const obs = new Observable(subscriber => { subscriber.next(1); });`
**Reference:** [Observables in Angular](https://angular.io/guide/observables-in-angular)

### 28. What is the difference between an Observable and a Promise?
**Answer:** 
**The Core Concept:**
Promises handle a single event and execute immediately.

**Key Details:**
- Observables handle a stream of events, are lazy (don't execute until subscribed), and can be cancelled.
**Example:** `obs.unsubscribe()` (Promises cannot be cancelled).
**Reference:** [Observables vs Promises](https://angular.io/guide/comparing-observables)

### 29. What is a Subject in RxJS?
**Answer:** 
**The Core Concept:**
A special type of Observable that allows values to be multicasted to many Observers.

**Key Details:**
- It is both an Observable and an Observer.
**Example:** `const subject = new Subject<number>(); subject.next(1);`
**Reference:** [RxJS Subject](https://rxjs.dev/guide/subject)

### 30. What is `BehaviorSubject`?
**Answer:** A type of Subject that stores the latest value emitted to its consumers, and whenever a new Observer subscribes, it immediately receives the "current value".
**Example:** `const bSubject = new BehaviorSubject(0);`
**Reference:** [BehaviorSubject](https://rxjs.dev/guide/subject#behaviorsubject)

### 31. How does Angular Routing work?
**Answer:** The Angular Router enables navigation from one view to the next as users perform application tasks, updating the URL without full page reloads.
**Example:** `<router-outlet></router-outlet>`
**Reference:** [Routing and Navigation](https://angular.io/guide/router)

### 32. What is `routerLink`?
**Answer:** A directive that ties a clickable HTML element to a route, allowing navigation.
**Example:** `<a routerLink="/heroes">Heroes</a>`
**Reference:** [RouterLink](https://angular.io/api/router/RouterLink)

### 33. What are Route Guards?
**Answer:** Interfaces (like `CanActivate`) that tell the router whether or not it should allow navigation to a requested route, usually for authentication.
**Example:** `canActivate(): boolean { return this.auth.isLoggedIn(); }`
**Reference:** [Route Guards](https://angular.io/guide/router-tutorial-toh#milestone-5-route-guards)

### 34. What is Content Projection?
**Answer:** A pattern in which you insert, or project, the content you want to use inside another component using `<ng-content>`.
**Example:** `<ng-content select="[header]"></ng-content>`
**Reference:** [Content Projection](https://angular.io/guide/content-projection)

### 35. Explain `@Input()` and `@Output()`.
**Answer:** 
**The Core Concept:**
`@Input()` allows data to flow from a parent to a child component.

**Key Details:**
- `@Output()` allows the child to emit events to the parent using `EventEmitter`.
**Example:** `@Input() name: string; @Output() save = new EventEmitter();`
**Reference:** [Input and Output](https://angular.io/guide/inputs-outputs)

### 36. What is `ViewChild`?
**Answer:** A decorator that configures a view query, allowing a component to access a child component, directive, or DOM element inside its template.
**Example:** `@ViewChild('myInput') inputRef: ElementRef;`
**Reference:** [ViewChild](https://angular.io/api/core/ViewChild)

### 37. What is `HostListener`?
**Answer:** A decorator that declares a DOM event to listen for, and provides a handler method to run when that event occurs on the host element.
**Example:** `@HostListener('click', ['$event']) onClick(e) { ... }`
**Reference:** [HostListener](https://angular.io/api/core/HostListener)

### 38. What is `HostBinding`?
**Answer:** A decorator that marks a DOM property as a host-binding property, keeping it synced with a component property.
**Example:** `@HostBinding('class.active') isActive = true;`
**Reference:** [HostBinding](https://angular.io/api/core/HostBinding)

### 39. What is Angular Material?
**Answer:** A UI component library for Angular developers based on Google's Material Design specification.
**Example:** `import { MatButtonModule } from '@angular/material/button';`
**Reference:** [Angular Material](https://material.angular.io/)

### 40. What is `HttpClient`?
**Answer:** A simplified API for HTTP functionality, resting on top of `XMLHttpRequest`, which returns RxJS Observables.
**Example:** `this.http.get('/api/users')`
**Reference:** [HttpClient](https://angular.io/guide/http)

### 41. How do you pass headers in `HttpClient`?
**Answer:** By passing an options object containing an instance of `HttpHeaders` to the HTTP method.
**Example:** `http.get(url, { headers: new HttpHeaders({'Auth': 'Token'}) })`
**Reference:** [Adding headers](https://angular.io/guide/http#adding-and-updating-headers)

### 42. What are HTTP Interceptors?
**Answer:** Interceptors provide a mechanism to intercept and/or mutate outgoing requests or incoming responses globally.
**Example:** Adding an auth token to every request automatically.
**Reference:** [Interceptors](https://angular.io/guide/http#intercepting-requests-and-responses)

### 43. What is the async pipe?
**Answer:** The `async` pipe subscribes to an Observable or Promise and returns the latest value it has emitted, automatically unsubscribing when the component is destroyed.
**Example:** `<li *ngFor="let u of users$ | async">{{ u.name }}</li>`
**Reference:** [AsyncPipe](https://angular.io/api/common/AsyncPipe)

### 44. What is JIT vs AOT?
**Answer:** 
**The Core Concept:**
Just-in-Time (JIT) compiles the app in the browser at runtime.

**Key Details:**
- Ahead-of-Time (AOT) compiles your Angular HTML and TypeScript code into efficient JavaScript code during the build phase.
**Example:** `ng build` uses AOT by default in newer versions.
**Reference:** [AOT Compiler](https://angular.io/guide/aot-compiler)

### 45. What are Angular Elements?
**Answer:** Angular components packaged as Custom Elements (a web standard), allowing them to be used in non-Angular frameworks or plain HTML.
**Example:** `createCustomElement(MyComponent, { injector })`
**Reference:** [Angular Elements](https://angular.io/guide/elements)

### 46. What is a standalone component?
**Answer:** (Introduced in Angular 14) Components, directives, and pipes that don't need to be declared in an `NgModule`.
**Example:** `@Component({ standalone: true, imports: [CommonModule] })`
**Reference:** [Standalone Components](https://angular.io/guide/standalone-components)

### 47. Explain `ng-template`.
**Answer:** 
**The Core Concept:**
An Angular element used for rendering HTML.

**Key Details:**
- It is never displayed directly; it is used by structural directives (like `*ngIf`) or `ViewContainerRef` to instantiate views.
**Example:** `<ng-template #myTemplate>Content</ng-template>`
**Reference:** [ng-template](https://angular.io/api/core/TemplateRef)

### 48. What is `ng-container`?
**Answer:** 
**The Core Concept:**
A logical container that can be used to group nodes but is not rendered in the DOM tree as a node itself.

**Key Details:**
- Great for avoiding extra `<div>` tags.
**Example:** `<ng-container *ngIf="show">Text</ng-container>`
**Reference:** [ng-container](https://angular.io/guide/structural-directives#grouping-with-ng-container)

### 49. How do you optimize an Angular application?
**Answer:** Use AOT, Lazy Loading, OnPush Change Detection, `trackBy` in `*ngFor`, detach change detectors, and use the `async` pipe.
**Example:** `changeDetection: ChangeDetectionStrategy.OnPush`
**Reference:** [Performance](https://angular.io/guide/workspace-config)

### 50. What is `trackBy` in `*ngFor`?
**Answer:** A function that helps Angular track items in a collection by a unique identifier, preventing re-rendering of the entire list when only some items change.
**Example:** `*ngFor="let i of items; trackBy: trackById"`
**Reference:** [trackBy](https://angular.io/api/common/NgForOf#properties)


## Hard (50 Questions)

### 51. Explain how Change Detection works in Angular.
**Answer:** 
**The Core Concept:**
Angular uses Zone.js to intercept asynchronous events.

**Key Details:**
- When an event fires, Angular traverses the component tree from top to bottom (Change Detector Tree) to check if bindings have changed and updates the DOM.
**Example:** Default strategy checks every component.
**Reference:** [Change Detection](https://angular.io/guide/change-detection)

### 52. What is `ChangeDetectionStrategy.OnPush`?
**Answer:** It tells Angular to only run change detection on a component if its input references change, or an event originates from the component, skipping it during regular change detection cycles.
**Example:** `@Component({ changeDetection: ChangeDetectionStrategy.OnPush })`
**Reference:** [OnPush](https://angular.io/api/core/ChangeDetectionStrategy)

### 53. What is Zone.js?
**Answer:** 
**The Core Concept:**
A library that creates an execution context (zone) across asynchronous tasks.

**Key Details:**
- Angular uses it to know exactly when to trigger change detection.
**Example:** Running outside Angular: `this.ngZone.runOutsideAngular(() => ...)`
**Reference:** [Zone.js](https://angular.io/guide/zone)

### 54. How do you trigger Change Detection manually?
**Answer:** By injecting `ChangeDetectorRef` and calling `markForCheck()` or `detectChanges()`.
**Example:** `constructor(private cdr: ChangeDetectorRef) { cdr.detectChanges(); }`
**Reference:** [ChangeDetectorRef](https://angular.io/api/core/ChangeDetectorRef)

### 55. What is the difference between `markForCheck()` and `detectChanges()`?
**Answer:** 
**The Core Concept:**
`markForCheck()` marks the component and its ancestors as dirty, so they are checked in the *next* cycle.

**Key Details:**
- `detectChanges()` forces an immediate, synchronous check of the component and its children.
**Example:** Use `markForCheck` with Observables and OnPush.
**Reference:** [ChangeDetectorRef](https://angular.io/api/core/ChangeDetectorRef)

### 56. What is `ViewEncapsulation`?
**Answer:** 
**The Core Concept:**
Determines how styles defined in a component apply to the DOM.

**Key Details:**
- Options are Emulated (default, adds scoping attributes), ShadowDom, and None (global styles).
**Example:** `@Component({ encapsulation: ViewEncapsulation.None })`
**Reference:** [View Encapsulation](https://angular.io/guide/view-encapsulation)

### 57. Explain Lazy Loading of modules.
**Answer:** Loading NgModules only when the user navigates to their routes, drastically reducing the initial bundle size and load time.
**Example:** `{ path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }`
**Reference:** [Lazy Loading](https://angular.io/guide/lazy-loading-ngmodules)

### 58. What is `PreloadAllModules` strategy?
**Answer:** A router preloading strategy that loads all lazy-loaded modules in the background *after* the app initializes, improving subsequent navigation speed.
**Example:** `RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })`
**Reference:** [Preloading](https://angular.io/guide/router#preloading-background-loading-of-feature-areas)

### 59. Explain the RxJS `switchMap` operator.
**Answer:** It maps each value to an Observable, then flattens all inner Observables, but *cancels* the previous inner Observable when a new one arrives.
**Example:** Useful for search typeaheads to cancel old HTTP requests.
**Reference:** [switchMap](https://rxjs.dev/api/operators/switchMap)

### 60. Explain the RxJS `mergeMap` operator.
**Answer:** It maps each value to an Observable and merges all inner Observables concurrently without cancelling any.
**Example:** Saving multiple unrelated items to a database concurrently.
**Reference:** [mergeMap](https://rxjs.dev/api/operators/mergeMap)

### 61. Explain the RxJS `concatMap` operator.
**Answer:** It maps values to inner Observables and subscribes to them in strict sequential order, waiting for one to complete before starting the next.
**Example:** Executing database inserts in exact order.
**Reference:** [concatMap](https://rxjs.dev/api/operators/concatMap)

### 62. How do you prevent memory leaks in Angular?
**Answer:** By unsubscribing from Observables in `ngOnDestroy()`, using the `async` pipe, or using RxJS operators like `takeUntil`.
**Example:** `this.obs$.pipe(takeUntil(this.destroy$)).subscribe();`
**Reference:** [Observables Best Practices](https://angular.io/guide/observables-in-angular)

### 63. What is a Resolver in Angular Routing?
**Answer:** 
**The Core Concept:**
A service that acts as a data provider, used to fetch data *before* a component is loaded via routing.

**Key Details:**
- The router waits for the resolver to finish before activating the route.
**Example:** `resolve(route: ActivatedRouteSnapshot) { return this.api.getData(); }`
**Reference:** [Resolve](https://angular.io/api/router/Resolve)

### 64. What is a Custom Form Validator?
**Answer:** A function that implements the `ValidatorFn` interface, returning `null` if valid or an error object if invalid, which can be applied to `FormControls`.
**Example:** `function forbiddenNameValidator(nameRe: RegExp): ValidatorFn { ... }`
**Reference:** [Custom Validators](https://angular.io/guide/form-validation#custom-validators)

### 65. What are `ControlValueAccessor` interfaces?
**Answer:** The interface that acts as a bridge between the Angular forms API and a native DOM element, used to build custom form controls that work with `ngModel` and `formControlName`.
**Example:** Implementing `writeValue()`, `registerOnChange()`, etc.
**Reference:** [ControlValueAccessor](https://angular.io/api/forms/ControlValueAccessor)

### 66. How does Hierarchical Dependency Injection work?
**Answer:** 
**The Core Concept:**
Angular has an Injector tree.

**Key Details:**
- If a component asks for a dependency, Angular checks its injector.
- If not found, it checks the parent, all the way up to the root injector.
- If a provider is redefined at a component level, it creates a new instance for that sub-tree.
**Example:** `providers: [MyService]` inside `@Component` creates a local instance.
**Reference:** [Hierarchical Injectors](https://angular.io/guide/hierarchical-dependency-injection)

### 67. What is the `providedIn: 'root'` syntax?
**Answer:** 
**The Core Concept:**
It registers a service as a singleton in the root injector.

**Key Details:**
- It enables tree-shaking, meaning if the service is never injected, it is removed from the compiled bundle.
**Example:** `@Injectable({ providedIn: 'root' })`
**Reference:** [Tree-shakable providers](https://angular.io/guide/dependency-injection-providers#tree-shakable-providers)

### 68. What are InjectionTokens?
**Answer:** Objects used as injection tokens when the thing being injected is not a class (like an interface, a string, or a configuration object).
**Example:** `const APP_CONFIG = new InjectionToken<AppConfig>('app.config');`
**Reference:** [InjectionToken](https://angular.io/api/core/InjectionToken)

### 69. What is `@Self()`, `@Optional()`, `@SkipSelf()`, and `@Host()`?
**Answer:** 
**The Core Concept:**
Resolution modifiers for DI.

**Key Details:**
- `@Self` looks only in the local injector.
- `@Optional` prevents errors if not found.
- `@SkipSelf` starts searching from the parent.
- `@Host` stops searching at the host component.
**Example:** `constructor(@Optional() private service: MyService)`
**Reference:** [Resolution Modifiers](https://angular.io/guide/hierarchical-dependency-injection#resolution-modifiers)

### 70. How do you implement Server-Side Rendering (SSR) in Angular?
**Answer:** 
**The Core Concept:**
Using Angular Universal.

**Key Details:**
- It executes Angular on a Node.js server, generating static application pages that get bootstrapped on the client.
**Example:** `ng add @nguniversal/express-engine`
**Reference:** [Angular Universal](https://angular.io/guide/universal)

### 71. What is hydration in Angular Universal?
**Answer:** 
**The Core Concept:**
The process of restoring the application state on the client side using the HTML sent by the server, rather than destroying and recreating the DOM.

**Key Details:**
- (Angular 16+ has non-destructive hydration).
**Example:** `provideClientHydration()`
**Reference:** [Hydration](https://angular.io/guide/hydration)

### 72. Explain the use of `ng-content` with multiple slots.
**Answer:** You can project content into specific locations in a component by using the `select` attribute on `<ng-content>`.
**Example:** `<ng-content select="[header]"></ng-content>`
**Reference:** [Multi-slot projection](https://angular.io/guide/content-projection#multi-slot-content-projection)

### 73. What is a structural directive under the hood?
**Answer:** 
**The Core Concept:**
Syntactic sugar for an `<ng-template>`.

**Key Details:**
- Angular translates `*ngIf="condition"` into `<ng-template [ngIf]="condition">...`.
**Example:** `*ngIf` asterisk syntax.
**Reference:** [Structural Directives asterisk](https://angular.io/guide/structural-directives#the-asterisk--prefix)

### 74. How do you create a custom structural directive?
**Answer:** 
**The Core Concept:**
Inject `TemplateRef` and `ViewContainerRef` in the constructor.

**Key Details:**
- Use `viewContainer.createEmbeddedView(templateRef)` to render it.
**Example:** `@Directive({ selector: '[appUnless]' })`
**Reference:** [Writing structural directives](https://angular.io/guide/structural-directives#creating-a-structural-directive)

### 75. What is `APP_INITIALIZER`?
**Answer:** 
**The Core Concept:**
An injection token that allows you to provide a function that is executed during the application bootstrap process.

**Key Details:**
- App execution halts until the Promise/Observable it returns completes.
**Example:** Used to fetch configuration before the app starts.
**Reference:** [APP_INITIALIZER](https://angular.io/api/core/APP_INITIALIZER)

### 76. Explain State Management with NgRx.
**Answer:** 
**The Core Concept:**
NgRx is a Redux-inspired state management library for Angular, utilizing RxJS.

**Key Details:**
- It involves Actions, Reducers, Selectors, and Effects to manage global state securely and predictably.
**Example:** `this.store.dispatch(loadUsers())`
**Reference:** [NgRx Docs](https://ngrx.io/)

### 77. What are NgRx Effects?
**Answer:** 
**The Core Concept:**
An RxJS-powered side effect model for NgRx Store.

**Key Details:**
- They listen for actions dispatched from the store, perform asynchronous operations (like HTTP calls), and dispatch new actions on completion.
**Example:** `loadUsers$ = createEffect(() => this.actions$.pipe(ofType(loadUsers), mergeMap(...)))`
**Reference:** [NgRx Effects](https://ngrx.io/guide/effects)

### 78. What is `RouterOutlet` events?
**Answer:** 
**The Core Concept:**
The `<router-outlet>` emits events when a component is inserted or removed.

**Key Details:**
- `(activate)` and `(deactivate)` can be used to run animations or logic.
**Example:** `<router-outlet (activate)="onActivate($event)"></router-outlet>`
**Reference:** [RouterOutlet Events](https://angular.io/api/router/RouterOutlet)

### 79. Explain Angular Signals.
**Answer:** 
**The Core Concept:**
(Introduced in Angular 16) Signals provide a reactive primitive for managing state.

**Key Details:**
- A signal is a wrapper around a value that can notify interested consumers when that value changes, aiming to eventually make Zone.js optional.
**Example:** `const count = signal(0); count.set(1);`
**Reference:** [Angular Signals](https://angular.io/guide/signals)

### 80. How do computed signals work?
**Answer:** 
**The Core Concept:**
A `computed` signal derives its value from other signals.

**Key Details:**
- It is lazily evaluated and memoized, recalculating only when its dependencies change.
**Example:** `const doubleCount = computed(() => count() * 2);`
**Reference:** [Computed Signals](https://angular.io/guide/signals#computed-signals)

### 81. How do you handle API integration with proper error handling and loading states in Angular?
**Answer:** 
**The Core Concept:**
By wrapping HTTP calls in services, using RxJS `catchError` for centralized error handling, and exposing `BehaviorSubject` or Signals for loading states.

**Key Details:**
- Interceptors are used for global error catching and token injection.
**Example:** `return this.http.get(url).pipe(catchError(this.handleError));`
**Reference:** [Angular HTTP Guide](https://angular.io/guide/http)

### 82. What’s your approach to optimizing performance — especially when dealing with large lists or change detection?
**Answer:** Use `ChangeDetectionStrategy.OnPush` to prevent unnecessary checks, `trackBy` in `*ngFor` to prevent DOM recreation, and Virtual Scrolling (`@angular/cdk/scrolling`) for rendering only visible items in massive lists.
**Example:** `<cdk-virtual-scroll-viewport itemSize="50"> <div *cdkVirtualFor="let item of items"></div>`
**Reference:** [Angular Virtual Scrolling](https://material.angular.io/cdk/scrolling/overview)

### 83. Suppose your API returns a list in random order, how would you sort and display it efficiently using pipes or RxJS operators?
**Answer:** 
**The Core Concept:**
Sorting inside a pure pipe is an anti-pattern due to performance hits on every change detection cycle.

**Key Details:**
- The best approach is to sort the data using the RxJS `map` operator before assigning it to the template binding.
**Example:** `this.data$ = this.api.getData().pipe(map(items => items.sort((a,b) => a.id - b.id)));`
**Reference:** [RxJS Map](https://rxjs.dev/api/operators/map)

### 84. How do you implement role-based authentication and route guards in an Angular app?
**Answer:** 
**The Core Concept:**
By implementing the `CanActivate` (or `CanMatch` in newer versions) interface.

**Key Details:**
- The guard injects an AuthService, checks if the user's role matches the required roles specified in the route's `data` object, and redirects if unauthorized.
**Example:** `{ path: 'admin', component: AdminComponent, canActivate: [RoleGuard], data: { expectedRole: 'admin' } }`
**Reference:** [Angular Route Guards](https://angular.io/guide/router-tutorial-toh#milestone-5-route-guards)

### 85. What are the lifecycle hooks used during component initialization, and how can misuse of them cause performance issues?
**Answer:** 
**The Core Concept:**
`ngOnChanges`, `ngOnInit`, `ngDoCheck`, and `ngAfterViewInit`.

**Key Details:**
- Misusing `ngDoCheck` (running heavy logic) causes massive performance drops because it fires on every single change detection cycle.
**Example:** Executing API calls inside `ngDoCheck` instead of `ngOnInit`.
**Reference:** [Angular Lifecycle Hooks](https://angular.io/guide/lifecycle-hooks)

### 86. How do you deal with memory leaks caused by Observables and subscriptions?
**Answer:** 
**The Core Concept:**
Always unsubscribe in `ngOnDestroy`.

**Key Details:**
- Better yet, use the `async` pipe in templates which automatically subscribes/unsubscribes, or use RxJS operators like `takeUntil(this.destroy$)` or `take(1)`.
**Example:** `this.mySub$.pipe(takeUntil(this.destroy$)).subscribe();`
**Reference:** [RxJS takeUntil](https://rxjs.dev/api/operators/takeUntil)

### 87. What is an ngModule?
**Answer:** 
**The Core Concept:**
An NgModule is a class decorated with `@NgModule` that defines a module in Angular.

**Key Details:**
- It acts as a container for a cohesive block of functionality, grouping related components, directives, pipes, and services.
- It helps organize code, configure the compiler, and control visibility.
**Example:** `@NgModule({ declarations: [AppComponent], imports: [BrowserModule], bootstrap: [AppComponent] })`
**Reference:** [GreatFrontEnd Angular Questions](https://github.com/greatfrontend/top-angular-interview-questions)

### 88. What are directives and what are its types?
**Answer:** 
**The Core Concept:**
Directives are classes that add behavior to elements in an application.

**Key Details:**
- There are three types: Component directives (directives with a template), Structural directives (change DOM layout, e.g., `*ngIf`), and Attribute directives (change appearance or behavior of existing elements, e.g., `NgClass`).
**Example:** `<div *ngIf="isVisible">Visible</div>`
**Reference:** [GreatFrontEnd Angular Questions](https://github.com/greatfrontend/top-angular-interview-questions)

### 89. What is the difference between component and directive?
**Answer:** 
**The Core Concept:**
Both are classes decorated with metadata interacting with the DOM.

**Key Details:**
- A Component is a special type of directive that always has a template and encapsulated styles (creating reusable UI blocks).
- A Directive modifies the behavior or appearance of an existing element but does not have a template.
**Example:** `AppComponent` vs `NgModel`.
**Reference:** [GreatFrontEnd Angular Questions](https://github.com/greatfrontend/top-angular-interview-questions)

### 90. What is the difference between constructor and ngOnInit()?
**Answer:** 
**The Core Concept:**
The `constructor` is a standard TypeScript feature used for initializing class members and dependency injection.

**Key Details:**
- `ngOnInit()` is an Angular lifecycle hook called after Angular has initialized all data-bound properties (`@Input`).
- Component logic should live in `ngOnInit`.
**Example:** Inject `HttpClient` in `constructor`, call API in `ngOnInit`.
**Reference:** [GreatFrontEnd Angular Questions](https://github.com/greatfrontend/top-angular-interview-questions)

### 91. What are decorators?
**Answer:** 
**The Core Concept:**
Decorators are a TypeScript feature used to add metadata to classes, methods, or properties.

**Key Details:**
- Angular uses them to configure classes, telling the compiler how to process them (e.g., `@Component`, `@Injectable`, `@Input`).
**Example:** `@Component({ selector: 'app-root' })`
**Reference:** [GreatFrontEnd Angular Questions](https://github.com/greatfrontend/top-angular-interview-questions)


### 92. How does Angular handle change detection differently with `OnPush` strategy?
**Answer:** 
**The Core Concept:**
`OnPush` tells Angular to run change detection for a component only when its `@Input()` references change, an event originates from the component (or its children), or change detection is triggered manually (`markForCheck()`).

**Key Details:**
- This drastically improves performance by skipping the component tree when deeply nested objects mutate without a reference change.
**Example:** `@Component({ changeDetection: ChangeDetectionStrategy.OnPush })`
**Reference:** [Angular Change Detection](https://angular.io/guide/change-detection)

### 93. Explain the difference between `mergeMap`, `switchMap`, `concatMap`, and `exhaustMap`.
**Answer:** 
**The Core Concept:**
They are RxJS flattening operators.

**Key Details:**
- `mergeMap` runs all inner observables concurrently.
- `switchMap` cancels the previous inner observable and starts a new one (great for searches).
- `concatMap` queues them in order.
- `exhaustMap` ignores new inner observables while the current one is still executing (great for submit buttons).
**Example:** `fromEvent(input, 'input').pipe(switchMap(e => fetch(e)))`
**Reference:** [RxJS Operators](https://rxjs.dev/guide/operators)

### 94. How do you implement global error handling in Angular?
**Answer:** 
**The Core Concept:**
By implementing the `ErrorHandler` interface provided by Angular core.

**Key Details:**
- You create a custom class, override the `handleError(error)` method to log or display toast notifications, and then provide it in the `AppModule` using `{ provide: ErrorHandler, useClass: CustomErrorHandler }`.
**Example:** `class GlobalErrorHandler implements ErrorHandler { handleError(error) { console.error(error); } }`
**Reference:** [Angular ErrorHandler](https://angular.io/api/core/ErrorHandler)

### 95. What are Angular Signals introduced in Angular 16+?
**Answer:** 
**The Core Concept:**
Signals are a new, reactive core primitive that tells Angular exactly when and where data changes.

**Key Details:**
- Unlike RxJS Observables, Signals always have a current value and are synchronous.
- They enable fine-grained change detection, meaning Angular can update the exact DOM node that changed without checking the entire component tree.
**Example:** `count = signal(0); update() { this.count.update(c => c + 1); }`
**Reference:** [Angular Signals](https://angular.io/guide/signals)

### 96. How do Standalone Components change Angular architecture?
**Answer:** 
**The Core Concept:**
Introduced in Angular 14, Standalone Components remove the requirement to declare components inside an `NgModule`.

**Key Details:**
- They manage their own dependencies (imports) directly within the `@Component` decorator, vastly simplifying the learning curve and reducing boilerplate.
**Example:** `@Component({ standalone: true, imports: [CommonModule] })`
**Reference:** [Angular Standalone Components](https://angular.io/guide/standalone-components)

### 97. What is Server-Side Rendering (SSR) in Angular Universal (Angular 17+)?
**Answer:** 
**The Core Concept:**
SSR renders the Angular application into static HTML on the server before sending it to the client.

**Key Details:**
- This drastically improves SEO (search engines can index the HTML) and the initial load time (First Contentful Paint), before the client-side JavaScript takes over (hydration).
**Example:** Using `@angular/ssr` or Angular Universal packages.
**Reference:** [Angular SSR](https://angular.io/guide/ssr)

### 98. How do you protect routes in Angular using Route Guards?
**Answer:** 
**The Core Concept:**
Route guards are interfaces (`CanActivate`, `CanDeactivate`, `CanLoad`, etc.) that determine if a user can navigate to or from a route based on custom logic (e.g., authentication status).

**Key Details:**
- In modern Angular, these are often implemented as functional guards returning an Observable or boolean.
**Example:** `const authGuard: CanActivateFn = (route, state) => inject(AuthService).isLoggedIn();`
**Reference:** [Angular Route Guards](https://angular.io/guide/router-tutorial-toh#milestone-5-route-guards)

### 99. What is a Memory Leak in Angular and how do you prevent it?
**Answer:** 
**The Core Concept:**
A memory leak occurs when an object is no longer needed but cannot be garbage collected because a reference remains.

**Key Details:**
- In Angular, this commonly happens when RxJS subscriptions are not closed.
- Prevent it by using the `async` pipe in templates, or by unsubscribing in the `ngOnDestroy` lifecycle hook.
**Example:** `this.sub = data$.subscribe(); ngOnDestroy() { this.sub.unsubscribe(); }`
**Reference:** [RxJS Unsubscribe Best Practices](https://angular.io/guide/observables)

### 100. How does Angular's Dependency Injection (DI) system work hierarchically?
**Answer:** 
**The Core Concept:**
Angular's DI system provides singleton instances of services based on the provider scope.

**Key Details:**
- If provided at `providedIn: 'root'`, it's a global singleton.
- If provided in a specific `@Component`, a new instance is created for that component and its children.
- The injector tree matches the component tree, allowing children to override parent services.
**Example:** `@Injectable({ providedIn: 'root' })`
**Reference:** [Angular Hierarchical DI](https://angular.io/guide/hierarchical-dependency-injection)
