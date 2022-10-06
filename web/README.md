# P33 PEI dashboard website

For now, this is a [SvelteKit](https://kit.svelte.dev/) starter app with one minor change to the [homepage](./src/routes/index.svelte) to import Plotly figure JSON and render it.

## Pre-requisites

Run both the [ingestion](../ingest.ipynb) and the [transform](../transform.ipynb) notebooks. This should result in a [../data/figure.json](../data/figure.json) and [../data/figure.svelte](../data/figure.svelte) file. The JSON file is curently used, but you can uncomment some code in routes/index.svelte to see how the figure.svelte might be used.

You'll also need to install nodejs (from wherever) and run `npm install`.

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.

## Updating math equations

We use [KaTex](https://katex.org) to render math equations on the website using the <MathEquation /> component. See katex.org for [a list of available math symbols](https://katex.org/docs/supported.html).
