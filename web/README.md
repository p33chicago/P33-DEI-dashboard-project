# Tech Equity Index website

This project uses [SvelteKit](https://kit.svelte.dev/) and [Tailwindcss](https://tailwindcss.com/) - refer to the documentation for these projects for more information.

The build pipeline leverages [adapter-static](https://github.com/sveltejs/kit/tree/master/packages/adapter-static) to generate static web assets - there is no "server" other than the most basic file-based webserver (Github Pages).

## Key files and folders

- [package.json](./package.json) - lists dependencies and commands that can be run with `npm run {command}`
- [src/](./src/) - where all the code we wrote lives
  - [routes/](./src/routes/) - pages of the website; matches URL structure of website; see "Routes" below
  - [lib/](./src/lib/) - code that's either page-agnostic or could be
    - [components/](./src/lib/components/) - Svelte components for use on pages or other components
    - [domain/](./src/lib/domain/) - Types and objects that representing novel concepts central to this project. See [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design) for more info.
    - [p33py_adapter/](./src/lib/p33py_adapter/) - code for converting from p33py's JSON back to the domain model.
- [static/](./static/) - where various images, fonts, and other static assets live; anything in this folder will be available from the website
  - metrics/ and scorecard/ - destination for output from the Python codebase; created by build.py in root of git repo.
- [tests/](./tests/) - automated tests
- [svelte.config.js](./svelte.config.js), [tailwind.config.cjs](./tailwind.config.cjs), and other files in the root of the web/ folder - various config files for the tooling; consult the respective project's documentation for more info.

## Running

```bash
# Install dependencies
npm install
npx playwright install

# Start the development server
npm run dev

# Run tests
npm run test
```

## Building for production

To create a production version of your app:

```bash
npm run build
npm run preview
```

## Routes

SvelteKit uses a filesystem naming convention for creating URLs on the website: URLs are generated for each folder in [src/routes/](./src/routes/), with one exception: parenthesized folders (e.g. "(scorecard)") are ignored (but their contents are not).

To promote good develpment practices, things in routes/ should only contain code that binds state to the UI (via props and attributes) and visa versa (via event handlers); everything else should live in [src/lib/](./src/lib/).

## Updating math equations

We use [KaTex](https://katex.org) to render math equations on the website using the <MathEquation /> component. See katex.org for [a list of available math symbols](https://katex.org/docs/supported.html).
